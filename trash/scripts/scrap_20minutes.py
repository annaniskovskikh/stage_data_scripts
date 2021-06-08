# -*- coding: utf-8 -*-

import sys
import time
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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


def main():
    #driver's instance
    driver = '/home/anna/Documents/M2/TechWeb/geckodriver'
    driver = webdriver.Firefox(executable_path=driver)

    driver.get(f"https://www.20minutes.fr/")

    accept_cookies(driver)
    refuse_notifications(driver)

    #get domains sub-elements
    search_results = driver.find_elements_by_class_name('header-nav-list')

    """with open("20minutes_domaines_urls.csv", "a") as fic:
        fic_writer = csv.writer(fic, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fic_writer.writerow(['Domaine', 'Sous-domaine', 'URL'])  """

    for result in search_results:
        elements = result.find_elements_by_css_selector('a')
        for element in elements:
            if "annonces-legales" not in str(element.get_attribute('href')):
                #fic_writer.writerow([domain, element.text, element.get_attribute('href')])
                #print(element.text, element.get_attribute('href'))
                driver.get(element.get_attribute('href'))
                rslts = driver.find_elements_by_class_name('teaser ')
                for rslt in rslts:
                    titles = rslt.find_element_by_class_name('teaser-title')
                    print(f"TITLE : {titles.text}")
                    summary = titles.find_elements_by_class_name('teaser-summary')
                    for sum in summary:
                        print(f"SUMMARY : {sum.text}")

    #extract_domain_urls_csv(driver, domain, fic_writer)


if __name__ == "__main__":
    main()