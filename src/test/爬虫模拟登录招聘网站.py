# -*-coding:utf-8 -*-
# -*-encoding:utf-8 -*-

from selenium import webdriver
from scrapy.selector import Selector
import time
import os

def writeFile(dirPath, page):
    data = Selector(text = page).xpath("//td[@class='zwmc']/div/a")  
    titles = data.xpath('string(.)').extract()#获取招聘标题集
    print titles
    timeMarks = Selector(text = browser.page_source).xpath("//td[@class='gxsj']/span/text()").extract()#获取招聘发布日期集
    print timeMarks
    links = Selector(text = browser.page_source).xpath("//td[@class='zwmc']/div/a/@href").extract()#获取招聘链接集
    print links

    for i in range(len(titles)):
        fileName = titles[i].replace(':','-').replace('/','-').replace('\\', '-').replace('*', 'x').replace('|', '-').replace('?', '-').replace('<', '-').replace('>', '-').replace('"', '-').replace('\n', '-').replace('u2014','').replace('\t', '-')
        filePath = dirPath + os.sep + fileName + '.txt'  #os.sep 可以取代操作系统特定的路径分割符。

        with open(filePath, 'w') as fp:
            fp.write(titles[i])
            print titles[i]
            fp.write('$***$')
            fp.write(timeMarks[i])
            fp.write('$***$')
            fp.write(links[i])

def searchFunction(browser, url, keyWord, dirPath):
    browser.get(url)

#勾选城市
    browser.find_element_by_xpath("//input[@id='buttonSelCity']").click()
    time.sleep(2)
#     browser.find_element_by_xpath("//table[@class='sPopupTabC']/tbody/tr[1]/td/label/input[@iname='北京']").click()
#     time.sleep(2)
#     browser.find_element_by_xpath("//table[@class='sPopupTabC']/tbody/tr[1]/td/label/input[@iname='上海']").click()
#     time.sleep(2)
    browser.find_element_by_xpath("//table[@class='sPopupTabC']/tbody/tr[1]/td/label/input[@iname='深圳']").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class='sPopupTitle250']/div/a[1]").click()
    time.sleep(3)

#定位搜索框
    searchBox = browser.find_element_by_xpath("//div[@class='keyword']/input[@type='text']")

#发送搜索内容 
    searchBox.send_keys(keyWord)

#确认搜索   
    browser.find_element_by_xpath("//div[@class='btn']/button[@class='doSearch']").click()

#定位共140个职位满足条件，获取140数值
    totalCount = Selector(text = browser.page_source).xpath("//span[@class='search_yx_tj']/em/text()").extract()[0]   
  
    pageOver = int(totalCount) / 60 #一页显示60条信息
    for i in range(pageOver):
        time.sleep(3)
        writeFile(dirPath, browser.page_source)
        time.sleep(2)
        browser.find_element_by_link_text("下一页").click()    

    time.sleep(3)
    writeFile(dirPath, browser.page_source) 


if __name__ == '__main__':
    print 'START'
    url = 'http://www.zhaopin.com/'
    keyWord = u"玖富"
    dirPath = keyWord + u"招聘信息"

    if not os.path.exists(dirPath): #如果path存在，返回True；如果path不存在，返回False。
        os.makedirs(dirPath)

#定义一个火狐浏览器对象
    browser = webdriver.Chrome()
    searchFunction(browser, url, keyWord, dirPath)

    browser.close()
    print 'END'