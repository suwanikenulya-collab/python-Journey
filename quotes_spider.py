import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        for quote in response.css("span.text::text"):
            print(quote.get())