#!/usr/bin/env python3
#encoding:UTF-8
# # login.pyベースの登録フォーム(Twitterの認証からコールバック)
def get(c, user):
    user_id = user["screen_name"]
    print('<meta http-equiv="refresh" content="0.01;URL=./index.py">')
    str = textwrap.dedent('''
    <p>Authentication succeeded</p>
    <p>You can enjoy our APP! </p>
    <a href='./index.py'>Back to index page</a>
    ''')
    return str

#---------------------------------------------
# プログラム本体
#---------------------------------------------
import cgi
import cgitb
import sqlite3
import textwrap
from http import cookies
import hashlib
import io,sys
import requests
import os
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cgitb.enable()
#ローカル
conn = sqlite3.connect('./clothes/dresser.db')
#本番環境
#conn = sqlite3.connect('../clothes/dresser.db')
# twitter
tokens,user = {},{}
oauth = os.environ.get("QUERY_STRING").split("&")
for s in oauth:
    if s.split("=")[0] == "oauth_token":
        tokens["oauth_token"] = s.split("=")[1]
    elif s.split("=")[0] == "oauth_verifier":
        tokens["oauth_verifier"] = s.split("=")[1]
# access_tokenをPOSTでリクエストし、取得
request = "https://api.twitter.com/oauth/access_token?oauth_token={}&oauth_verifier={}".format(tokens["oauth_token"],tokens["oauth_verifier"])
response = requests.get(request).text.split("&")
# レスポンスからデータを取得
for s in response:
    if s.split("=")[0] == "oauth_token":
        user["oauth_token"] = s.split("=")[1]
    elif s.split("=")[0] == "oauth_token_secret":
        user["oauth_token_secret"] = s.split("=")[1]
    elif s.split("=")[0] == "user_id":
        user["user_id"] = s.split("=")[1]
    elif s.split("=")[0] == "screen_name":
        user["screen_name"] = s.split("=")[1]
        
c = conn.cursor()
form = cgi.FieldStorage()
# ユーザidはtwitterのスクリーンネームに
user_id = user["screen_name"]
# クッキーを生成しuser_id を遷移先のページに渡す
print("Set-Cookie: user="+ user_id)
print("Content-Type: text/html; charset=UTF-8\n\n")

html = textwrap.dedent('''
 <!DOCTYPE html>
<html lang = "ja">
<head>
<title>Dresser</title>
</head>
    <body>
      {0}
    </body>
</html>
''').format(get(c, user)).strip()
print(html)
