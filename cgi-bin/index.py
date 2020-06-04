#!/usr/bin/env python3
#encoding:UTF-8

def check_cookie(cookie):
    if 'user' in cookie:
        str = '''
        <h2>Welcome {0}!</h2>
        <a href>マイページへ</a>
        <a href='./recommender.py'>Today's Coordination</a>
        '''.format(cookie['user'].value)
    else:
        str = '''
        <a href='./login_form.py'>Sign In!</a>
        <a href='./create_account.py'>Sign Up!</a>
        '''
    return str



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
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE",""))

cgitb.enable()
# クッキーが生成されていたらuserとして遷移先のページでもクッキーを渡し続ける処理
if 'user' in cookie:
    user = cookie['user'].value
    print("Set-Cookie: user="+ user)
print("Content-Type: text/html; charset=UTF-8\n\n")

html = '''
<!DOCTYPE html>
<html lang = "ja">
<head>
<title>Dresser</title>
</head>
  <body>
    <h1>Dresser</h1>
    {get}
    <h2>About Our App</h2>
    <p>Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season</p>
  </body>
</html>
'''.format(get = check_cookie(cookie)).strip()

print(html)
#print(cookie)
#print('cookie type =', cookie.value)
