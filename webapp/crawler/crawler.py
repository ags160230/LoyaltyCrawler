"""
Loyalty Crawler web crawling and parsing spider
"""
import scrapy
import scrapy.exceptions
from webapp.models import ArchiveManager, CriteriaManager


# Function to generate seed urls for the spider
# (call this function for user I/O selection of criterion)
def generate_parameters(search_criterion_id):
    criterion = CriteriaManager.get_criterion(search_criterion_id)
    keywords = criterion.criterion
    start_urls = ['https://google.com/search?q=' + keywords]
    return start_urls


class Crawler(scrapy.Spider):
    name = 'Daddy Crawl Legs'
    custom_settings = {'CLOSESPIDER_ITEMCOUNT': 100}            # the condition to stop when amount hit 100
    session_id = ArchiveManager.get_last_session_id() + 1
    start_urls = generate_parameters(1)

    def parse(self, response):
        # url_list = []

        for link in response.css('.r a'):
            ArchiveManager.create_artifact(self.session_id, 'https://google.com' + link.css('a::attr(href)').get())
            # url_list.append('https://google.com' + link.css('a::attr(href)').get()) # if returning list
            # yield {'link': 'https://google.com' + link.css('a::attr(href)').get()}

        next_page = response.css('#foot td a::attr(href)').getall()

        if next_page is not None:
            next_page_link = 'https://google.com' + next_page[9]
            yield scrapy.Request(url=next_page_link, callback=self.parse)
        """
        else:
            return url_list
        """

