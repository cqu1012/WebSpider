# -*- coding: utf-8 -*-
from threading import Thread
from fake_useragent import UserAgent
from queue import Queue
import requests
from time import sleep
from lxml import etree

#创建线程类
class Spider(Thread):
    def __init__(self,url_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
    def run(self):
        url = self.url_queue.get()
        rsp = requests.get(url,headers={'User-Agent':UserAgent().random})
        html =etree.HTML(rsp.text)
        contents =[div.xpath('string(.)').strip()  for div in  html.xpath('//div[@class="content"]')]
        with open('段子.txt','a',encoding='utf-8') as f:
            for content in contents:
                f.write(content+'\n')

def main():
    headers = {'User-Agent':UserAgent().random}
    base_url= 'https://www.qiushibaike.com/text/page/{}/'
    url_queue = Queue()
    for i in range(1,6):
        url = base_url.format(i)
        url_queue.put(url)
        spider=Spider(url_queue)
        spider.start()
        sleep(2)

if __name__ == '__main__':
    main()

