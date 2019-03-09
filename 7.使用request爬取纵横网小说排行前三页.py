# -*- coding: utf-8 -*-
#request练习
#用request爬去纵横网小说排行前三页
import requests
def OpenUrl(url):
    req = requests.get(url)
    return req.text
def SaveHtml(html,filename):
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)
def Main():
    for i in range(3):
        base_url = 'http://www.zongheng.com/rank/details.html?rt=3&d=1&p={}'.format(i+1)
        SaveHtml(OpenUrl(base_url),filename='第{}页.html'.format(i+1))

if __name__ == '__main__':
    Main()




