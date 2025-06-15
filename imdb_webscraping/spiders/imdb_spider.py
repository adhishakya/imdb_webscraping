import scrapy
import csv
import os
from ..utils.selenium_util import get_movie_links
from ..utils.config import xpath_movie_name, xpath_rating, xpath_genres, xpath_release_year, xpath_movie_runtime

class ImdbSpiderSpider(scrapy.Spider):
    name = "imdb_spider"

    def __init__(self):
        file_exists = os.path.isfile('imdb_top_250_movies.csv')
        self.csv_file = open('imdb_top_250_movies.csv', 'a', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)
        if not file_exists:
            self.csv_writer.writerow(['name', 'rating', 'genre', 'release_year', 'movie_runtime', 'imdb_link'])

    def start_requests(self):
        get_links = get_movie_links() 
        for links in get_links:
            yield scrapy.Request(url=links, callback=self.parse)

    def parse(self, response):
        # extracting movie details
        name = response.css(xpath_movie_name).get()
        rating = response.css(xpath_rating).get()
        genres = response.xpath(xpath_genres).getall()
        release_year = response.xpath(xpath_release_year).get()
        movie_runtime = response.xpath(xpath_movie_runtime).get()

        movie_details = {
            'name': name if name else 'N/A',
            'rating': rating if rating else 'N/A',
            'genre': ' / '.join(genres) if genres else 'N/A',
            'release_year': release_year if release_year else 'N/A',
            'movie_runtime': movie_runtime if movie_runtime else 'N/A',
            'imdb_link': response.url
        }
        print(movie_details)

        self.csv_writer.writerow([
            movie_details['name'],
            movie_details['rating'],
            movie_details['genre'],
            movie_details['release_year'],
            movie_details['movie_runtime'],
            movie_details['imdb_link']
        ])


    def closed(self, reason):
        self.csv_file.close()
