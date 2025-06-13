import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
import time
import csv
import os

class ImdbSpiderSpider(scrapy.Spider):
    name = "imdb_spider"

    def __init__(self):
        file_exists = os.path.isfile('imdb_top_250_movies.csv')
        self.csv_file = open('imdb_top_250_movies.csv', 'a', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)
        if not file_exists:
            self.csv_writer.writerow(['name', 'rating', 'genre', 'release_year', 'movie_runtime', 'imdb_link'])

    def start_requests(self):
        options = Options()
        options.add_argument('--headless')  # Run in headless mode

        service = Service('/usr/local/bin/geckodriver')  # path to the geckodriver
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window() #opens the browser on top
        driver.get('https://www.imdb.com')  # opens the URL
        time.sleep(3)

        menu_button = driver.find_element(By.ID, 'imdbHeader-navDrawerOpen')
        menu_button.click() 

        top_250_movies = driver.find_element(By.XPATH, '//a[@href="/chart/top/?ref_=nv_mv_250"]')
        top_250_movies.click()  
        time.sleep(3)

        get_links = driver.find_elements(By.XPATH, '//a[@href and descendant::h3]') #links with h3 tag as child

        for links in get_links:
            href = links.get_attribute('href')
            if href[0:27] == 'https://www.imdb.com/title/': #filtering out only the movie links
                yield scrapy.Request(url=href)

        driver.quit() 

    def parse(self, response):
        # extracting movie details
        name = response.css('span.hero__primary-text::text').get()
        rating = response.css('span.sc-d541859f-1::text').get()
        genres = response.xpath('//div[contains(@class, "ipc-chip-list__scroller")]//span[@class="ipc-chip__text"]/text()').getall()
        release_year = response.xpath('(//ul[@class="ipc-inline-list ipc-inline-list--show-dividers sc-d3b78e42-2 etAqcO baseAlt baseAlt"]/li)[1]/a/text()').get()
        movie_runtime = response.xpath('(//ul[@class="ipc-inline-list ipc-inline-list--show-dividers sc-d3b78e42-2 etAqcO baseAlt baseAlt"]/li)[3]/text()').get()

        # yielding the extracted data
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
