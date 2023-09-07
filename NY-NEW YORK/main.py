from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\NY-NEW YORK'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})
# Opening browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "http://a836-acris.nyc.gov/CP/"
browser.get(url)
browser.maximize_window()

# property records
time.sleep(4)
property_records = browser.find_element(By.XPATH, "//font[contains(text(),'Search Property Records')]").click()

# document type
time.sleep(3)
doc_type = browser.find_element(By.XPATH, "//font[contains(text(),'Document Type')]").click()

# selecting document type
time.sleep(4)
instruments = Select(browser.find_element(By.XPATH, "//select[@name='combox_doc_narrow']"))
instruments.select_by_visible_text("MORTGAGES & INSTRUMENTS")

time.sleep(2)
mortgage = Select(browser.find_element(By.XPATH, "//select[@name='combox_doc_doctype']"))
mortgage.select_by_visible_text("MORTGAGE")

# selecting date range
time.sleep(2)
date_range = Select(browser.find_element(By.XPATH, "//select[@name='cmb_date']"))
date_range.select_by_visible_text("Specific Date Range")

# from date
time.sleep(1)
month = browser.find_element(By.XPATH, "//input[@name='edt_fromm']").send_keys('08')
time.sleep(1)
date = browser.find_element(By.XPATH, "//input[@name='edt_fromd']").send_keys('08')
time.sleep(1)
year = browser.find_element(By.XPATH, "//input[@name='edt_fromy']").send_keys('2017')
time.sleep(1)

# to date

month = browser.find_element(By.XPATH, "//input[@name='edt_tom']").send_keys('08')
time.sleep(1)
date = browser.find_element(By.XPATH, "//input[@name='edt_tod']").send_keys('08')
time.sleep(1)
year = browser.find_element(By.XPATH, "//input[@name='edt_toy']").send_keys('2017')

time.sleep(2)
borough = Select(browser.find_element(By.XPATH, "//select[@name='borough']"))
borough.select_by_visible_text("MANHATTAN / NEW YORK")

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//input[@value='Search']").click()
time.sleep(4)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//form[@name='DATA']/table/tbody"))
    total_pages += element_count

    max_rows = Select(browser.find_element(By.XPATH, "//select[@name='com_maxrows']"))
    max_rows.select_by_visible_text('99')
    time.sleep(4)

    ids = browser.find_elements(By.XPATH, "//form[@name='DATA']/table/tbody/tr[2]/td/table/tbody/tr")
    a = []
    for doc in ids:
        if doc in browser.find_elements(By.XPATH, "//form[@name='DATA']/table/tbody/tr[2]/td/table/tbody/tr[1]"):
            del doc
        else:
            a.append(doc)
    total += len(a)

    for i in range(len(a)):
        img = browser.find_element(By.XPATH,
                                   f"//form[@name='DATA']/table/tbody/tr[2]/td/table/tbody/tr[{i + 2}]/td/div/font/input[2]")
        img.click()
        time.sleep(4)
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@name='mainframe']"))
        save = browser.find_element(By.XPATH, "//div[@class='vtm_toolbar']/table/tbody/tr/td[13]").click()
        time.sleep(1)
        ok = browser.find_element(By.XPATH, "//span[contains(text(),'OK')]").click()
        time.sleep(23)
        browser.switch_to.default_content
        browser.back()
        time.sleep(3)

    print('Successfully downloaded', len(a), 'documents in page', p)

    time.sleep(5)
    try:
        next_button = browser.find_element(By.LINK_TEXT, "next")
        next_button.click()
    except Exception as e:
        break

    time.sleep(3)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

### DEED

# edit
time.sleep(2)
edit = browser.find_element(By.XPATH, "//form[@name='DATA']/table/tbody/tr/td/font/font[3]/a[3]/font").click()

# selecting document type
time.sleep(5)
instruments = Select(browser.find_element(By.XPATH, "//select[@name='combox_doc_narrow']"))
instruments.select_by_visible_text("DEEDS AND OTHER CONVEYANCES")

time.sleep(3)
deed = Select(browser.find_element(By.XPATH, "//select[@name='combox_doc_doctype']"))
deed.select_by_visible_text("DEED")

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//input[@value='Search']").click()
time.sleep(3)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//form[@name='DATA']/table/tbody"))
    total_pages += element_count

    max_rows = Select(browser.find_element(By.XPATH, "//select[@name='com_maxrows']"))
    max_rows.select_by_visible_text('99')
    time.sleep(4)

    ids = browser.find_elements(By.XPATH, "//form[@name='DATA']/table/tbody/tr[2]/td/table/tbody/tr")
    a = []
    for doc in ids:
        if doc in browser.find_elements(By.XPATH, "//form[@name='DATA']/table/tbody/tr[2]/td/table/tbody/tr[1]"):
            del doc
        else:
            a.append(doc)
    total += len(a)

    for i in range(len(a)):
        img = browser.find_element(By.XPATH,
                                   f"//form[@name='DATA']/table/tbody/tr[2]/td/table/tbody/tr[{i + 2}]/td/div/font/input[2]")
        img.click()
        time.sleep(4)
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@name='mainframe']"))
        save = browser.find_element(By.XPATH, "//div[@class='vtm_toolbar']/table/tbody/tr/td[13]").click()
        time.sleep(1)
        ok = browser.find_element(By.XPATH, "//span[contains(text(),'OK')]").click()
        time.sleep(23)
        browser.switch_to.default_content
        browser.back()
        time.sleep(3)

    print('Successfully downloaded', len(a), 'documents in page', p)

    time.sleep(5)
    try:
        next_button = browser.find_element(By.LINK_TEXT, "next")
        next_button.click()
    except Exception as e:
        break

    time.sleep(3)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()