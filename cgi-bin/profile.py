#!/usr/bin/env python3
#encoding:UTF-8
def make_user_data():
    str = ""
    str += textwrap.dedent('''
        <p>
          <input type="radio" name="gender" value="men" checked="checked">Men
          <input type="radio" name="gender" value="women">Women
        </p>
        住所<input type="text" name="zipcode" size="40" maxlength="8">
    ''')

    return str


#---------------------------------------------
# プログラム本体
#---------------------------------------------
import cgi
import cgitb
import sqlite3
import textwrap
import json
import requests
import io,sys
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

cgitb.enable()
conn = sqlite3.connect('./clothes/dresser.db')
c = conn.cursor()

print("Content-Type: text/html; charset=UTF-8\n\n")
html = textwrap.dedent('''
 <!DOCTYPE html>
<html lang = "ja">
<head>
<title>Dresser</title>
</head>
    <body>
      <h1>input your data</h1>
      <form action="./done.py" method="post">
      {0}
      <input type="submit" value="Submit!">
      </form>
    </body>
</html>
''').format(make_user_data()).strip()
print(html)
