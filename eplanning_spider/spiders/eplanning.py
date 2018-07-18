# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request, FormRequest


class EplanningSpider(Spider):
    name = 'eplanning'
    allowed_domains = ['eplanning.ie']
    start_urls = ['http://eplanning.ie/']

    def parse(self, response):
        urls = response.xpath('//a/@href').extract()
        for url in urls:
            if '#' == url:
                pass
            else:
                yield Request(url, callback=self.parse_application)

    def parse_application(self, response):
        app_url = response.xpath(
            '//*[@class="glyphicon-inbox btn-lg"]/following-sibling::a/@href').extract_first()

        yield Request(response.urljoin(app_url), callback=self.parse_form)

    # dont_filter = True to prevent filtering the same url
    def parse_form(self, response):
        yield FormRequest.from_response(response, formdata={'RdoTimeLimit': '42'},
                                        dont_filter=True, formxpath='(//form)[2]',
                                        callback=self.parse_pages)

    def parse_pages(self, response):
        pass
