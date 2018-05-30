# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from wyzw.items import WyzwItem
from wyzw import urlSettings
from wyzw import fileUtil
import re
import pdb

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['booktxt.net']
    base_url = 'http://www.booktxt.net'
    start_urls = ['http://www.booktxt.net/2_2591/']

    def parse(self, response):
        #sel:page code
        sel = Selector(response)
        url_list = sel.xpath(urlSettings.POST_URL_XPATH).extract()
        for i in url_list:
            item = WyzwItem()
            item['url'] = self.base_url + i
            #fileUtil.save_content('url',page_url+'\n')
            yield scrapy.Request(item['url'], meta={'item':item}, callback=self.content_parse)
    
    def content_parse(self, response):
        item = response.meta['item']
        title = response.xpath(urlSettings.POST_TITLE_XPATH).extract()
        item['title'] = title[0][5:-5].strip()
        item['text'] = response.xpath(urlSettings.POST_TEXT_XPATH).extract()
        #过滤文章
        text_content = item['text'][0][42:-46]
        text_content = text_content.replace('<br>\r\n<br>\r\n\xa0\xa0\xa0\xa0','')

        #正则过滤标点符号
        r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
        item['text'] = re.sub(r,' ',text_content)
        #去掉中文标点符号
        item['text'] = item['text'].replace('，',' ').replace('。',' ').replace('“',' ').replace('”','').replace('！','').replace('（','').replace('）','').replace('？','').replace('、','').replace('——','')
        item['text'] = item['text'].replace('请翻页域者','')
        fileUtil.save_content(item['title'],item['text'])
        print(item['title'] + ' is download done!')
