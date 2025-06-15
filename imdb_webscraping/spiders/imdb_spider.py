import scrapy
from ..utils.selenium_util import get_movie_links
from ..utils.config import xpath_movie_name, xpath_rating, xpath_genres, xpath_release_year, xpath_movie_runtime
from ..items import ImdbWebscrapingItem

class ImdbSpiderSpider(scrapy.Spider):
    name = "imdb_spider"

    def start_requests(self):
        get_links = get_movie_links() 
        for links in get_links:
            yield scrapy.Request(url=links, callback=self.parse)

    def parse(self, response):
        # extracting movie details
        item = ImdbWebscrapingItem()
        item['name'] = response.css(xpath_movie_name).get()
        item['rating'] = response.css(xpath_rating).get()
        genres = response.xpath(xpath_genres).getall()
        item['genres'] = ' / '.join([genre.strip() for genre in genres])
        item['release_year'] = response.xpath(xpath_release_year).get()
        item['movie_runtime'] = response.xpath(xpath_movie_runtime).get()
        item['imdb_link'] = response.url

        yield item
