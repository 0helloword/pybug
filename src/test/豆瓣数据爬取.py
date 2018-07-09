# -*-coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import os

#豆瓣新书速递，通过元素的属性值制定新书速递书名规则
# r=requests.get('https://book.douban.com/latest?icn=index-latestbook-all')
# pattern=re.compile('<div class="detail-frame">.*?\n.*?<h2>.*?\n.*?<a.*?>(.*?)<\/a>')#新书速递书名规则
# t=re.findall(pattern, r.text)
# 
# n=0
# for item in t:
#     print item
#     n=n+1
# print '豆瓣新书速递:共%d本'%n

#豆瓣小组福田租房发布信息
# r=requests.get("https://www.douban.com/group/futianzufang/")
# pattern_top=re.compile('<td class="title">.*?\n.*?<span.*?>.*?\n.*?<img.*?>.*?\n.*?<\/span>.*?\n.*?<a.*?>(.*?)<\/a>')
# t1=re.findall(pattern_top, r.text)
# pattern=re.compile('<td class="title">.*?\n.*?<a.*?>(.*?)<\/a>')
# t2=re.findall(pattern, r.text)
# n1=0
# n2=2
# for item1 in t1:
#     print item1
#     n1=n1+1
# print '福田最新置顶租房消息:共%d条'%n1
# print '\n'
# for item2 in t2:
#     print item2
#     n2=n2+1
# print '福田最新租房消息:共%d条'%n2

#或者直接用正则表达式找出链接中包含https://www.douban.com/group/topic/的所有链接，即发布的所有租房信息
# r=requests.get("https://www.douban.com/group/futianzufang/")
# # print r.text
#  
# soup=BeautifulSoup(r.text,'html.parser')
# print '获取链接中包含https://www.douban.com/group/topic/的所有链接，即发布的所有租房信息'
# links_node=soup.find_all('a',href=re.compile(r"https://www.douban.com/group/topic/"))
#  
# n=0
# #将爬取的信息导出到html文件中 
# res_data={}
# fout=open('output.html','w')  
# fout.write("<html>")
# fout.write("<body>")
# fout.write("<table>")
# for link in links_node:
#     print link.name,link['href'],link.get_text()
#     res_data['url']=link['href']
#     res_data['content']=link.get_text()  
#     fout.write("<tr>")
#     fout.write("<td>%s</td>"% res_data['url'])
#     fout.write("<td>%s</td>"% res_data['content'].encode('utf-8'))
#     fout.write("</tr>")
#     n+=1
# print '共发布了%d条租房信息'%n            
# fout.write("</table>")
# fout.write("</body>")
# fout.write("</html>")
     
#将租房信息导出到一个txt文件中
url='https://www.douban.com/group/futianzufang/'
keyword=u'豆瓣'
dirpath=keyword+u'租房信息'
 
if not os.path.exists(dirpath):
    os.mkdir(dirpath)
filename='1.txt'
filePath = dirpath + os.sep + filename
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
titles=soup.find_all('a',href=re.compile('https://www.douban.com/group/topic/'))

with open(filePath,'w')as fp:
    for title in titles:
        fp.write(title['href'])  
        fp.write(title.get_text())
        fp.write('\n')
print 'END'





   


   
        
  
 


