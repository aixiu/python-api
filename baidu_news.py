# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/26 10:00:24

# 百度热搜

from bs4 import BeautifulSoup
import requests
import time

def get_baidu_days(tab_str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
    }
    base_url = f"https://top.baidu.com/board?tab={tab_str}"
    data = requests.get(url=base_url, headers=headers, timeout=20)
    try:
        data.raise_for_status()
        data.encoding = data.apparent_encoding
        soup = BeautifulSoup(data.text, 'lxml')
        title_list = []
        hot_index = []

        title_list_text =  soup.find_all('div', attrs={'class': 'c-single-text-ellipsis'})
        hot_index_text = soup.find_all('div', attrs={'class': 'hot-index_1Bl1a'})
        for title in title_list_text:
            title_list.append(title.get_text().strip())
        for hot in hot_index_text:
            hot_index.append(hot.get_text().strip())
        return title_list, hot_index
        
    except:
        return 'Something Wrong!'
    
def main(tab_str):
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    data, hot_index = get_baidu_days(tab_str)
    print(f'{"  当前指数  ":#^50}')
    print(f'{now_time:^54}')
    print()
    for index, i in enumerate(data):        
        print(f'{index + 1}、{i}  ==>  热搜指数：{hot_index[index]}')
    print()
    print(f'{"  End  ":#^50}')
    
if __name__ == '__main__':
    print('请输入数字版块编码：1 = 热搜，2 = 小说，3 = 电影，4 = 电视剧，5 = 汽车，6 = 游戏')
    print()
    try:
        in_tab_str = int(input('请输入查看的版块(编码)：'))

        if in_tab_str == 1:
            tab_str = 'realtime'
        if in_tab_str == 2:
            tab_str = 'novel'
        if in_tab_str == 3:
            tab_str = 'movie'
        if in_tab_str == 4:
            tab_str = 'teleplay'
        if in_tab_str == 5:
            tab_str = 'car'
        if in_tab_str == 6:
            tab_str = 'game'        
            
        main(tab_str=tab_str)
    except Exception as e:
        print(f'请输入数字！！  错误信息：{e}')
    

        
    
    
