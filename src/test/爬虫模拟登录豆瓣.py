# -*-coding:utf-8 -*-
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import re


#模拟浏览器
chrome=webdriver.Chrome()
#打开网页
chrome.get('https://www.douban.com/')
chrome.maximize_window()
#输入登录账户密码


chrome.find_element_by_id('form_email').send_keys('15626513325')
chrome.find_element_by_name('form_password').send_keys('zzjdlrbrqsb')
chrome.find_element_by_class_name('bn-submit').click()

#爬取数据
time.sleep(5)
r=requests.get('https://www.douban.com/')
soup=BeautifulSoup(r.text,'html.parser')
links_node=soup.find_all('a',href=re.compile(r"https://www.douban.com/note/"))
 
 
for link in links_node:
    print link.get_text()






