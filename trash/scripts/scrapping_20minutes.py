# -*- coding: utf-8 -*-

import sys
import time
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def scroll_for_more_articles(driver):
    #scroll to the middle
    driver.execute_script("window.scrollTo(0, 550)")
    time.sleep(2)

    #load lots of articles
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CLASS_NAME, 'infinite-more'))).click()


def refuse_notifications(driver):
    try:
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'batchsdk-ui-alert__buttons_negative'))).click()
    except:
        print("There is no demand of notifications")

def accept_cookies(driver):
    try:
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'didomi-notice-agree-button'))).click()
    except:
        print("Cookies have been already accepted")


def get_title_summary_url(domain, driver, url_domain):
    driver.get(url_domain)

    refuse_notifications(driver)
    #driver.execute_script("window.scrollTo(0, 1000)")
    #time.sleep(2)
    search_results = driver.find_elements_by_class_name("teaser-title")

    i = 0
    data_articles = []
    for result in search_results:
        i += 1
        print("----------------")
        print(result.find_elements_by_class_name('teaser-title').text)
        """title = result.find_elements_by_class_name('teaser-title').text
        summary = result.find_elements_by_class_name('teaser-summary').text
        subclass = result.find_elements_by_class_name('teaser-headline').text
        article_url_part = result.find_element_by_css_selector('a')
        article_url = f"https://www.20minutes.fr/{domain}{article_url_part}"
        data_articles.append(subclass, i, title, summary, article_url)"""

    #return data_articles


def extract_domain_urls_csv(driver, domain, fic_writer):
    driver.get(f"https://www.20minutes.fr/{domain}")

    accept_cookies(driver)
    refuse_notifications(driver)

    #get domains sub-elements
    search_results = driver.find_elements_by_class_name('subheader-list-item')

    for result in search_results:
        element = result.find_element_by_css_selector('a')
        if "annonces-legales" not in str(element.get_attribute('href')):
            fic_writer.writerow([domain, element.text, element.get_attribute('href')])
            print(domain, element.text, element.get_attribute('href'))


def main():
    #driver's instance
    driver = '/home/anna/Documents/M2/TechWeb/geckodriver'
    driver = webdriver.Firefox(executable_path=driver)

    #domains to scrap
    domains_list = ['actu-generale', 'locales', 'arts-stars', 'sport', \
                    'economie', 'planete', 'insolite', 'societe/desintox', \
                    'hi-tech/by-the-web', 'hi-tech', 'voyage', 'guide-achat', 'actus']

    #domains_list = ['economie']
    with open("20minutes_domaines_urls.csv", "a") as fic:
        fic_writer = csv.writer(fic, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fic_writer.writerow(['Domaine', 'Sous-domaine', 'URL'])  
        for domain in domains_list:
            extract_domain_urls_csv(driver, domain, fic_writer)


if __name__ == "__main__":
    main()