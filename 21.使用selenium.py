# -*- coding: utf-8 -*-
#学习使用selenium
from selenium import webdriver
chrome = webdriver.Chrome()
chrome.get('http://www.baidu.com')
chrome.save_screenshot('baidu.png')
print(chrome.page_source)
chrome.quit()
