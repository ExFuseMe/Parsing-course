import scrapy
class PythonSpider(scrapy.Spider):
    name='article'
    def start_requests(self):
        urls = ['https://docs.python.org/3/tutorial/index.html']
        return [scrapy.Request(url=url,callback=self.parse)for url in urls]
    def parse(self, response):
        title =response.css('h1::text').extract_first()
        print('Article: ',title)