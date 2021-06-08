# -*- coding: utf-8 -*-

import sys
import time
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def accept_cookies(driver):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'didomi-notice-agree-button'))).click()
    except:
        print("Cookies have been already accepted.")


def get_article_text(driver, article_url, articles_texts):
    driver.get(article_url)
    accept_cookies(driver)

    try:
        full_text = []
        search_results = driver.find_elements_by_class_name('article-content')
        for result in search_results:
            elements = result.find_elements_by_css_selector('p')
            for element in elements:
                full_text.append(element.text)
        articles_texts.append(" ".join(full_text))
    except:
        print(f"There is a problem with {article_url} to extract its text..")
        
    return articles_texts


def scroll_down(driver):
    #scroll to the end to load max of articles
    driver.execute_script("window.scrollTo(0, 2450)")
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'load-more'))).click()


def get_titles_urls(driver, url, articles_urls, articles_titles, articles_tags):
    driver.get(url)
    accept_cookies(driver)

    try:
        for i in range(5):
            scroll_down(driver)
    except:
        pass
    
    try:
        search_results = driver.find_elements_by_class_name('tag-items')
        for result in search_results:
            urls = result.find_elements_by_css_selector('a')
            titles = result.find_elements_by_class_name('dm-tag-title')
            tags = result.find_elements_by_class_name('dm-tag-tag')

            [articles_urls.append(item.get_attribute('href')) for item in urls]
            [articles_titles.append(item.text) for item in titles]
            [articles_tags.append(item.text) for item in tags]
    except:
        print(f"There is a problem to get articles with this url : {url}.")

    return articles_urls, articles_titles, articles_tags

    
def get_categories_pages(driver):
    categories_urls = []
    search_results = driver.find_elements_by_id('block-menu-menu-categories')
    for result in search_results:
        elements = result.find_elements_by_css_selector('a')
        for element in elements:
            categories_urls.append(element.get_attribute('href'))

    return categories_urls


def main():
    #driver's instance
    driver = '/home/anna/Documents/M2/TechWeb/geckodriver'
    driver = webdriver.Firefox(executable_path=driver)
    driver.get("https://www.cnews.fr/")

    accept_cookies(driver)

    categories_urls = get_categories_pages(driver)
    #categories_urls = {'https://www.cnews.fr/france'}

    articles_urls = []
    articles_titles = []
    articles_tags = []
    articles_texts = []
    for url in categories_urls:
        articles_urls, articles_titles, articles_tags = get_titles_urls(driver, url, articles_urls, articles_titles, articles_tags)

    #print(articles_urls, articles_titles, articles_tags)

    for articles_url in articles_urls:
        articles_texts = get_article_text(driver, articles_url, articles_texts)

    #print(articles_texts)

    with open("Cnew_artciles.csv", "a") as fic:
        fic_writer = csv.writer(fic, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fic_writer.writerow(['Domaine', 'Title', 'Text', 'Tag', 'URL'])
        for title, text, tag, url in zip(articles_titles, articles_texts, articles_tags, articles_urls):
            name_domain = str(url).split('/')[3]
            fic_writer.writerow([name_domain, title, text, tag, url])


if __name__ == "__main__":
    main()