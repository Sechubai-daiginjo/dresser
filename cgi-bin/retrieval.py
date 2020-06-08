#!/usr/bin/env python3
#encoding:UTF-8

def create_form(c, user):
    c.execute("SELECT gender FROM users WHERE userid = '{}' ;".format(user))
    for row in c:
        gender = row[0]
    if gender == 'men':
        str = textwrap.dedent('''
        <form action="./retrieval.py" method="GET">
            <select name="type">
            <option value="tshirt-cutsew">tshirt-cutsew</option>
            <option value="shirt-blouse">shirt-blouse</option>
            <option value="polo-shirt">polo-shirt</option>
            <option value="denim-pants">denim-pants</option>
            <option value="slacks">slacks</option>
            <option value="pants">pants</option>
            <option value="no-collar-jacket">no-collar-jacket</option>
            <option value="tailored-jacket">tailored-jacket</option>
            <option value="jacket">jacket</option>
            <option value="nylon-jacket">nylon-jacket</option>
            <option value="other-outer">other-outer</option>
            </select>
            <input type="submit" value="Let's Look Popular Clothes">
        </form>
        ''')

    elif gender == 'women':
        str = textwrap.dedent('''
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

def get_clothes(c):
    form = cgi.FieldStorage()
    type = form['type'].value
    str = textwrap.dedent('''
    <table border="1">
    <tr>
     <th>Looks</th>
     <th>Name</th>
     <th>Price</th>
    </tr>
    ''')
    c.execute("SELECT gender FROM users WHERE userid = '{}' ;".format(user))
    for row in c:
        gender = row[0]

    if gender == 'men':
        c.execute("SELECT * FROM men_ranking WHERE GoodsTypePath = '{}' order by RANDOM() limit 5;".format(type))
        for row in c:
            str += textwrap.dedent('''
            <tr>
             <td><img src={row1} /></td>
             <td>{row2}</td>
             <td>{row3}</td>
            <tr>
            ''').format(row1=row[-1], row2=row[0], row3=row[3])

    elif gender == 'women':
        c.execute("SELECT * FROM women_ranking WHERE GoodsTypePath = '{}' order by RANDOM() limit 5;".format(type))
        for row in c:
            str += textwrap.dedent('''
            <tr>
             <td><img src={row1} /></td>
             <td>{row2}</td>
             <td>{row3}</td>
            <tr>
            ''').format(row1=row[-1], row2=row[0], row3=row[3])
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
    <h2>Let's Look Popular Clothes</h2>
    {form}
    {image}
    <br>
    <a href='./index.py'>Back to Index Page</a>
  </body>
</html>
'''.format(form=create_form(c, user), image=get_clothes(c)).strip()

print(html)
