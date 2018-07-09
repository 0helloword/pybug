#-*-coding:utf-8-*-
from HTMLParser import  HTMLParser
import urllib


class PyNewsParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._count=0
        self._news=dict()
        self._flag=None
    
    def handle_starttag(self, tag, attrs):
        if tag=='h3' and attrs.__contains__(('class','company_name')):
            self._count+=1
            self._news[self._count]=dict()
            self._flag='company_name'
        if tag=='p' and attrs.__contains__(('class','txt oneline')):
            self._flag='txt oneline'
            
    def handle_data(self, data):
        if self._flag=='company_name':
            self._news[self._count][self._flag]=data
        if self._flag=='txt oneline':
            self._news[self._count][self._flag]=data
          
        self._flag=None
              
    def news_list(self):
        print 'csdn今日推荐的文章共',self._count,'条，具体如下：'
#         print self._news.values()
        for news in self._news.values():
         
            print news['company_name'],'\t'#news['txt oneline']

parser=PyNewsParser()
pypage=urllib.urlopen('https://www.csdn.net/')
pyhtml=pypage.read()
parser.feed(pyhtml)
parser.news_list()
parser.close()            
    
            