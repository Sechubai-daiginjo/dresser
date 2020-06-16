#!/usr/bin/env python3
#encoding:UTF-8

def create_form(c, user):
    c.execute("SELECT gender FROM users WHERE userid = '{}' ;".format(user))
    for row in c:
        gender = row[0]
    if gender == 'men':
        str = textwrap.dedent('''
        <form action="./retrieval.py" method="GET">
            <div class="row">
                <div class="top-space-40 col-md-2 col-md-push-4">
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
                </div>
                <div class="top-space-40 col-md-2 col-md-push-4">            
                    <input type="submit" value="Let's Look Popular Clothes" class="btn btn-primary">
                </div>
            </div>
        </form>
        ''')

    elif gender == 'women':
        str = textwrap.dedent('''
        <form action="./retrieval.py" method="GET">
            <div class="row">
                <div class="top-space-40 col-md-2 col-md-push-4">
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
                <div class="top-space-40 col-md-2 col-md-push-4"> 
                    <input type="submit" value="Let's Look Popular Clothes" class="btn btn-primary">
                </div>
            </div>
        </form>
        ''')

    return str

def get_clothes(c):
    form = cgi.FieldStorage()
    type = form['type'].value
    str = textwrap.dedent('''
    
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
             <td><img src={row1} class="foto_size"></td>
             <td>{row2}</td>
             <td>{row3}</td>
            </tr>
            ''').format(row1=row[-1], row2=row[0], row3=row[3])

    elif gender == 'women':
        c.execute("SELECT * FROM women_ranking WHERE GoodsTypePath = '{}' order by RANDOM() limit 5;".format(type))
        for row in c:
            str += textwrap.dedent('''
            <tr>
             <td><img src={row1} class="foto_size"></td>
             <td>{row2}</td>
             <td>{row3}</td>
            </tr>
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
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">

<meta charset="utf-8">
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
                    <div class="middle-div">
				        <div class="row">
                            <div class="tyuou top-space-40 col-md-12">
                                <h1>Let's Look Popular Clothes</h1>
                            </div>
                            <div class="col-md-12">
                                {form}
                                </br>
                            </div>
                            <div class="col-md-12">
                                <table class="retrieval">
                                    {image}
                                </table>
                            </div>
                            <div class="tyuou top-space-50 col-md-12">
                                <p><a href='./index.py'>Back to Index Page</a></p>
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
'''.format(form=create_form(c, user), image=get_clothes(c)).strip()

print(html)
