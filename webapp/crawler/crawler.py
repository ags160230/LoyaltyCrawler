"""
Loyalty Crawler web crawling and parsing spider
"""
import scrapy
import scrapy.exceptions
# from .models Artifacts, ArchiveManager (link this correctly so this works)

keywords = 'loyalty program million'


class Crawler(scrapy.Spider):
    name = 'Loyalty'

    custom_settings = {'CLOSESPIDER_ITEMCOUNT': 100}            # the condition to stop when amount hit 100

    start_urls = ['https://google.com/search?q=' + keywords]    # place inside function and add search criteria

    """ for loop to pass one search criteria at a time -> function() """

    """
    def crawl(self, search_criterion_id):
        keyword = CriteriaManager.get_criterion(search_criterion_id)
        # start spider
    """


    def parse(self, response):
        for link in response.css('.r a'):
            yield {'link': 'https://google.com' + link.css('a::attr(href)').get()}
            print("damn")

        next_page = response.css('#foot td a::attr(href)').getall()

        if next_page is not None:
            next_page_link = 'https://google.com' + next_page[9]
            yield scrapy.Request(url=next_page_link, callback=self.parse)
