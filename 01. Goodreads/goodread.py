# -*- coding: utf-8 -*-
import scrapy


class GoodreadSpider(scrapy.Spider):
    name = 'goodread'
    allowed_domains = ['www.goodreads.com/quotes/']
    start_urls = ['https://www.goodreads.com/quotes/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
        	text = quote.xpath('.//*[@class="quoteText"]/text()').extract_first()
        	author = quote.xpath('.//*[@class="authorOrTitle"]/text()').extract_first()
        	
        	# print(text)
        	# print(author)
        	# print('\n')

        	yield{	'Text': text,
        			'Author': author}
        next_page_url = response.xpath('//*[@class="next_page"]/@href').extract_first()
        if(next_page_url!=''):
        	absolute_next_page_url = response.urljoin(next_page_url)
        	yield scrapy.Request(absolute_next_page_url, dont_filter=True)
