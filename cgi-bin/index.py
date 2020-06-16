#!/usr/bin/env python3
#encoding:UTF-8

def check_cookie(cookie):
    str = ''
    if 'user' in cookie:
        str += '''
		<div class="row">
            <div class="col-md-12">
                <h2 style="color:white">Welcome {0}!</h2>
            </div>
            <div class="col-md-5 col-md-push-1">
                <a href='./recommender.py'>
                    <button type="button" class="btn btn-primary btn-lg">Today's Coordination</button>
                </a>
                
            </div>
            <div class="col-md-3 col-md-push-2">
                <p><a href='./logout.py'>Sign Out</a></p>
            </div>
        </div>
        '''.format(cookie['user'].value)
    else:
        str += '''
		<div class="row">
            <div class="col-md-3 col-md-push-3">
                <p><a href='./login_form.py'>Sign In!</a></p>
            </div>
            <div class="col-md-3 col-md-push-3">
                <p><a href='./create_account.py'>Sign Up!</a></p>
            </div>
        </div>
        '''
    return str

def retrieve_clothes(c, cookie):
    str = ''
    if 'user' in cookie:
        str += '<div class="row"><div class="white top-space-20 col-md-12"><h2>Check Clothes Type and Get Summer Clothes Data!</h2></div></div>'
        c.execute("SELECT gender FROM users WHERE userid = '{}' ;".format(user))
        for row in c:
            gender = row[0]
        if gender == 'men':
            str += textwrap.dedent('''
            <form action="./retrieval.py" method="GET">
                <div class="row">
                    <div class="col-md-2 col-md-push-3">
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
                    </div>
                    <div class="col-md-2 col-md-push-4">
                        <input type="submit" value="Let's Look Popular Clothes" class="btn btn-primary">
                    </div>
                </div>
            </form>
            ''')

        elif gender == 'women':
            str += textwrap.dedent('''
            <form action="./retrieval.py" method="GET">
                <div class="row">
                    <div class="col-md-2 col-md-push-3">
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
                    </div>
                    <div class="col-md-2 col-md-push-4">
                        <input type="submit" value="Let's Look Popular Clothes" class="btn btn-primary">
                    </div>
                </div>
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
#conn = sqlite3.connect('./clothes/dresser.db')
#本番環境
conn = sqlite3.connect('../clothes/dresser.db')
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
  	<header id="fh5co-header">
		<div class="container">
			<div class="row">
				<div class="col-md-4">
                    <h1 class="logo">Dresser</h1>
				</div>
			</div>
        </div>
	</header>

	<div class="fh5co-hero" style="background-image: url(../images/dresser.jpg);" data-stellar-background-ratio="0.5">
		<div class="overlay"></div>
			<div class="container">
				<div class="row">
					<div class="col-md-8 col-md-offset-2 col-sm-12 col-sm-offset-0 col-xs-12 col-xs-offset-0 text-center fh5co-table">
						<div class="fh5co-intro fh5co-table-cell">
                                {get}
                                {retrieval}
                            <h1>About Our App</h1>
                            <p>Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season</p>
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
            <div class="col-md-4">
				<h3>Pulms in Snow</h3>
				<p class="footer-font">
                <a href='https://github.com/Sechubai-daiginjo/dresser'>
                <img src='../images/37318.png'　width="80" height="100">
                Source Code </a><br>
                Shingo Watanabe (Owner, Backend)<br>
                Tomoya Iwamoto (Member, Frontend)<br>
                Sho Shimamura (Member, Backend)<br>
                </p>
			</div>
        </div>
	</div>
</footer>

</body>
</html>
'''.format(get = check_cookie(cookie), retrieval = retrieve_clothes(c, cookie)).strip()

print(html)
print(cookie)
#print('cookie type =', cookie.value)
