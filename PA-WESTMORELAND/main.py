from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\PA-WESTMORELAND'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "http://www.wcdeeds.us/paxworld/"
browser.get(url)
browser.maximize_window()

# Accept
time.sleep(4)
click_accept = browser.find_element(By.ID, "disclaimerAgreement")
click_accept.click()

# Advanced legal
time.sleep(4)
advanced = browser.find_element(By.ID, "btnCriteriaAdvancedNameSearch").click()

time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//input[@id='dtFrom']")
start_date = '01/18/2023'
time.sleep(3)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH, "//input[@id='dtTo']")
end_date = '01/18/2023'
time.sleep(3)
input_end_date.send_keys(end_date)

# selecting document types
time.sleep(3)
doc_types_drop_down = browser.find_element(By.XPATH, "//div[@id='jstreeCatDocTypes']/ul/li[4]/i").click()
time.sleep(3)
mortgage = browser.find_element(By.XPATH, "//div[@id='jstreeCatDocTypes']/ul/li[4]/ul/li[1]/a/i[1]").click()
time.sleep(3)
mortgage_1 = browser.find_element(By.XPATH, "//div[@id='jstreeCatDocTypes']/ul/li[4]/ul/li[5]/a/i[1]").click()
time.sleep(3)
mortgage_2 = browser.find_element(By.XPATH, "//div[@id='jstreeCatDocTypes']/ul/li[4]/ul/li[13]/a/i[1]").click()

# details search
time.sleep(3)
search = browser.find_element(By.ID, "btnDetailSearch").click()
time.sleep(6)
minimize = browser.find_element(By.XPATH, "//button[@id='btnCriteria']/span").click()
time.sleep(3)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
n = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='gridResultsDetailOnly']/tbody"))
    total_pages += element_count
    time.sleep(2)
    a = []
    doc_no = browser.find_elements(By.XPATH,
                                   "//table[@id='gridResultsDetailOnly']/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/span[1]")
    for e in doc_no:
        a.append(e.text)
    print(len(a))
    print(a)
    images = browser.find_elements(By.XPATH,
                                   "//table[@id='gridResultsDetailOnly']/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/span[1]/a")
    total = total + len(images)

    for img in images:
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        time.sleep(10)
        save = browser.find_element(By.XPATH, "//li[@id='liSaveImage']/a/span").click()
        time.sleep(8)

    print('Successfully downloaded', len(images), 'documents in page', p)
    time.sleep(3)
    n += 1
    try:
        total_count_pages = browser.find_element(By.XPATH, "//div[@id='gridResultsDetailOnly_paginate']/span[2]").text
        words = total_count_pages.split()
        for word in words:
            if word.isdigit():
                a = int(word)
        if n < a:
            next_button = browser.find_element(By.XPATH,
                                               "//div[@id='gridResultsDetailOnly_paginate']/button[2]").click()
            time.sleep(4)
        else:
            break
    except Exception as e:
        break

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

### DEED

time.sleep(4)
minimize = browser.find_element(By.XPATH, "//button[@id='btnCriteria']/span").click()
time.sleep(3)

# deselecting document types
mortgage = browser.find_element(By.XPATH, "//div[@id='jstreeCatDocTypes']/ul/li[4]/ul/li[1]/a/i[1]").click()
time.sleep(3)
mortgage_1 = browser.find_element(By.XPATH, "//div[@id='jstreeCatDocTypes']/ul/li[4]/ul/li[5]/a/i[1]").click()
time.sleep(3)
mortgage_2 = browser.find_element(By.XPATH, "//div[@id='jstreeCatDocTypes']/ul/li[4]/ul/li[13]/a/i[1]").click()
time.sleep(3)
doc_types_drop_down = browser.find_element(By.XPATH, "//div[@id='jstreeCatDocTypes']/ul/li[4]/i").click()

# seecting deed document type
time.sleep(3)
doc_types_drop_down = browser.find_element(By.XPATH, "//div[@id='jstreeCatDocTypes']/ul/li[1]/i").click()
time.sleep(3)
deed = browser.find_element(By.XPATH, "//div[@id='jstreeCatDocTypes']/ul/li[1]/ul/li[10]/a/i[1]").click()
time.sleep(3)

# details search
time.sleep(3)
search = browser.find_element(By.ID, "btnDetailSearch").click()
time.sleep(6)
minimize = browser.find_element(By.XPATH, "//button[@id='btnCriteria']/span").click()
time.sleep(3)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
n = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='gridResultsDetailOnly']/tbody"))
    total_pages += element_count
    time.sleep(2)
    a = []
    doc_no = browser.find_elements(By.XPATH,
                                   "//table[@id='gridResultsDetailOnly']/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/span[1]")
    for e in doc_no:
        a.append(e.text)
    print(len(a))
    print(a)
    images = browser.find_elements(By.XPATH,
                                   "//table[@id='gridResultsDetailOnly']/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/span[1]/a")
    total = total + len(images)

    for img in images:
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        time.sleep(10)
        save = browser.find_element(By.XPATH, "//li[@id='liSaveImage']/a/span").click()
        time.sleep(8)

    print('Successfully downloaded', len(images), 'documents in page', p)
    time.sleep(3)
    n += 1
    try:
        total_count_pages = browser.find_element(By.XPATH, "//div[@id='gridResultsDetailOnly_paginate']/span[2]").text
        words = total_count_pages.split()
        for word in words:
            if word.isdigit():
                a = int(word)
        if n < a:
            next_button = browser.find_element(By.XPATH,
                                               "//div[@id='gridResultsDetailOnly_paginate']/button[2]").click()
            time.sleep(4)
        else:
            break
    except Exception as e:
        break

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()