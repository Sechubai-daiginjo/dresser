#!/usr/bin/env python3
#encoding:UTF-8
#def sign_up_with_twitter():
    #Twitterログイン認証の実装


#---------------------------------------------
# プログラム本体
#---------------------------------------------
import cgi
import cgitb
import textwrap
from http import cookies
import io,sys
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
C = cookies.SimpleCookie()

#cgitb.enable()
print("Content-Type: text/html; charset=UTF-8\n\n")

html ='''
<!DOCTYPE html><html lang = "ja">
<head>
<title>Dresser</title>
<script type="text/javascript" src="../check.js"></script>
</head>
  <body>
    <h1>Dresser</h1>
    <h2>Twitterから新規登録</h2>
    <!-- Twitterでログインするやつをかく -->
    <form
      action = "./register.py"
      method = "post"
      name = "myform"
      onsubmit = "return check();"
      >
    <h2>user id : <input type = "text" name = "user_id" id='name'></h2>
    <h2>pssword : <input type = "password" name = "password" minlength='8' id='pass'></h2>
    <p>
      <input type="radio" name="gender" value="men" checked="checked">Men
      <input type="radio" name="gender" value="women">Women
    </p>
    Zip Code<input type="text" name="zipcode" size="40" maxlength="8" id='zip'>
    <p><input type = "submit" value = "resister"></p>

  </body>
</html>
'''.format().strip()

print(html)
