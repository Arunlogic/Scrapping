# Importing required libraries
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\OH-CUYAHOGA'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

# Opening browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

# Getting page
url = "https://cuyahoga.oh.publicsearch.us/search/advanced"
browser.get(url)
browser.maximize_window()

# Sign in
time.sleep(5)
sign_in = browser.find_element(By.XPATH,"//a[contains(text(),'Sign In')]")  #user name = ganisolo@superrito.com & password - Delete123
sign_in.click()
time.sleep(50)
submit = browser.find_element(By.XPATH,"//button[@class='user-form__submit-button user-form__button']")
submit.click()
time.sleep(10)

# From date
time.sleep(5)
start_date = '09/20/2022'
input_start_date = browser.find_element(By.XPATH,"//input[@id='recordedDateRange']")
time.sleep(3)
input_start_date.send_keys(Keys.CONTROL, 'a')
time.sleep(4)
input_start_date.send_keys(Keys.BACKSPACE)
time.sleep(4)
input_start_date.send_keys(start_date)

# To date
time.sleep(3)
end_date = '09/20/2022'
input_end_date = browser.find_element(By.XPATH,"//input[@aria-label='end date']")
time.sleep(3)
input_end_date.send_keys(Keys.CONTROL, 'a')
time.sleep(4)
input_end_date.send_keys(Keys.BACKSPACE)
time.sleep(4)
input_end_date.send_keys(end_date)
time.sleep(3)
click_somewhere = browser.find_element(By.XPATH,"//input[@id='parcel']").click()

# Selecting document type
time.sleep(5)
document = browser.find_element(By.XPATH,"//input[@id='docTypes-input']").click()
time.sleep(5)
sending = browser.find_element(By.XPATH,"//input[@id='docTypes-input']").send_keys('MORTGAGE')
time.sleep(5)

mort = browser.find_elements(By.XPATH,"//div[@class='checkbox__controls']")
#mort = browser.find_element(By.XPATH,"//input[@name='MORTGAGE'][@type='checkbox']")
time.sleep(3)
length = 0
for m in mort:
    length+=1
    if length ==1:
        m.click()
        break
    time.sleep(3)
print('Successfully clicked the document type')

# Search
time.sleep(5)
browser.execute_script("window.scrollBy(0,600)","")
time.sleep(3)
search = browser.find_element(By.XPATH,"//button[@class='css-1aabfxg']")
search.click()
time.sleep(15)

# Counting the total pages & Counting the total documents & How much documents it's downloaded
total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='a11y-table']"))
    total_pages += element_count

    document_number = []
    ids = browser.find_elements(By.XPATH, "//td[@class='col-7']")
    for d in ids:
        document_number.append(d.text)
    print(document_number)
    total = total + len(document_number)

    for i in range(len(document_number)):
        view = browser.find_element(By.XPATH,"//span[contains(text(),'"+document_number[i]+"')]")
        view.click()
        time.sleep(8)
        download = browser.find_element(By.XPATH, "//button[contains(text(),'Download')]")
        download.click()
        time.sleep(15)
        browser.back()
        time.sleep(10)

    print('Successfully downloaded', len(document_number), 'documents in page', p)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

    try:
        next_button = browser.find_element(By.XPATH,"//button[@class='pagination__page-jump'][@aria-label='next page']")
        time.sleep(5)
        next_button.click()
    except Exception as e:
        break
    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

for p in range(total_pages):
    browser.back()
    time.sleep(8)

# Deed
time.sleep(5)
browser.execute_script("window.scrollBy(0,-300)","")
time.sleep(5)
removing_type = browser.find_element(By.XPATH,"//button[@class='react-tokenized-select__remove-button']")
removing_type.click()

# Selecting document type

time.sleep(5)
document = browser.find_element(By.XPATH,"//input[@id='docTypes-input']").click()
time.sleep(5)
sending = browser.find_element(By.XPATH,"//input[@id='docTypes-input']").send_keys('DEED')
time.sleep(5)

mort = browser.find_elements(By.XPATH,"//div[@class='checkbox__controls']")
#mort = browser.find_element(By.XPATH,"//input[@name='MORTGAGE'][@type='checkbox']")
time.sleep(3)
length = 0
for m in mort:
    length+=1
    if length ==1:
        m.click()
        break
    time.sleep(3)
print('Successfully clicked DEED')

# Search
time.sleep(5)
browser.execute_script("window.scrollBy(0,600)","")
time.sleep(3)
search = browser.find_element(By.XPATH,"//button[@class='css-1aabfxg']")
search.click()
time.sleep(15)

# To download
total_pages = 0
total = 0
p = 0
while True:
    time.sleep(15)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='a11y-table']"))
    total_pages += element_count

    links = browser.find_elements(By.XPATH, "//td[@class='col-7']")
    hrefs = []
    for c in links:
        hrefs.append(c.text)
    print(hrefs)
    total = total + len(hrefs)

    for i in range(len(hrefs)):
        doc_no = browser.find_element(By.XPATH, "//span[contains(text(),'" + hrefs[i] + "')]")
        doc_no.click()
        time.sleep(15)
        download = browser.find_element(By.XPATH, "//button[contains(text(),'Download')]")
        download.click()
        time.sleep(20)
        browser.back()
        time.sleep(8)

    print('Successfully downloaded', len(hrefs), 'documents in page', p)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

    try:
        next_button = browser.find_element(By.XPATH,"//button[@class='pagination__page-jump'][@aria-label='next page']")
        time.sleep(5)
        next_button.click()
    except Exception as e:
        break
    time.sleep(10)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()
