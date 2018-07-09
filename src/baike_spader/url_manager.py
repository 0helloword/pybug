#coding:utf-8

class UrlManager(object):
    
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
        
        
    def add_new_url(self,url):#添加新的url
        if url is  None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
          
    def add_new_urls(self,urls):#添加新的url列表
        if len(urls)==0:   #urls in None or 
            return
        else:
            for url in urls:
                self.add_new_url(url)
        

    
    def has_new_url(self):#判断是否有新的url
        return len(self.new_urls)!=0#如果新的url列表不为0则表示有新的url

    
    def get_new_url(self):#获取一个待爬取的url
        new_url=self.new_urls.pop()#pop从列表中获取一个url并且移除这个url
        self.old_urls.add(new_url)#将其添加到old_url中
        return new_url
        

  
    
    
    
    
    
    
    
    

