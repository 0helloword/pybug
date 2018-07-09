#coding:utf-8
from baike_spader import url_manager
from baike_spader import html_downloader
from baike_spader import html_outputer
from baike_spader import html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()#初始化url管理器
        self.downloader=html_downloader.HtmlDownloader()#初始化url下载器
        self.parser=html_parser.HtmlParser()#初始化网页解析器
        self.outputer=html_outputer.HtmlOutputer()#初始化输出器
        
    def craw(self,root_url):#爬虫调度方式craw
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()#从url管理器获取一个新的url
                print 'craw %d:%s'%(count,new_url)
                html_cont=self.downloader.download(new_url)#启动下载器，将下载的页面数据保存在html_cont
                #print html_cont
                new_urls,new_data=self.parser.parse(new_url,html_cont)#调用解析器解析页面数据，得到新的url列表和新的数据
#                 print new_urls
                self.urls.add_new_urls(new_urls)#解析出来新的url添加到url列表
                print new_data
                self.outputer.collect_data(new_data)#收集数据
                
                if count==100:
                    break
                
                count=count+1
        
            except:
                print 'craw failed'
        self.outputer.output_html()#将收集的数据输出
    


if __name__=="__main__":
    root_url="https://baike.baidu.com/item/Python"#入口地址
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)#启动爬虫
    
    
    