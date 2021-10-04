import time
import requests
import lxml
from bs4 import BeautifulSoup as bs
import cloudscraper
from selenium import webdriver


def get_page_source(url):
    # use webdriver to execute the JS so we can produce a full DOM for the webpage
    driver = webdriver.Firefox(executable_path='C:/Program Files/UmarStuff/GeckoDriver/geckodriver.exe')
    driver.get(url)
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    # sleep for 10s to let the page load
    time.sleep(2)
    page_source = driver.page_source
    driver.quit()
    return page_source


def get_make_and_model(dom_element):
    section = dom_element.find_all('section', limit=2)
    name = section.find_all('h1')
    print(name)

url = 'http://www.autotrader.co.uk/car-details/202108166303615?advertising-location=at_cars&price-from=500&radius=20&postcode=ng96hx&fuel-type=Petrol&sort=relevance&onesearchad=New&onesearchad=Nearly%20New&onesearchad=Used&transmission=Manual&price-to=2000&include-delivery-option=on&page=2'
page = get_page_source(url)

soup = bs(page, 'html.parser')
# print(soup.prettify())

# make, model = get_make_and_model(soup.find('aside'))
get_make_and_model(soup.find('aside'))

# with open('test-page.html', 'w') as f:
#     f.write(soup.prettify())

# # use cloudscraper to avoid CloudFlare blocking access to the website because you're a bot
# scraper = cloudscraper.create_scraper()
# source = scraper.get(page).text
#
# # soup = bs(source, 'lxml')
# soup = bs(source, 'html.parser')
#
# container = soup.find_all('div', attr={'class':'js-event-list-tournament-events'})
# print(container)

# aside = soup.find('aside')

# print(soup.prettify())
# name = aside.find_all('section', limit=2)
# print(name)
