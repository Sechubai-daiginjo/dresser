#!/usr/bin/env python3
#encoding:UTF-8

def get_weather_info(c, user):
    API_KEY = '6b5200aaaad2c25aaf160e5637959924'
    #zipcode = '305-0821'
    c.execute("SELECT zipcode FROM users WHERE userid = '{}' ;".format(user))
    for row in c:
        zipcode = row[0]
    #api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
    #url = api.format(city = city_name, key = API_KEY)
    api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={zip}&APPID={key}"
    url = api.format(zip = zipcode, key = API_KEY)
    response = requests.get(url)
    data = response.json()
    jsonText = json.dumps(data, indent=4)
    return response

def get_jsonText(response):
    data = response.json()
    data = json.loads(response.text)
    #print(data)
    weather = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    weather_data = [weather, temp, pressure, humidity, temp_min, temp_max]

    return weather_data

def get_clothes(c, weather_data, user):
    c.execute("SELECT gender FROM users WHERE userid = '{}' ;".format(user))
    for row in c:
        gender = row[0]
    weather = weather_data[0]
    temp = weather_data[1]
    temp_min = weather_data[4]
    temp_max = weather_data[5]
    str = ""
    str += textwrap.dedent('''
        <div class="fh5co-section">
			<div class="container">

				<div class="row">
					<div class="col-md-4">
                      <h2>
                        Weather
                        <p>{weather}</p>
                      </h2>
					</div>
                    <div class="col-md-4">
                      <h2>
                        Highest Temperature
                        <p>{temp_max}</p>
                      </h2>
                    </div>
                    <div class="col-md-4">
                      <h2>
                        Lowest Temperature
                        <p>{temp_min}</p>
                      </h2>
                    </div>
                </div>

			</div>
		</div>
        
        <div class="fh5co-section">
			<div class="container">
				<div class="row">
    ''').format(weather=weather, temp_max=temp_max, temp_min=temp_min)

    c.execute("SELECT GoodsTypePath FROM users_clothes WHERE userid = '{}' ;".format(user))
    for rows in c:
        rows = rows[0].split(",")
        sc = random.sample(rows, len(rows))

    count = []
    for row in sc:
        if gender == 'men':
            if (row == ' tshirt-cutsew' or row == ' shirt-blouse' or row == ' polo-shirt' or row == ' parka') and 'tops' not in count:
                # pythonにはswitch文がないので冗長になるけどif文で全部書きます
                if int(temp_max) >= 23 and row == ' tshirt-cutsew' and 'tops' not in count:
                    c.execute("SELECT DefaultImagePath FROM men_ranking WHERE GoodsTypePath = 'tshirt-cutsew' order by RANDOM() limit 1;")
                    count.append('tops')
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>   
                        ''').format(src[0])

                elif int(temp_max) >= 23 and row == ' shirt-blouse' and 'tops' not in count:
                    c.execute("SELECT DefaultImagePath FROM men_ranking WHERE GoodsTypePath = 'shirt-blouse' order by RANDOM() limit 1;")
                    count.append('tops')
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                             <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>      
                        ''').format(src[0])

                elif int(temp_max) >= 23 and row == ' polo-shirt' and 'tops' not in count:
                    c.execute("SELECT DefaultImagePath FROM men_ranking WHERE GoodsTypePath = 'polo-shirt' order by RANDOM() limit 1;")
                    count.append('tops')
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>  
                        ''').format(src[0])

                elif int(temp_max) >= 17 and temp_max < 23 and row == ' tshirt-cutsew' and 'tops' not in count:
                    c.execute("SELECT DefaultImagePath FROM men_ranking WHERE TypeCategoryPath = 'jacket-outerwear' order by RANDOM() limit 1;")
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>
                        ''').format(src[0])
                    c.execute("SELECT DefaultImagePath FROM men_ranking WHERE TypeCategoryPath = 'tshirt-cutsew' order by RANDOM() limit 1;")
                    count.append('tops')
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>
                        ''').format(src[0])

                elif int(temp_max) < 17 and row == ' parka' and 'tops' not in count:
                    c.execute("SELECT DefaultImagePath FROM men_ranking WHERE TypeCategoryPath = 'tshirt-cutsew' order by RANDOM() limit 1;")
                    count.append('tops')
                    for src in c:
                        str = textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>
                        ''').format(src[0])


            elif (row == ' denim-pants' or row == ' slacks') and 'pants' not in count:
                row = row.lstrip()
                c.execute("SELECT DefaultImagePath FROM men_ranking WHERE GoodsTypePath = '{}' order by RANDOM() limit 1;".format(row))
                for src in c:
                    str += textwrap.dedent('''
					<div class="col-md-6">
                        <h1>
                            <p>Pants</p>
                        </h1>
                        <h2>
                            <img src={} />
                        </h2>
                    </div>  
                    ''').format(src[0])
                count.append('pants')

        elif gender == 'women':

            if (row == ' tshirt-cutsew' or row == ' shirt-blouse' or row == ' knit-sweater' or row == ' parka') and 'tops' not in count:
                # pythonにはswitch文がないので冗長になるけどif文で全部書きます
                if int(temp_max) >= 23 and row == ' tshirt-cutsew' and 'tops' not in count :
                    c.execute("SELECT DefaultImagePath FROM women_ranking WHERE GoodsTypePath = 'tshirt-cutsew' order by RANDOM() limit 1;")
                    count.append('tops')
                    count.append('onepiece')
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>  
                        ''').format(src[0])

                elif int(temp_max) >= 23 and row == ' shirt-blouse' and 'tops' not in count:
                    c.execute("SELECT DefaultImagePath FROM women_ranking WHERE GoodsTypePath = 'shirt-blouse' order by RANDOM() limit 1;")
                    count.append('tops')
                    count.append('onepiece')
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>
                        ''').format(src[0])

                elif int(temp_max) >= 23 and row == ' knit-sweater' and 'tops' not in count:
                    c.execute("SELECT DefaultImagePath FROM women_ranking WHERE GoodsTypePath = 'knit-sweater' order by RANDOM() limit 1;")
                    count.append('tops')
                    count.append('onepiece')
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>
                        ''').format(src[0])

                elif int(temp_max) >= 17 and temp_max < 23 and row == ' tshirt-cutsew' and 'tops' not in count:
                    c.execute("SELECT DefaultImagePath FROM women_ranking WHERE TypeCategoryPath = 'jacket-outerwear' order by RANDOM() limit 1;")
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Outerwear</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>
                        ''').format(src[0])
                    c.execute("SELECT DefaultImagePath FROM women_ranking WHERE TypeCategoryPath = 'tshirt-cutsew' order by RANDOM() limit 1;")
                    count.append('tops')
                    count.append('onepiece')
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div> 
                        ''').format(src[0])

                elif int(temp_max) < 17 and row == ' parka' and 'tops' not in count:
                    c.execute("SELECT DefaultImagePath FROM women_ranking WHERE TypeCategoryPath = 'tshirt-cutsew' order by RANDOM() limit 1;")
                    count.append('tops')
                    count.append('onepiece')
                    for src in c:
                        str += textwrap.dedent('''
					    <div class="col-md-6">
                            <h1>
                                <p>Tops</p>
                            </h1>
                            <h2>
                                <img src={} />
                            </h2>
                        </div>
                        ''').format(src[0])
            elif (row == ' denim-pants' or row == ' pants' or row ==' skirt') and 'pants' not in count:
                row = row.lstrip()
                c.execute("SELECT DefaultImagePath FROM women_ranking WHERE GoodsTypePath = '{}' order by RANDOM() limit 1;".format(row))
                for src in c:
                    str += textwrap.dedent('''
					<div class="col-md-6">
                        <h1>
                            <p>Pants or Skirt</p>
                        </h1>
                        <h2>
                            <img src={} />
                        </h2>
                    </div>   
                    ''').format(src[0])
                count.append('pants')
                count.append('onepiece')

            elif (row == ' shirts-onepiece' or ' onepiece-dress') and 'onepiece' not in count:
                row = row.lstrip()
                c.execute("SELECT DefaultImagePath FROM women_ranking WHERE GoodsTypePath = '{}' order by RANDOM() limit 1;".format(row))
                for src in c:
                    str += textwrap.dedent('''
					<div class="col-md-6">
                        <h1>
                            <p>Onepiece</p>
                        </h1>
                        <h2>
                            <img src={} />
                        </h2>
                    </div>
                    ''').format(src[0])
                count.append('onepiece')
                count.append('tops')
                count.append('pants')

    return str


def do_func():
    response = get_weather_info(c, user)
    #jsonText = get_weather_info()[1]
    weather_data = get_jsonText(response)
    #print(weather_data)
    get = get_clothes(c, weather_data, user)
    str = textwrap.dedent('''
    <div class="fh5co-section">
		<div class="container">
            <div class="row">
				<div class="col-md-12">
                    <h1>Today's Coordination for You!</h1>
                </div>
            </div>
        </div>
    </div>
    {get}
    ''').format(get=get)
    return str

#---------------------------------------------
# プログラム本体
#---------------------------------------------
import cgi
import cgitb
import sqlite3
import textwrap
#import Cookie
import requests
import json
from http import cookies
import os
import io,sys
import random
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# クッキーの取得
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE",""))

cgitb.enable()
# クッキーが生成されていたらuserとして遷移先のページでもクッキーを渡し続ける処理
if 'user' in cookie:
    user = cookie['user'].value
    print("Set-Cookie: user="+ user)
#ローカル
conn = sqlite3.connect('./clothes/dresser.db')
#本番環境
#conn = sqlite3.connect('../clothes/dresser.db')
c = conn.cursor()


#html本体
print("Content-Type: text/html; charset=UTF-8\n\n")
do_func()
html = textwrap.dedent('''
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
  <div id="fh5co-wrap" style="background-color: #EEEEEE;">
  	<header id="fh5co-header">
			<div class="container">
				<nav class="fh5co-main-nav">
          <h1>Dresser</h1>
        </nav>
			</div>
		</header>

	<div class="fh5co-section">
		<div class="container">
        <div class="row">
        <div style="width:1200px;margin-left:auto;margin-right:auto;text-align:center;background-color: #FFFFFF;">

    {}

                    </div>
                </div>
            </div>

        </div>
        </div>
      </div>
    </div>

    <a href='./index.py'>Back to Index Page</a>
  </body>
</html>
''').format(do_func())
print(html)
