"""
Loyalty Crawler web crawling and parsing spider
"""
import scrapy
import scrapy.exceptions
from webapp.models import ArchiveManager, CriteriaManager

"""
# global variable for search criterion id (default is one)
search_criterion_id = 1


# Function to set the (global) search criterion id to use when running the spider
# (call this when performing user I/O to select criterion for new session)
def set_search_criterion_id(s_c_id):
    global search_criterion_id
    search_criterion_id = s_c_id


# Function to generate seed urls for the spider
def generate_parameters(s_c_id):
    record = CriteriaManager.get_criterion(s_c_id)
    keywords = record.criterion
    seed_urls = ['https://google.com/search?q=' + keywords]
    return seed_urls
"""


class Crawler(scrapy.Spider):
    name = 'Daddy Crawl Legs'
    custom_settings = {'CLOSESPIDER_ITEMCOUNT': 100}            # the condition to stop when amount hit 100
    session_id = ArchiveManager.get_last_session_id() + 1
    record = CriteriaManager.get_criterion_to_use()
    keywords = record.criterion
    start_urls = ['https://google.com/search?q=' + keywords]

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
        else:
            CriteriaManager.reset_criterion_to_use()
            # return url_list
