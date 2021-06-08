import requests
from bs4 import BeautifulSoup


def get_info_article(url_domain):
    page = requests.get(url_domain)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify()) --> to save a fic to analyse (bash: python3 scrap_20min_subDom.py > html_test.html)

url = 'https://www.20minutes.fr/economie/emploi/'
get_info_article(url)






#to change an attribute value
"""def set_attribute(driver, *args):
    driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", *args)

search_result = driver.find_element_by_id('load-more')
set_attribute(driver, search_result, "data-load", "3")
print(search_result.get_attribute('data-load'))"""