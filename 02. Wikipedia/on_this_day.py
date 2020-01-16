# -*- coding: utf-8 -*-
import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']

    def parse(self, response):
        otd = response.xpath('//*[@id="mp-otd"]')               #Selects the 'otd' section of wiki.
        date = otd.xpath('.//p/b/a/@title').extract_first()     #Today's date
        our_list = otd.xpath('.//ul')[0]	    	        #It has 3 uls, we are interested in the first one
        news = our_list.xpath('.//text()').extract()	        #Taking all the news from ul
        listed_news = ''.join(news)		                #Joining them all

        print('\n\nToday is ' + date + ', and this is what happened today')
        print(listed_news)
        print('\n\n')
