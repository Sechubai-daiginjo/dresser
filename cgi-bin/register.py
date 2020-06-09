#!/usr/bin/env python3
#encoding:UTF-8
def zipcode_data(form):
    zipcode = form['zipcode'].value
    RECEST_URL = "http://zipcloud.ibsnet.co.jp/api/search?zipcode={0}".format(zipcode)
    response = requests.get(RECEST_URL)
    json_result = response.text
    json_to_dic_result = json.loads(response.text)
    if json_to_dic_result["results"] != None:
        result_dic = json_to_dic_result["results"][0]
        # openweathermap を郵便番号で利用するにはハイフンが必要なのでその処理
        if '-' not in zipcode:
            formated_zipcode = str(zipcode)[0:3] + '-' + str(zipcode)[3:]
        else:
            formated_zipcode = zipcode
    # 間違った郵便番号の時の処理
    else:
        print("Your zipcode was incorrect")
        print("<a href='./create_account.py'>アカウント作成ページに戻る</a>")
        exit()
    #result_dic['address2'] = re.sub('[市|区].*', '', result_dic['address2'])
    #result_dic['address2'] += '市'
    #return result_dic['address2']
    return formated_zipcode

def register(form, c, formated_zipcode):
    user_id = form['user_id'].value
    password = form['password'].value
    password = hashlib.sha512(password.encode()).hexdigest()
    gender = form['gender'].value
    user_data = [(user_id, password, gender, formated_zipcode),]
    #c.execute("INSERT INTO users VALUES ({},{},{},{})".format(user_id, password, gender, formated_zipcode,))
    c.executemany('INSERT INTO users VALUES (?,?,?,?)',user_data )
    # データベースに変更加えたらコミットしないといけないらしい
    conn.commit()
    #print('INSERT INTO users VALUES (?,?,?,?)',user_data)
    #print('updated')

def get_basic_clothes(form, c):
    user_id = form['user_id'].value
    gender = form['gender'].value

    str = textwrap.dedent('''
    <form action="./done.py" method="post">
    ''')

    if gender == 'men':
        categories = [' tops', ' pants']
        for category in categories:
            c.execute("SELECT DefaultImagePath, GoodsTypePath FROM basic_men WHERE TypeCategoryPath = '{}' order by random() limit 5;".format(category))
            for row in c:
                str += textwrap.dedent('''
				<div class="col-md-6">                
                    <img src={} />
                    <h3><input type="checkbox" name="{}" value="{}" > I have like this one</h3>
                    <br></br>
                </div>  
                ''').format(row[0], row[1], row[1])


    elif gender == 'women':
        categories = [' tops', ' pants', ' skirt', ' onepiece']
        for category in categories:
            c.execute("SELECT DefaultImagePath, GoodsTypePath FROM basic_women WHERE TypeCategoryPath = '{}' order by random() limit 5;".format(category))
            for row in c:
                str += textwrap.dedent('''
				<div class="col-md-6">
                    <img src={} />
                    <h3><input type="checkbox" name="{}" value="{}" > I have like this one</h3>
                    <br></br>
                </div>
                ''').format(row[0], row[1], row[1])

    else:
        print('Something Wrong ')
        exit()
    str += textwrap.dedent('''

	<div class="col-md-2 col-md-push-5">
        <h3><input type="submit" value="Register your clothes" class="btn btn-primary"></h3>
    </div>
        
    </form>
    ''')
    return str

def do_func(c, user_id):
    user_id = user_id
    formated_zipcode = zipcode_data(form)
    c.execute("SELECT userid FROM users WHERE userid = '{}' ;".format(user_id))
    #for row in c:
    #    if row != "()":
    #        print('すでに登録済みのユーザーです')
    #    else:
    register(form, c, formated_zipcode)

    str = textwrap.dedent('''
    {}

    ''').format(get_basic_clothes(form, c))
    return str


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
import hashlib
import io,sys
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
cookie = cookies.SimpleCookie()
user_id = form['user_id'].value
cgitb.enable()
#ローカル
conn = sqlite3.connect('./clothes/dresser.db')
#本番環境
#conn = sqlite3.connect('../clothes/dresser.db')
c = conn.cursor()
# クッキーを生成しuser_id を遷移先のページに渡す
print("Set-Cookie: user="+ user_id)
print("Content-Type: text/html; charset=UTF-8\n\n")

html = textwrap.dedent('''
<!DOCTYPE html>
<html lang = "ja">
<head>
<title>Dresser</title>
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/animate.css">
<link rel="stylesheet" href="../css/bootstrap.css">
<link rel="stylesheet" href="../css/icomoon.css">
<link rel="stylesheet" href="../css/test.css">
</head>

<body style="background-color: #ffefd5;">
<div id="fh5co-wrap">
    <div class="large-div">
  	    <header id="fh5co-header">
		    <div class="container">
			    <div class="row">
				    <div class="col-md-4">
                        <h1>Dresser</h1>
				    </div>
			    </div>
            </div>
	    </header>

        <div class="fh5co-section">
		    <div class="container">
			    <div class="row">
                    <div class="middle-div">
				        <div class="row">
				            <div class="col-md-12">
                                <h1>Update Completed!</h1>
                            </div>
                            <div class="col-md-12">               
                                <h2>Please register your clothes</h2>
                            </div>   
                            {0}
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
				        <h3>About Us</h3>
				        <p class="footer-font">Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season</p>
			      </div>
        </div>
	  </div>
</footer>

</body>
</html>
''').format(do_func(c, user_id)).strip()
print(html)
