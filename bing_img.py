# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/24 18:26:38

import requests
import json

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=20)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Something Wrong!'
    
    
url = 'https://raw.onmicrosoft.cn/Bing-Wallpaper-Action/main/data/zh-CN_all.json'  
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
        }
respons = requests.get(url=url, headers=headers).json()
img_data_dic = {}
img_data = json.dumps(respons, indent=3, ensure_ascii=False)
print(type(img_data))
print(img_data['LastUpdate'])

# aa = {
#     "LastUpdate": img_data['LastUpdate'],
#     "Total": img_data['Total'],
#     "Language": img_data['Language'],
#     "message": img_data['message'],
#     "status": img_data['status'],
#     "success": img_data['success'],
#     "data": [{
#         "startdate": img_data['data']['startdate'],
#         "fullstartdate": img_data['data']['fullstartdate'],
#         "enddate": img_data['data']['enddate'],
#         "url": f"https://cn.bing.com{img_data['data']['startdate']}",
#         "urlbase": img_data['data']['startdate'],
#         "copyright": img_data['data']['startdate'],
#         "copyrightlink": img_data['data']['startdate'],
#         "title": img_data['data']['startdate'],
#         "quiz": img_data['data']['startdate'],        
#         "hsh": img_data['data']['startdate'],
#     }],
# }
# print(aa)
