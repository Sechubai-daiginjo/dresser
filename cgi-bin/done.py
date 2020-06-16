#!/usr/bin/env python3
#encoding:UTF-8

def get_users_clothes(form, user, c):
    user_id = user
    TypeCategory = []
    for row in form.value:
        if row.value not in TypeCategory:
            TypeCategory.append(row.value)
    TypeCategory = ','.join(TypeCategory)
    c.execute('INSERT INTO users_clothes VALUES (?,?)', (user_id, TypeCategory) )
    # データベースに変更加えたらコミットしないといけないらしい
    conn.commit()

#---------------------------------------------
# プログラム本体
#---------------------------------------------
import cgi
import cgitb
import sqlite3
import textwrap
import json
import sys
import requests
import re
from http import cookies
import os
import hashlib
import io,sys
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
form = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE",""))

#user_id = form['user_id'].value
user = cookie['user'].value
cgitb.enable()
#ローカル
conn = sqlite3.connect('./clothes/dresser.db')
#本番環境
#conn = sqlite3.connect('../clothes/dresser.db')
c = conn.cursor()
# クッキーを生成しuser_id を遷移先のページに渡す
print("Set-Cookie: user="+ user)
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
                        <h1 class="logo">Dresser</h1>
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
				                    <div class="top-space-40 col-md-12">
                                        <h1>Update Completed!</h1>
                                    </div>
                                    <div class="col-md-12">
                                        <p>Your account was created! </p>
                                    </div>
                                    <div class="col-md-12">
                                        <p>You can enjoy our APP! </p>
                                    </div>
                                    <div class="col-md-12">
                                        <p><a href='./index.py'>Back to Index Page</a></p>
                                    </div>
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
''').strip()
print(html)
get_users_clothes(form, user, c)
