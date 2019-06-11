# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse
class SeleniumDownloadMiddleware():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches",['enable-automation'])
        self.driver = webdriver.Chrome(options=self.options)
    def process_request(self,request,spider):
        self.driver.get(request.url)
        time.sleep(1)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        summitBtn = self.driver.find_element_by_class_name('btn log-in')
        time.sleep(2)
        summitBtn.click()
        source = self.driver.page_source
        # 把请求到source封装成一个response对象返回给引擎再给spider进行处理
        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        time.sleep(2)
        return response

