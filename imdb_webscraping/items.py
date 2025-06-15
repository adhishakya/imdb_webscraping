# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbWebscrapingItem(scrapy.Item):
    name = scrapy.Field()
    rating = scrapy.Field()
    genres = scrapy.Field()
    release_year = scrapy.Field()
    movie_runtime = scrapy.Field()
    imdb_link = scrapy.Field()
