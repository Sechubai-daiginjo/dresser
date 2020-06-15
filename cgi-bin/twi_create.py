#!/usr/bin/env python3
#encoding:UTF-8
# create_account.pyベースの登録フォーム(Twitterの認証からコールバック)

#---------------------------------------------
# プログラム本体
#---------------------------------------------
import cgi
import cgitb
import textwrap
from http import cookies
import io,sys
import json
import os
import requests
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
C = cookies.SimpleCookie()

# accesstokenを取得
tokens,user = {},{}
oauth = os.environ.get("QUERY_STRING").split("&")
for s in oauth:
    if s.split("=")[0] == "oauth_token":
        tokens["oauth_token"] = s.split("=")[1]
    elif s.split("=")[0] == "oauth_verifier":
        tokens["oauth_verifier"] = s.split("=")[1]

request = "https://api.twitter.com/oauth/access_token?oauth_token={}&oauth_verifier={}".format(tokens["oauth_token"],tokens["oauth_verifier"])
response = requests.get(request).text.split("&")
for s in response:
    if s.split("=")[0] == "oauth_token":
        user["oauth_token"] = s.split("=")[1]
    elif s.split("=")[0] == "oauth_token_secret":
        user["oauth_token_secret"] = s.split("=")[1]
    elif s.split("=")[0] == "user_id":
        user["user_id"] = s.split("=")[1]
    elif s.split("=")[0] == "screen_name":
        user["screen_name"] = s.split("=")[1]

cgitb.enable()
print("Content-Type: text/html; charset=UTF-8\n\n")

html ='''
<!DOCTYPE html><html lang = "ja">

<head>
<title>Dresser</title>
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/animate.css">
<link rel="stylesheet" href="../css/bootstrap.css">
<link rel="stylesheet" href="../css/icomoon.css">
<link rel="stylesheet" href="../css/test.css">
<script type="text/javascript" src="../check.js"></script>
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
                    <div class="login-div">
                        <div class="row">
					        <div class="col-md-12">
                                <div class="row">
							        <div class="col-md-12">

                                    </div>
                                </div>
                            </div>

                            <!-- Twitterでログインするやつをかく -->

                            <form
                              action = "./register.py"
                              method = "post"
                              name = "myform"
                              onsubmit = "return check();"
                            >

					        <div class="col-md-6 col-md-push-3">
                                <h2>User ID</h2>
                                <input type = "text" class="form-control" name = "user_id" id='name' placeholder="User ID" value={} readonly>
                            </div>
                            <div class="col-md-12">
                            </div>
  				                <div class="col-md-6 col-md-push-3">
                                <h2>Password</h2>
                                <input type = "password" class="form-control" name = "password" minlength='8' id='pass' placeholder="Password">
                            </div>
                            <div class="col-md-12">
                            </div>    
					        <div class="col-md-6 col-md-push-3">
                                <h2>Gender</h2>
                                <input type="radio" name="gender" value="men" checked="checked">Men
                                <input type="radio" name="gender" value="women">Women
                            </div>
                            <div class="col-md-12">
                            </div>
					        <div class="col-md-6 col-md-push-3">
                                <h2>Zip Code</h2>
                                <input type="text" class="form-control" name="zipcode" size="40" maxlength="8" id='zip' placeholder="Zip Code">
                            </div>
                            <div class="col-md-12">
                            </br>
                            </div>
					        <div class="col-md-6 col-md-push-3">
                                <p><input type = "submit" value = "resister" class="btn btn-primary"></p>
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
				<h3>About Us</h3>
				<p class="footer-font">Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season</p>
			</div>
        </div>
	</div>
</footer>

</body>
</html>
'''.format(user["screen_name"]).strip()

print(html)
