# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import re

#抽取某本书的前100条短评内容并计算评分的平均值。
count=0
sum=0.0
while(count<100):
    try:
        r=requests.get('https://book.douban.com/subject/27124852/comments/')
    except Exception as err:
        print err
        break    
    soup=BeautifulSoup(r.text,'lxml')
    pattern=soup.find_all('p','comment-content')
    for item in pattern:
        count=count+1
        print count,item.string
    pattern_s=re.compile('<span class="user-stars allstar(.*?) rating"')
    p=re.findall(pattern_s, r.text)
    for star in p:
        sum+=int(star)
    #print sum
    if count==100:
        break
    
sum=sum/count
print '该书评分的平均值为：%d' %sum