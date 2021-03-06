import scrapy
from scrapy_splash import SplashRequest
from lxml import etree


class ListingSpider(scrapy.Spider):
    name = "listing"
    start_urls = ["http://www.mlslistings.com/search/keyword/95008/openhouse/false/listingstatus/1/propertyclass/1"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5},)

    def parse(self, response):
        nodes = response.xpath('//div[@class="listResults ng-scope"]').extract()

        # for node in nodes:
        #     house = Property()
        #     tree = etree.HTML(node)
        #     house.price = tree.xpath('//span[@class="listSalePrice ng-binding"]/text()')[0]
        #     house.addr = tree.xpath('//span[@class="longAddress ng-binding"]/text()')[0]
        #     house.type = tree.xpath('//span[@class="subClass ng-binding"]/text()')[0]
        #     house.beds = tree.xpath('//span[@class="beds"]/span[@class="itemValue ng-binding"]/text()')[0]
        #     house.baths = tree.xpath('//span[@class="baths"]/span[@class="itemValue ng-binding"]/text()')[0]
        #     house.sqft = tree.xpath('//span[@class="structureSqFt"]/span[@class="itemValue ng-binding"]/text()')[0]
        #     house.sqftlot = tree.xpath('//span[@class="lotSqFt"]/span[@class="itemValue ng-binding"]/text()')[0]
        #     house.print_details()
