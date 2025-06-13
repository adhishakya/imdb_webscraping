from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
import time

#firefox config
options = Options()
options.headless = False
options.profile = FirefoxProfile()

service = Service('/usr/local/bin/geckodriver')  # path to the geckodriver
driver = webdriver.Firefox(service=service, options=options)
driver.maximize_window() #opens the browser on top
driver.get('https://www.imdb.com/')  # opens the URL
time.sleep(3)

menu_button = driver.find_element(By.ID, 'imdbHeader-navDrawerOpen')
menu_button.click() 

top_250_movies = driver.find_element(By.XPATH, '//a[@href="/chart/top/?ref_=nv_mv_250"]')
top_250_movies.click()  
time.sleep(5)

get_links = driver.find_elements(By.XPATH, '//a[@href and descendant::h3]') #links with h3 tag as child
movie_links = []

for links in get_links:
    href = links.get_attribute('href')
    if href[0:27] == 'https://www.imdb.com/title/': #filtering out only the movie links
        movie_links.append(href)

print(movie_links)
driver.close() 