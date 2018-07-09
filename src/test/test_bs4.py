#coding:utf-8
# BeautifulSoup网页解析器
from bs4 import BeautifulSoup
import re

html_doc="""
<html><head><title>the dormouse's story</title></head>
<body>
<p class="title"><b>the dormouse's story中文字符测试</b></p>
<p class="story">once upon a time there were three little sisters;and their name</p>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/one" class="sister" id="link1">one</a>
<a href="http://example.com/elsie" class="sister" id="link1">ls</a>

"""

soup=BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
print '获取所有的连接'
links=soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()
    
print '获取elsie的连接'
links_node=soup.find('a',href='http://example.com/elsie')
print links_node.name,links_node['href'],links_node.get_text()

print '正则匹配'
links_node=soup.find('a',href=re.compile(r"ls"))
print links_node.name,links_node['href'],links_node.get_text()

print '获取P段落内容'
p_node=soup.find('p',class_="title")   #class是关键字，需要加下横线
print p_node.name,p_node.get_text()

