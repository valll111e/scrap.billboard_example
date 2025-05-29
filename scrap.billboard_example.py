##xpath scraping
from selenium import webdriver
import pandas as pd
profile = "https://www.billboard.com/charts/hot-100/"
driver=webdriver.Chrome(executable_path="/Users/chromedriver")
driver.get(profile)
find_rank=driver.find_elements_by_xpath(
    "//span[@class='c-label  a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet']")
find_artist=driver.find_elements_by_xpath(
    "//span[@class='c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only']")
find_title=driver.find_elements_by_xpath(
    "//h3[@class='c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only']")
ranking = []
for rank in find_rank:
    this_rank = rank.text
    ranking.append(this_rank)

artist = []
for art in find_artist:
    this_art = art.text
    artist.append(this_art)

titles = []
for title in find_title:
    this_title = title.text
    titles.append(this_title)

find_title_1st = driver.find_elements_by_xpath(
    "//h3[@class='c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet']")
find_artist_1st = driver.find_elements_by_xpath(
    "//h3[@class='c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only']")
artist_1st = find_artist_1st[0].text.strip()
title_1st = find_title_1st[0].text.strip()
data = {'Rank': ranking, 'Title': titles, 'Artist': artist}
df = pd.DataFrame(data)
df

##BeautifulSoup Scraping

import pandas as pd
import requests
from bs4 import BeautifulSoup
profile='https://www.billboard.com/charts/hot-100/'
html_content=requests.get(profile).text
soup = BeautifulSoup(html_content, 'html.parser')
soup
find_rank=soup.find_all(
    "span", class_="c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet")
find_artist=soup.find_all(
    "span",class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
find_title=soup.find_all(
    "h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
ranking = []
for rank in find_rank:
    this_rank = rank.get_text().strip()
    ranking.append(this_rank)
print(this_rank)

artist = []
for art in find_artist:
    this_art=art.get_text().strip()
    artist.append(this_art)
print(this_art)

titles = []
for title in find_title:
    this_title=title.get_text().strip()
    titles.append(this_title)
print(this_title)
data = {'Rank':ranking, 'Title':title, 'Artist':artist}
df = pd.DataFrame(data)
df