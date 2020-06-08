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
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/animate.css">
<link rel="stylesheet" href="../css/bootstrap.css">
<link rel="stylesheet" href="../css/icomoon.css">
</head>

<body>
  <div id="fh5co-wrap">
  	<header id="fh5co-header">
			<div class="container">
				<nav class="fh5co-main-nav">
                  <h1>Dresser</h1>
				</nav>
			</div>
		</header>

		<div class="fh5co-hero" style="background-image: url(../images/hero_4.jpg);" data-stellar-background-ratio="0.5">
			<div class="overlay"></div>
			<div class="container">
				<div class="row">
					<div class="col-md-8 col-md-offset-2 col-sm-12 col-sm-offset-0 col-xs-12 col-xs-offset-0 text-center fh5co-table">
						<div class="fh5co-intro fh5co-table-cell">
              <h2>{get}</h2>
              <h1>About Our App</h1>
              <p>Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season</p>
						</div>
					</div>
				</div>
			</div>
		</div>

  </div>
</body>

</html>
'''.format(get = check_cookie(cookie)).strip()

print(html)
#print(cookie)
#print('cookie type =', cookie.value)
