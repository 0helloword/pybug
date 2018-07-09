# -*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup# BeautifulSoup是模块用于接收一个HTML或XML字符串,然后将其进行格式化,之后便可以使用他提供的方法进行快速查找指定元素
import re


#获取豆瓣图书某一页的短评
r=requests.get('https://book.douban.com/subject/27124852/comments/')
soup=BeautifulSoup(r.text,'lxml')   #如果lxml报错，则表示没有安装lxml，pip install lxml即可   使用lxml解析
pattern=soup.find_all('p','comment-content')#获取p标签class属性为comment-content的字符集

for item in pattern:
    print item.string   #依次打印解析后的图书短评

#获取总评分
pattern_s=re.compile('<span class="user-stars allstar(.*?) rating"')#使用正则表达式将评分设置为.*?
p=re.findall(pattern_s, r.text)
sum=0.0
i=0
for star in p:
    sum+=int(star)
    i=i+1
print '该书总分为%d'%sum
print '该书平均评分为%d'%(sum/i)