from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pyao

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\TX-EL PASO'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "https://apps.epcounty.com/publicrecords/OfficialPublicRecords"
browser.get(url)
browser.maximize_window()

# Selecting document type
time.sleep(4)
document = Select(browser.find_element(By.XPATH, "//select[@id='StyleID']"))
document.select_by_visible_text('DOT - DEED OF TRUST')

time.sleep(2)
start_date = '09/20/2022'
input_start_date = browser.find_element(By.XPATH, "//input[@id='InstrumentDateFrom']")
time.sleep(2)
input_start_date.send_keys(start_date)

time.sleep(2)
end_date = '09/20/2022'
input_end_date = browser.find_element(By.XPATH, "//input[@id='InstrumentDateTo']")
time.sleep(2)
input_end_date.send_keys(end_date)

time.sleep(2)
search = browser.find_element(By.XPATH, "//input[@id='submit']")
search.click()
time.sleep(8)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0

while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@id='page-container']/table/tbody"))
    total_pages += element_count
    ids = browser.find_elements(By.XPATH, "//div[@id='page-container']/table/tbody/tr/td[11]/a/i")
    print(len(ids))
    total = total + len(ids)

    for img in ids:
        parent_handle = browser.current_window_handle
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        time.sleep(20)
        all_handles = browser.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                browser.switch_to.window(handle)
                time.sleep(2)
                browser.close()
        browser.switch_to.window(parent_handle)
        time.sleep(2)

    print('Successfully downloaded', len(ids), 'documents in page', p)
    time.sleep(3)
    try:
        next_button = browser.find_element(By.XPATH, "//li[@class='PagedList-skipToNext']/a").click()
    except Exception as e:
        break
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

### DEED

# new search
search = browser.find_element(By.XPATH, "//div[@class='float-right']/a").click()
time.sleep(10)

# Selecting document type
document = Select(browser.find_element(By.XPATH, "//select[@id='StyleID']"))
document.select_by_visible_text('WAD - WARRANTY DEED')

time.sleep(2)
start_date = '09/20/2022'
input_start_date = browser.find_element(By.XPATH, "//input[@id='InstrumentDateFrom']")
time.sleep(2)
input_start_date.send_keys(start_date)

time.sleep(2)
end_date = '09/20/2022'
input_end_date = browser.find_element(By.XPATH, "//input[@id='InstrumentDateTo']")
time.sleep(2)
input_end_date.send_keys(end_date)

time.sleep(2)
search = browser.find_element(By.XPATH, "//input[@id='submit']")
search.click()
time.sleep(8)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0

while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@id='page-container']/table/tbody"))
    total_pages += element_count
    ids = browser.find_elements(By.XPATH, "//div[@id='page-container']/table/tbody/tr/td[11]/a/i")
    print(len(ids))
    total = total + len(ids)

    for img in ids:
        parent_handle = browser.current_window_handle
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        time.sleep(20)
        all_handles = browser.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                browser.switch_to.window(handle)
                time.sleep(2)
                browser.close()
        browser.switch_to.window(parent_handle)
        time.sleep(2)

    print('Successfully downloaded', len(ids), 'documents in page', p)
    time.sleep(3)
    try:
        next_button = browser.find_element(By.XPATH, "//li[@class='PagedList-skipToNext']/a").click()
    except Exception as e:
        break
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()