from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json
class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']
    rules = [Rule(LinkExtractor(deny=r'.*'), callback='parse_items', follow=False)]

    def parse_items(self, response):
        title = response.css('h1::text').extract_first()
        link = response.css('tr a::attr(href)').get()
        data = json.dumps({title:link})
        with open('data.json', 'a') as file:
            file.write(data)
            file.write("\n")
        