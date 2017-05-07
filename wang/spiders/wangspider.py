# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ali.items import AliItem
class wang(scrapy.Spider):
    name = 'wang'


    def start_requests(self):
        start_url=['https://mojim.com/cnh104044-A2.htm']
        for url in start_url:
            yield scrapy.Request(url=url,callback=self.parse_getlink)


    def parse_getlink(self,response):
        n=0
        #print response.url
        soup = BeautifulSoup(response.body,'lxml')
        for i in soup.find_all('div',id='inS'):
            for j in i.find_all('a'):
               url = j.get('href')
               url = 'https://mojim.com' + str(url)
               yield scrapy.Request(url=url, callback=self.parse)
               n+=1

        print n


    def parse(self,response):
        item = AliItem()
        soup = BeautifulSoup(response.body,'lxml')
        for i in soup.find_all('dd',id='fsZx3'):
            item['content'] = i.get_text()
            yield item