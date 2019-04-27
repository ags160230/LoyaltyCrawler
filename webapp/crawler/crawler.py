"""
Loyalty Crawler web crawling and parsing spider
"""
from twisted.internet import reactor
import scrapy
import scrapy.exceptions
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from webapp.models import ArchiveManager, CriteriaManager


class Crawler(scrapy.Spider):
    name = 'Daddy Crawl Legs'
    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': 25,   # the condition to stop when amount hit 100
        'USER_AGENT': 'Chrome/60.0.3112.113',
        # 'FEED_FORMAT': 'json',
        # 'FEED_URI': 'link.json'
    }
    session_id = ArchiveManager.get_last_session_id() + 1
    # record = CriteriaManager.get_criterion_to_use()
    # keywords = record.criterion
    keywords = "rewards"
    start_urls = ['https://google.com/search?q=' + keywords]
    count = 0
    COUNT_MAX = 25

    def parse(self, response):
        # url_list = []

        for link in response.css('.r a'):
            ArchiveManager.create_artifact(self.session_id, 'https://google.com' + link.css('a::attr(href)').get())
            # url_list.append('https://google.com' + link.css('a::attr(href)').get()) # if returning list
            # yield {'link': 'https://google.com' + link.css('a::attr(href)').get()}
            self.count += 1

        if self.count == self.COUNT_MAX:
            exit()

        """
        next_page = response.css('#foot td a::attr(href)').getall()
         
        if next_page is not None:
            next_page_link = 'https://google.com' + next_page[9]
            yield scrapy.Request(url=next_page_link, callback=self.parse)
        # else:
            # CriteriaManager.reset_criterion_to_use()
            # return url_list
        """


def run_crawler():
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner()
    spider = runner.crawl(Crawler)
    spider.addBoth(lambda _: reactor.stop())
    reactor.run(installSignalHandlers=False)

