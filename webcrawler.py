from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlSpider(CrawlSpider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/quotes/')),
        Rule(LinkExtractor(allow=r'/quotes/' , deny="category"), callback='parse_item', follow=True),
    )


