import scrapy
from data_collector.models import RealEstateListing, session

class RealEstateSpider(scrapy.Spider):
    name = 'real_estate_spider'
    start_urls = ['https://example-real-estate.com'] # TODO: Set real estate website

    def parse(self, response):
        for listing in response.css('div.listing'):
            real_estate_listing = RealEstateListing(
                title=listing.css('h2.title::text').get(),
                price=listing.css('span.price::text').get(),
                location=listing.css('span.location::text').get(),
                link=listing.css('a::attr(href)').get()
            )
            session.add(real_estate_listing)
            session.commit()
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)