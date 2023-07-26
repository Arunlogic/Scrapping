# Importing requiring libraries

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
import datetime as dt

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\WA - WHATCOM'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

# Opening Chrome browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

# Getting county page
time.sleep(3)
url = "http://recording.whatcomcounty.us/Disclaimer"
browser.get(url)
browser.maximize_window()

# Accept
click_accept = browser.find_element(By.XPATH,"//button[@class='btn btn-default']")
time.sleep(5)
click_accept.click()

# Advanced Search
advanced_search = browser.find_element(By.XPATH,"//button[@title='Go to Advanced search page']")
time.sleep(5)
advanced_search.click()

# Recording date
input_start_date = browser.find_element(By.XPATH,"//input[@id='Criteria_Filter_RecordingDateStart']")
input_end_date = browser.find_element(By.XPATH,"//input[@id='Criteria_Filter_RecordingDateEnd']")

start_date = '09/22/2022' #dt.date.today().strftime('%m/%d/%Y')
end_date = '09/22/2022' #dt.date.today().strftime('%m/%d/%Y')
input_start_date.send_keys(start_date)
time.sleep(5)
input_end_date.send_keys(end_date)

# Selecting datatype
time.sleep(4)
dropdown = Select(browser.find_element(By.XPATH,"//select[@id='Filter_DocumentSubtype']"))
dropdown.select_by_visible_text("Deed of Trust")

# Search
search_button = browser.find_element(By.XPATH,"//button[@id='adv-search-btn']")
time.sleep(5)
search_button.click()

# Counting the total pages & Counting the total documents & How much documents it's downloaded
total_pages = 0
Total_Documents = []
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, '/html/body/div[4]/div[4]'))
    total_pages += element_count

    document = browser.find_elements(By.XPATH, "//a[@class='recording-link']")
    hrefs = []
    for c in document:
        Total_Documents.append(c)
        hrefs.append(c.text)

    total = total + len(hrefs)
    '''
    for i in range(len(hrefs)):
        click_mortgage_form = browser.find_element(By.LINK_TEXT, hrefs[i])
        click_mortgage_form.click()
        time.sleep(10)
        view_image = browser.find_element(By.XPATH, "//div[@class='icon-document']")
        view_image.click()
        time.sleep(20)
        browser.back()
        time.sleep(5)
    print('Successfully downloaded', len(hrefs), 'documents in page', p)
    '''
    if not browser.find_elements(By.LINK_TEXT, 'Next'):
        break

    time.sleep(3)
    browser.find_element(By.LINK_TEXT, 'Next').click()

print('Total Pages: ', total_pages)
print('Total Documents:', len(Total_Documents))
print('Total downloaded documents:', total)

# DEED

time.sleep(5)
for p in range(total_pages - 1):
    browser.back()
    time.sleep(3)

time.sleep(3)
browser.back()
time.sleep(5)

# Selecting datatype as Deed
time.sleep(3)
dropdown = Select(browser.find_element(By.XPATH,"//select[@id='Filter_DocumentSubtype']"))
dropdown.select_by_visible_text("Deed")

# Search
time.sleep(5)
search_button = browser.find_element(By.XPATH,"//button[@id='adv-search-btn']")
search_button.click()

# Counting the total pages & Counting the total documents & How much documents it's downloaded
total_pages = 0
Total_Documents = []
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, '/html/body/div[4]/div[4]'))
    total_pages += element_count

    document = browser.find_elements(By.XPATH, "//a[@class='recording-link']")
    hrefs = []
    for c in document:
        Total_Documents.append(c)
        hrefs.append(c.text)

    total = total + len(hrefs)
    for i in range(len(hrefs)):
        click_mortgage_form = browser.find_element(By.LINK_TEXT, hrefs[i])
        click_mortgage_form.click()
        time.sleep(10)
        view_image = browser.find_element(By.XPATH, "//div[@class='icon-document']")
        view_image.click()
        time.sleep(20)
        browser.back()
        time.sleep(5)
    print('Successfully downloaded', len(hrefs), 'documents in page', p)

    if not browser.find_elements(By.LINK_TEXT, 'Next'):
        break

    time.sleep(3)
    browser.find_element(By.LINK_TEXT, 'Next').click()

print('Total Pages: ', total_pages)
print('Total Documents:', len(Total_Documents))
print('Total downloaded documents:', total)

# Quiting from web page
browser.quit()



