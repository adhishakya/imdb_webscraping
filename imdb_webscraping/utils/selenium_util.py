from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from ..utils.config import url, xpath_top_250, gecko_driver_path, path_menu_button, xpath_movie_links, title_filter
import time
def get_movie_links():
    try:
        options = Options()
        options.add_argument('--headless')  # Run in headless mode
        service = Service(gecko_driver_path)  # path to the geckodriver
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window() #opens the browser on top
        driver.get(url)  # opens the URL
        time.sleep(3)
        menu_button = driver.find_element(By.ID, path_menu_button)
        menu_button.click() 
        top_250_movies = driver.find_element(By.XPATH, xpath_top_250)
        top_250_movies.click()  
        time.sleep(3)
        get_links = driver.find_elements(By.XPATH, xpath_movie_links) #links with h3 tag as child
        links = [
            link.get_attribute('href') for link in get_links if link.get_attribute('href').startswith(title_filter)
        ]
        return links
    
    finally:
        driver.quit() 