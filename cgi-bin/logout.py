#!/usr/bin/env python3
#encoding:UTF-8

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
#cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
#cookie

#クッキーの有効期限を設定
print("Set-Cookie: Max-Age = 0.00001")
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
<link rel="stylesheet" href="../css/test.css">
</head>

<body>
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
                    <div class="col-md-3 col-md-push-3">
                        <h1>
                            Logged Out!
                        </h1>
                    </div>
                    <div class="col-md-4 col-md-push-3">
                        <h2>
                        <a href='./index.py'>Back to Index Page</a>
                        </h2>
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
'''
#print(user)
print(html)
