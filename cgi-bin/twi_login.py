#!/usr/bin/env python3
#encoding:UTF-8
# # login.pyベースの登録フォーム(Twitterの認証からコールバック)
def get(c, user):
    user_id = user["screen_name"]
    print('<meta http-equiv="refresh" content="0.01;URL=./index.py">')
    str = textwrap.dedent('''
    <div class="top-space-40 col-md-12">
        <h1>Authentication succeeded</h1>
    </div>
    <div class="col-md-12">
        <p>You can enjoy our APP! </p>
    </div>
    <div class="col-md-12">
        <p><a href='./index.py'>Back to index page</a></p>
    </div>
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
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">

<title>Dresser</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season" />
<meta name="keywords" content="dresser, fashion, coodinate, recommend, search, summer, tops, pants, onepiece, outwear" />
<meta name="author" content="Sechubai" />

<meta property="og:title" content="dresser"/>
<meta property="og:image" content="../images/dresser.jpg"/>
<meta property="og:site_name" content="dresser"/>
<meta property="og:description" content="Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season"/>

<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/animate.css">
<link rel="stylesheet" href="../css/bootstrap.css">
<link rel="stylesheet" href="../css/icomoon.css">
<link rel="stylesheet" href="../css/test.css">
</head>

<body>
<div id="fh5co-wrap">
    <div class="large-div">
  	    <header id="fh5co-header">
		    <div class="container">
			    <div class="row">
				    <div class="col-md-4">
                        <h1 class="logo"><a href='./index.py'>Dresser</a></h1>
				    </div>
			    </div>
            </div>
	    </header>

        <div class="fh5co-section">
		    <div class="container">
			    <div class="row">
                    <div class="middle-div col-md-12">
				        <div class="row">
                            <div class="col-md-8 col-md-push-4">
                                <div class="row">
                                    {0}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<footer id="fh5co-footer">
    <div class="container">
		<div class="row">
            <div class="col-md-4">
				<h3>About Our App</h3>
				<p class="footer-font">Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season</p>
			</div>
        </div>
	</div>
</footer>

</body>
</html>
''').format(get(c, user)).strip()
print(html)
