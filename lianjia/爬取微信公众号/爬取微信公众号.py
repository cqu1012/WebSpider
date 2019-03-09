# -*- coding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import org.openqa.selenium.keys
# keyword = input('请输入你需要爬取的关键字：')
keyword = '手机'
chrome = webdriver.Chrome()
chrome.get('https://weixin.sogou.com/')
inp = chrome.find_element_by_class_name('query')
inp.send_keys(keyword)
srh = chrome.find_element_by_class_name('swz')
srh.click()
html = chrome.page_source
titles = chrome.find_elements_by_xpath('//h3')
for title in titles:
    content =  title.click()
    time.sleep(3)
    # content.close()
    # chrome.close()
    # ActionChains(chrome).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
    # ActionChains(chrome).key_down(Keys.CONTROL).send_keys('w').perform()
    action = ActionChains(chrome)
    action.key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).send_keys(Keys.NULL).perform();



