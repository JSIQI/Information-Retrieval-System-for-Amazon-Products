# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class BestsellerSpider(scrapy.Spider):
    name = 'bestseller'
    allowed_domains = ['amazon.com']
    start_urls = [
        "https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab"]
    count = 0

    def parse4(self, response):
        items = response.xpath("//div[@class='zg_itemImmersion']//div[@class='zg_itemWrapper']")
        try:
            cat = {1: response.xpath("//div[@id='zg_left_col2']//ul[@id='zg_browseRoot']//ul/li["
                                     "@class='zg_browseUp']/a/text()").extract()[0].strip(),
                   2: response.xpath("//div[@id='zg_left_col2']//ul//ul//span[@class='zg_selected']/"
                                     "text()").extract()[0].strip()}
        except:
            cat = {1: None, 2: None}
            with open("result/error.txt", "a") as outfile:
                outfile.write("error: " + response)
        for i in items:
            item = AmazonItem()
            item['url'] = "https://www.amazon.com" + i.xpath(".//a[@class='a-link-normal']/@href").extract()[0]
            item['name'] = i.xpath(".//a[@class='a-link-normal']//div[2]/text()").extract()[0].strip()
            item['cat'] = cat
            yield item

    def parse3(self, response):
        cat2 = response.xpath("//div[@id='zg_left_col2']//ul//ul//span[@class='zg_selected']/text()").extract()[0]
        print(2, cat2)
        urls = response.xpath("//div[@id='zg_paginationWrapper']//a/@href").extract()
        # yield scrapy.Request(urls[0], callback=self.parse4)
        for u in urls:
            yield scrapy.Request(u, callback=self.parse4)

    def parse2(self, response):
        cat1 = response.xpath("//div[@id='zg_left_col2']//ul//ul//span[@class='zg_selected']/text()").extract()[0]
        print(1, cat1)
        urls = response.xpath("//div[@id='zg_left_col2']//ul//ul//a/@href").extract()
        if len(urls) == 0:
            yield scrapy.Request(response, callback=self.parse3)
        else:
            # yield scrapy.Request(urls[0], callback=self.parse3)
            for u in urls:
                yield scrapy.Request(u, callback=self.parse3)

    def parse(self, response):
        urls = response.xpath("//div[@id='zg_left_col2']//ul//ul//a/@href").extract()
        # yield scrapy.Request(urls[0], callback=self.parse2)
        for u in urls:
            yield scrapy.Request(u, callback=self.parse2)
