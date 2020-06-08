#!/usr/bin/env python3
#encoding:UTF-8

#---------------------------------------------
# プログラム本体
#---------------------------------------------
import cgi
import cgitb
import textwrap
from http import cookies
import os
import io,sys
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# クッキーの取得
#cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
#cookie

#クッキーの有効期限を設定
print("Set-Cookie: Max-Age = 0.00001")
print("Content-Type: text/html; charset=UTF-8\n\n")

html = '''
<!DOCTYPE html>
<html lang = "ja">
<head>
<title>Dresser</title>
</head>
  <body>
    <h1>Dresser</h1>
    Logged Out!
    <a href='./index.py'>Back to Index Page</a>
    <h2>About Our App</h2>
    <p>Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season</p>
  </body>
</html>
'''
#print(user)
print(html)
