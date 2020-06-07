#!/usr/bin/env python3
#encoding:UTF-8
import cgi
import cgitb
import textwrap
import io,sys
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cgitb.enable()

print("Content-Type: text/html; charset=UTF-8\n\n")
html ='''
<!DOCTYPE html>
<html lang = "ja">
<head>
<title>Dresser</title>
<script type="text/javascript" src="../check.js"></script>
</head>
  <body>
    <h1>Dresser</h1>
    <h2>Twitterでログイン</h2>
    <!-- Twitterでログインするやつをかく -->
    <form
      action = "./login.py"
      method = "post"
      name = "myform"
      onsubmit = "return check2();"
      >
    <h2>user id : <input type = "text" name = "user_id" id='name'></h2>
    <h2>pssword : <input type = "password" name = "password" minlength='8' id='pass'></h2>
    <input type = "submit" value = "sign-in">

  </body>
</html>
'''.format().strip()

print(html)
