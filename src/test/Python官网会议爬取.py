#-*-coding:utf-8-*-

#HTMLParser
#第一步是用爬虫把python官网的会议页面抓下来，第二步解析该HTML页面，获取会议名称，时间和地点

import urllib   #urllib提供了一系列用于操作URL的功能。
from HTMLParser import HTMLParser

class PyEventParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._count = 0     #初始化会议的个数为0
        self._events = dict()     #会议数据初始化为一个空字典
        self._flag = None        #初始化标签为空

    def handle_starttag(self, tag, attrs):#通过开始标签获取会议的标题，时间，地点
        if tag=='h3' and attrs.__contains__(('class','event-title')):#会议标题的html标签为<h3,属性值中包含 class="event-title"
            self._count+=1
            self._events[self._count]=dict()
            self._flag='event-title'
        if tag=='time':#会议时间的html标签为<time self._flag='time'
            self._flag='time'
        if tag=='span' and attrs.__contains__(('class','event-location')):#会议地点标签为<span,属性包含class="event-location" 
            self._flag='event-location'
            
    def handle_data(self, data):#根据标签获取数据
        if self._flag=='event-title':
            self._events[self._count][self._flag]=data
        if self._flag=='time':
            self._events[self._count][self._flag]=data
        if self._flag=='event-location':
            self._events[self._count][self._flag]=data
        self._flag=None
        
    def event_list(self):
        print '近期关于python的会议有：',self._count,'个，具体如下：'
        #print self._events.values()#打印会议的全部信息
        for event in self._events.values():
            print event['event-title'],'\t',event['time'],'\t',event['event-location']
        
parser=PyEventParser()      
pypage=urllib.urlopen('https://www.python.org/events/python-events/')#打开爬取网页地址
pyhtml=pypage.read()#获取网页源码
parser.feed(pyhtml)#解析html
parser.event_list()#打印会议信息
parser.close()

