# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class scrapyFormRequestDemoSpider(scrapy.Spider):
    name = 'scrapyFormRequestDemoSpider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        # extracting csrf_token for login form request parameter
        csrf_token = response.xpath(
            '//*[@name="csrf_token"]/@value').extract_first()
        # sending post request with login form request parameters with url
        yield FormRequest('http://quotes.toscrape.com/login',
                          formdata={'csrf_token': csrf_token,
                                    'username': 'foobar',
                                    'password': 'foobar'},
                          callback=self.parse_login_page_after_submit)
    # parse login page check response of post request
    def parse_login_page_after_submit(self, response):
        open_in_browser(response)
        # checking if response contains condition then it's sure successful login completed.
        # if response.xpath('//a[text()="Logout"]'):
        #     self.log('You logged in!')
