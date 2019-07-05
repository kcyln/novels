# coding: utf8

import requests
import re
import json

url = "https://book.qidian.com/info/1004608738"
response = requests.get(url)

pattern = re.compile(r'<a class="J-getJumpUrl" id="bookImg".*?><img src="(.*?)".*?<h1>.*?<em>(.*?)</em>.*?<a class="writer".*?>(.*?)</a> 著</span>.*?<p class="tag"><span class="blue">连载</span>(.*?)</p>.*?<p class="intro">(.*?)</p>', re.S)

item = re.findall(pattern, response.text)[0]
item = [i.replace("\r", "").replace(" ", "") for i in item]
i = {
    "image_url": "https:" + item[0],
    "name": item[1],
    "auth": item[2],
    "tags": item[3],
    "intro": item[4],
}
