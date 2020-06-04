#!/usr/bin/env python3
#encoding:UTF-8
def display_user_data():
    str = ""
    str += textwrap.dedent('''

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
      
    </body>
</html>
''').format(display_user_data()).strip()
print(html)
