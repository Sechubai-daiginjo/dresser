#!/usr/bin/env python3
#encoding:UTF-8
def get(c, form):
    user_id = form['user_id'].value
    password = form['password'].value
    c.execute("SELECT password FROM users WHERE userid = ?;", (user_id,))
    for row in c:
        # データベースの暗号化されたパスワードと、入力されたパスワードを暗号化したものを比較
        if row[0] == hashlib.sha512(password.encode()).hexdigest():
            #かなり無理矢理インデックスページにリダイレクトする
            print('<meta http-equiv="refresh" content="0.01;URL=./index.py">')

            str = textwrap.dedent('''
            <p>Authentication succeeded</p>
            <p>You can enjoy our APP! </p>
            <a href='./index.py'>Back to index page</a>
            ''')

        else:
            str = textwrap.dedent('''
            <p>Authentication failed</p>
            <a href='./login_form.py'>Back to sign up page</a>
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
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cgitb.enable()
#ローカル
conn = sqlite3.connect('./clothes/dresser.db')
#本番環境
#conn = sqlite3.connect('../clothes/dresser.db')
c = conn.cursor()
form = cgi.FieldStorage()
user_id = form['user_id'].value

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
''').format(get(c, form)).strip()
print(html)
