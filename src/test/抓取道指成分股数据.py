# -*-coding:utf-8 -*-
# 在“http://money.cnn.com/data/dow30/”上抓取道指成分股数据并将30家公司的代码、公司名称和最近一次成交价放到一个列表中输出。


import requests
import re
import pandas


def retrieve_dji_list1():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    dji_list=[]
    for item in dji_list_in_text:
        dji_list.append([item[0],item[1],float(item[2])])
    return dji_list

def retrieve_dji_list2():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text

dji_list1 = retrieve_dji_list1()
print(dji_list1)
dj=pandas.DataFrame(dji_list1)#转换成dataframe格式
cols=['code','name','lasttrade']
dj.columns=cols
print dj
dji_list2 = retrieve_dji_list2()
print(dji_list2)