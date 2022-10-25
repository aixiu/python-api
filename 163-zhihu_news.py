# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/24 11:11:15

# 360新闰和知乎新闻整合

from bs4 import BeautifulSoup
import requests
import time


def get_zhihu_days(index):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
    }
    base_url = f"https://www.zhihu.com/api/v4/columns/c_1261258401923026944/items?limit=1&offset={index}"
    data = requests.get(base_url, headers=headers).json()
    html = data['data'][0]['content']
    soup = BeautifulSoup(html, 'lxml')
    day_news = soup.find_all('p')
    print(day_news)
    final_list = []
    news_list = []
    for i in day_news:
        i = i.text
        i.replace(u'\u200b', '')
        if i != '':
            final_list.append(i)
            if '、' in i:
                # new_str = '、'.join(i.split('、')[1:])
                new_str = i.split('、', 1)[1].replace(u'\u200b', '')  # 字符串切割1次，取第二个，并去除不可见字符\u200b
                news_list.append(new_str)
    final_list[0], final_list[1] = final_list[1], final_list[0]
    return final_list, news_list


def get_163_days(index):
    list_url = 'https://www.163.com/dy/media/T1603594732083.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",
        "realIP": "218.109.147.57"
    }

    data = requests.get(list_url, headers=headers)
    # print(data.url)
    soup = BeautifulSoup(data.text, 'lxml')
    days_list = soup.find_all('a', attrs={"class": "title"})
    new_url = days_list[index]['href']
    new_data = requests.get(new_url, headers=headers)
    soup = BeautifulSoup(new_data.text, 'lxml')
    day_news = soup.find('div', attrs={"class": "post_body"})
    list_all = str(day_news).split('<br/>')
    final_list = []
    news_list = []
    for i in list_all:        
        if "<" not in i and ">" not in i and i != '':
            if '、' in i and "微语" not in i:
                # new_str = '、'.join(i.split('、')[1:])  # 如果列表中内容中有、号，则需要join将字符串用、号重新连起来
                new_str = i.split('、', 1)[1].replace(u'\u200b', '') # 字符串切割1次，取第二个，并去除不可见字符\u200b
                news_list.append(new_str)            
            final_list.append(i.replace(u'\u200b', ''))

    return final_list, news_list



def main(index, origin):
    if origin == 'zhihu':
        try:
            data, news_list = get_zhihu_days(index)
            suc = True
        except Exception as e:
            data = [str(e)]*18
            suc = False
            news_list = 'zhihu'
    else:
        try:
            data, news_list = get_163_days(index)
            suc = True
        except Exception as e:
            data = [str(e)]*18
            suc = False
            news_list = '163'
    return {
        'suc': suc,
        'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        'data': {
            'title': data[0],
            'date': data[1],
            'news': news_list,
            'weiyu': data[-1]
        },
        'all_data': data
    }

if __name__ == '__main__':
    index = int(input('输入页数：'))
    origin = input('可输入 zhihu 或空：')
    data = main(index=index, origin=origin)
    # print(type(data))
    # print(data['data'])
    # print(data['all_data'])
    
    # print(data)
    # print(data['data']['title'])
    # print()
    # print(data['data']['date'])
    # print()
    
    # for index, i in enumerate(data['data']['news'], 1):
    #     print(f'{index}、{i}')
        
    print()
    for i in data['all_data']:        
        print(i)






