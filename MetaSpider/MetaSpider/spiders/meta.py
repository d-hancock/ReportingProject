import scrapy

class MetaSpider(scrapy.Spider):
    name = "MetaAndH1"

    def start_requests(self):
        urls = [

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):



        page = response.url
        title = response.xpath('/html/head/title')
        desc = response.xpath("/html/head/meta[@name="description"]/@content")
        h1 = response.xpath('//h1')