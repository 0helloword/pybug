# -*-coding:utf-8 -*-
import string
import urllib2#urllib2就是使用各种协议打开url的一个扩展包

# 抓取新浪微博一个话题下所有页面，并以html文件形式储存在本地，路径为当前工程目录

def writeHTML(url,start_page,end_page):
    for i in range (start_page,end_page+1):
        Filename=string.zfill(i,3)   # zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0
        HtmlPath=Filename+'.html'
        print 'downloading No.'+str(i)+'page and save as'+Filename+'.html'
        f=open(HtmlPath,'w+')
        html=urllib2.urlopen(url+str(i)).read()  
        f.write(html)
        f.close()
        
    

def crawler():#爬取热门微博的网页，直接爬取http://weibo……下载页面空白
    url='http://s.weibo.com/weibo/%25E5%25A5%25B3%25E7%2594%259F%25E7%25BD%2591%25E8%25B4%25AD%25E7%259A%2584%25E6%2597%25A5%25E5%25B8%25B8?topnav=1&wvr=6&b=1'
    s_page=1
    e_page=2
    print 'now begin to download html page'
    writeHTML(url,s_page,e_page)
    
if __name__=='__main__':
    crawler()