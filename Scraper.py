from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")


#MONSTER

driver.get("https://www.monster.com/jobs/search/?q=Implementation&where=united-states")
driver.find_element_by_link_text("Load more jobs").click()
driver.find_element_by_link_text("Load more jobs").click()
driver.find_element_by_link_text("Load more jobs").click()
driver.find_element_by_link_text("Load more jobs").click()
driver.find_element_by_link_text("Load more jobs").click()
driver.find_element_by_link_text("Load more jobs").click()
driver.find_element_by_link_text("Load more jobs").click()
driver.find_element_by_link_text("Load more jobs").click()

time.sleep(15)

all_jobs = driver.find_elements_by_class_name('summary')

for job in all_jobs:
 print(job.text)

driver.get("localhost:8080/job/Monster%20Job%20Scraper/build?token=1234567891")



