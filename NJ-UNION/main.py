# Importing required libraries
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.firefox.options import Options
import pyautogui as pyao

path = 'C://IonIdea//Firefox web driver//firefox_geckodriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\NJ - UNION'

firefox_options = Options()
firefox_options.set_preference('pdfjs.disabled', True)
firefox_options.set_preference('browser.download.folderList', 1)
firefox_options.set_preference('browser.download.manager.showWhenStarting', False)
firefox_options.set_preference('browser.download.dir', path_to_save_pdf)


service = webdriver.firefox.service.Service(executable_path=path)
browser = webdriver.Firefox(service=service, options=firefox_options)

# Getting page
url = 'http://clerk.ucnj.org/UCPA/DocIndex?s=join'
browser.get(url)
browser.maximize_window()

# Clicking date range search
time.sleep(5)
date_range_search = browser.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr/td/font[1]/a[3]")
date_range_search.click()

# Seleting document type
time.sleep(5)
select_document_type = Select(browser.find_element(By.XPATH,"//select[@name='dt']"))
select_document_type.select_by_visible_text('Mortgage')

# input date
date_from = browser.find_element(By.XPATH,"//input[@name='from']")
date_to = browser.find_element(By.XPATH,"//input[@name='to']")

# start_date = dt.date.today().strftime('%m/%d/%Y')
# end_date = dt.date.today().strftime('%m/%d/%Y')
start_date = '07/31/2019'
end_date = '07/31/2019'
time.sleep(3)
date_from.send_keys(start_date)
time.sleep(5)
date_to.send_keys(end_date)

# Clicking search
time.sleep(3)
search_button = browser.find_element(By.XPATH,"//input[@value='Search']")
search_button.click()
time.sleep(4)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//*[@id='main']/table[2]/tbody/tr/td"))
    total_pages += element_count

    name = []
    form = browser.find_elements(By.TAG_NAME, 'a')
    for c in form:
        name.append(c.text)

    names = []
    for n in name:
        if n.isupper():
            names.append(n)
        else:
            del n
    print('Total Documents in page', p, ':', len(names))
    print(names)

    total = total + len(names)

    for i in range(len(names)):
        click_name = browser.find_element(By.LINK_TEXT,names[i])
        click_name.click()
        time.sleep(4)
        click_view_image = browser.find_element(By.XPATH,"//img[@title='View PDF document']")
        click_view_image.click()
        time.sleep(12)
        pyao.press('esc')
        for b in range(3):
            time.sleep(2)
            browser.back()
        time.sleep(2)

    print('Successfully downloaded', len(names), 'documents in page', p)

    if not browser.find_elements(By.LINK_TEXT, 'Next'):
        break

    time.sleep(5)
    browser.find_element(By.LINK_TEXT, 'Next').click()

print('Total Pages: ', total_pages)
print('Total viewed documents:', total)

# DEED
'''
time.sleep(5)
for p in range(total_pages-1):
    browser.back()
    time.sleep(3)

time.sleep(3)
browser.back()
time.sleep(6)

select_document_type = Select(browser.find_element(By.XPATH,"//select[@name='dt']"))
select_document_type.select_by_visible_text('Deed')

time.sleep(3)
search_button = browser.find_element(By.XPATH,"//input[@value='Search']")
search_button.click()
time.sleep(4)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//*[@id='main']/table[2]/tbody/tr/td"))
    total_pages += element_count

    name = []
    form = browser.find_elements(By.TAG_NAME, 'a')
    for c in form:
        name.append(c.text)

    names = []
    for n in name:
        if n.isupper():
            names.append(n)
        else:
            del n
    print('Total Documents in page', p, ':', len(names))
    print(names)

    total = total + len(names)

    for i in range(len(names)):
        click_name = browser.find_element(By.LINK_TEXT,names[i])
        click_name.click()
        time.sleep(4)
        click_view_image = browser.find_element(By.XPATH,"//img[@title='View PDF document']")
        click_view_image.click()
        time.sleep(12)
        pyao.press('esc')
        for b in range(3):
            time.sleep(2)
            browser.back()
        time.sleep(2)

    print('Successfully downloaded', len(names), 'documents in page', p)

    if not browser.find_elements(By.LINK_TEXT, 'Next'):
        break

    time.sleep(5)
    browser.find_element(By.LINK_TEXT, 'Next').click()

print('Total Pages: ', total_pages)
print('Total viewed documents:', total)
'''
browser.quit()