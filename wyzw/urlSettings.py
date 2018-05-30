# -*- coding:utf-8 -*-

#domain
DOMAIN = 'booktxt.net'

#scrapy name
SPIDER_NAME = 'text'

GROUP_ID = '33'

#文章起始url
START_URL = 'http://www.booktxt.net/2_2591/'

#文章url爬取规则XPATH
POST_URL_XPATH = '//div[@class="box_con"]/div/dl/dd/a/@href'

#文章标题爬取规则
POST_TITLE_XPATH = '//div[@class="bookname"]/h1'

#文章内容爬取规则
POST_TEXT_XPATH = '//div[@class="box_con"]/div[@id="content"]' 
