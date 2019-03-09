# -*- coding: utf-8 -*-
#使用selenium 爬取虎牙直播信息
from selenium import webdriver
from lxml import etree
import time
def getMsg(html):
    '''
    :param html: 网站html信息
    :return: 主播信息与人数
    '''
    html = etree.HTML(html)
    titles = html.xpath("//li[@class='game-live-item']/a[2]/text()")
    names =html.xpath("//li[@class='game-live-item']/span/span[@class='avatar fl']/i/text()")
    peopleNum = html.xpath("//li[@class='game-live-item']/span/span/i[2]/text()")
    return titles,names,peopleNum

def main():
    url = 'https://www.huya.com/g/4'
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    selm = webdriver.Chrome(chrome_options=options)
    selm.get(url)
    while True:
        html = selm.page_source
        titles, names, peopleNum = getMsg(html)
        for title,name,people in zip(titles,names,peopleNum):
            print('title:{},name:{},people:{}'.format(title,name,people))
        #判断是否有下一页
        html = etree.HTML(html)
        nextPage = html.xpath("//div[@class='laypage_main laypageskin_default']/a[@class='laypage_next']")
        # test = html.xpath('//div[@clas="123"]')
        # print(test,type(test))
        test = selm.page_source.find('123')
        print(test)
        if len(nextPage) != 0:
            #点击下一页
            selm.find_element_by_class_name('laypage_next').click()
            time.sleep(3)
        else:
            break
if __name__ == '__main__':
    main()
