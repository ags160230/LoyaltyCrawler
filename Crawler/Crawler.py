import scrapy
import scrapy.exceptions

keywords = 'loyalty program million'

class Crawler(scrapy.Spider):
    name = 'Loyalty'

    custom_settings = {'CLOSESPIDER_ITEMCOUNT': 100}

    start_urls = ['https://google.com/search?q=' + keywords]

    def parse(self, response):
        for link in response.css('.r a'):
            yield {'link': 'https://google.com' + link.css('a::attr(href)').get()}

        next_page = response.css('#foot td a::attr(href)').getall()
        if next_page is not None:
            next_page_link = 'https://google.com' + next_page[9]
            yield scrapy.Request(url=next_page_link, callback=self.parse)
