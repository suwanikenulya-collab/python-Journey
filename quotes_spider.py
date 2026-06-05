# Import the Scrapy library
import scrapy


# Create a spider (the web-crawling robot)
class QuotesSpider(scrapy.Spider):

    # Give the spider a name
    # This is used when running the spider
    name = "quotes"

    # List of websites where the spider should start
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    # This method runs automatically when a page is downloaded
    def parse(self, response):

        # Find all quote text on the page
        # CSS selector:
        # span.text = find <span class="text">
        # ::text = get only the text inside it
        for quote in response.css("span.text::text"):

            # Extract the actual text and print it
            print(quote.get())