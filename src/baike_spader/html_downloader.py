#coding:utf-8
import urllib2#urllib2就是使用各种协议打开url的一个扩展包

class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        
        response=urllib2.urlopen(url)
        
        if response.getcode()!=200:
            return None
        
        return response.read()
    
    

