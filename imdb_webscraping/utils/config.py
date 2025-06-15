url = 'https://www.imdb.com' # base url
gecko_driver_path = '/usr/local/bin/geckodriver'  # Path to the geckodriver executable
path_menu_button = 'imdbHeader-navDrawerOpen'  # ID of the menu button in the header
xpath_top_250 = '//a[@href="/chart/top/?ref_=nv_mv_250"]' # path to the top 250 movies link in the menu
xpath_movie_links = '//a[@href and descendant::h3]'  # XPath to find movie links with h3 tag as child
title_filter = 'https://www.imdb.com/title/' # link extraction criteria
xpath_movie_name = 'span.hero__primary-text::text' # movie name
xpath_rating = 'span.sc-d541859f-1::text' # movie rating
xpath_genres = '//div[contains(@class, "ipc-chip-list__scroller")]//span[@class="ipc-chip__text"]/text()' # movie genres
xpath_release_year = '(//ul[@class="ipc-inline-list ipc-inline-list--show-dividers sc-d3b78e42-2 etAqcO baseAlt baseAlt"]/li)[1]/a/text()' # movie release year
xpath_movie_runtime = '(//ul[@class="ipc-inline-list ipc-inline-list--show-dividers sc-d3b78e42-2 etAqcO baseAlt baseAlt"]/li)[3]/text()' # movie runtime