# -*- coding: utf-8 -*-
import scrapy

from scrapy_Enerprise.items import JWcropItem


class JWcorpSpider(scrapy.Spider):
    name = 'JWcorp'
    allowed_domains = ['femhzs.mofcom.gov.cn']
    start_urls = ['http://femhzs.mofcom.gov.cn/fecpmvc/pages/fem/CorpJWList.html']

    def parse(self, response):

        for tr in response.css('tr[id^=foreach]'):
            item = JWcropItem()
            li = list(map(lambda x: x.strip()[:-1] if ';' in x else x.strip(), tr.css('td::text').extract()))
            item['Overseas_Investment_Enterprises'] = li[0]
            item['Domestic_Investment_name'] = li[1]
            item['Investment_Country'] = li[2]
            yield item

        next_page = response.xpath('//div/a[@class="last pagenxt"]/@href').extract_first()
        next_url = 'http://femhzs.mofcom.gov.cn' + next_page
        yield scrapy.Request(next_url, callback=self.parse)


