
#练习处理滚动条
from selenium import webdriver
from time import sleep
from lxml import etree
url = 'https://search.jd.com/Search?keyword=%E6%B8%B8%E6%88%8F%E6%89%8B%E6%9C%BA&enc=utf-8&spm=2.1.1'
#简历webdriver对象
driver = webdriver.Chrome()
driver.get(url)
#处理滚动条
js = 'document.documentElement.scrollTop=10000'
# js = 'doucument.body.scrollTop=10000'
# js="var q=document.getElementById('id').scrollTop=10000"
driver.execute_script(js)
sleep(3)
#返回页面
html = driver.page_source
driver.quit()
#建立etree对象
Html = etree.HTML(html)
priceList = Html.xpath("//div[@class='p-price']/strong/i/text()")
titleList = Html.xpath("//li[@class='gl-item']/div/div/a/@title")
nameList = Html.xpath("//li[@class='gl-item']/div/div/a/em/text()")

for name,price,title in zip(nameList,priceList,titleList):
    print("{}:{}".format(name,price))

print(len(priceList))




