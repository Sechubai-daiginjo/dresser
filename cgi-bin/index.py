#!/usr/bin/env python3
#encoding:UTF-8

def check_cookie(cookie):
    str = ''
    if 'user' in cookie:
        str += '''
        <h2>Welcome {0}!</h2>
        <a href='./recommender.py'>Today's Coordination</a>
        <a href='./logout.py'>Sign Out</a>
        '''.format(cookie['user'].value)
    else:
        str += '''
        <a href='./login_form.py'>Sign In!</a>
        <a href='./create_account.py'>Sign Up!</a>
        '''
    return str

def retrieve_clothes(c, cookie):
    str = ''
    if 'user' in cookie:
        str += '<p>Check Clothes Type and Get Summer Clothes Data!</p>'
        c.execute("SELECT gender FROM users WHERE userid = '{}' ;".format(user))
        for row in c:
            gender = row[0]
        if gender == 'men':
            str += textwrap.dedent('''
            <form action="./retrieval.py" method="GET">
                <select name="type">
                <option value="tshirt-cutsew">tshirt-cutsew</option>
                <option value="shirt-blouse">shirt-blouse</option>
                <option value="polo-shirt">polo-shirt</option>
                <option value="denim-pants">denim-pants</option>
                <option value="slacks">slacks</option>
                <option value="pants">pants</option>
                <option value="o-collar-jacket">o-collar-jacket</option>
                <option value="tailored-jacket">tailored-jacket</option>
                <option value="jacket">jacket</option>
                <option value="nylon-jacket">nylon-jacket</option>
                <option value="other-outer">other-outer</option>
                </select>
                <input type="submit" value="Let's Look Popular Clothes">
            </form>
            ''')

        elif gender == 'women':
            str += textwrap.dedent('''
            <form action="./retrieval.py" method="GET">
                <select name="type">
                <option value="tshirt-cutsew">tshirt-cutsew</option>
                <option value="shirt-blouse">shirt-blouse</option>
                <option value="knit-sweater">knit-sweater</option>
                <option value="camisole">camisole</option>
                <option value="denim-pants">denim-pants</option>
                <option value="slacks">slacks</option>
                <option value="pants">pants</option>
                <option value="skirt">skirt</option>
                <option value="no-collar-jacket">no-collar-jacket</option>
                <option value="tailored-jacket">tailored-jacket</option>
                <option value="jacket">jacket</option>
                <option value="nylon-jacket">nylon-jacket</option>
                <option value="other-outer">other-outer</option>
                </select>
                <input type="submit" value="Let's Look Popular Clothes">
            </form>
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
import os
import io,sys
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# クッキーの取得
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
#ローカル
conn = sqlite3.connect('./clothes/dresser.db')
#本番環境
#conn = sqlite3.connect('../clothes/dresser.db')
c = conn.cursor()
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
    {retrieval}
    <h2>About Our App</h2>
    <p>Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season</p>
  </body>
</html>
'''.format(get = check_cookie(cookie), retrieval = retrieve_clothes(c, cookie)).strip()

print(html)
#print(cookie)
#print('cookie type =', cookie.value)
