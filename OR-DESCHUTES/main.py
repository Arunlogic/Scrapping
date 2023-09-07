from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\OR-DESCHUTES'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "https://recordings.deschutes.org/DigitalResearchRoom/"
browser.get(url)
browser.maximize_window()

# advance search
time.sleep(4)
advance = browser.find_element(By.XPATH, '//button[@title="Go to Advanced search page"]').click()

time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//input[@id='Criteria_Filter_RecordingDateStart']")
start_date = '01/18/2023'
time.sleep(2)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH, "//input[@id='Criteria_Filter_RecordingDateEnd']")
end_date = '01/18/2023'
time.sleep(2)
input_end_date.send_keys(end_date)

# document type
time.sleep(3)
mortgage = Select(browser.find_element(By.XPATH, "//select[@id='Filter_DocumentType']"))
mortgage.select_by_visible_text('MORTGAGE')

time.sleep(3)
search = browser.find_element(By.XPATH, "//button[@id='adv-search-btn']").click()
time.sleep(4)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0

while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='container body-content']/div[4]"))
    total_pages += element_count
    show = browser.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[4]/div[3]/div[3]/form/button").click()
    time.sleep(5)
    ids = browser.find_elements(By.XPATH, "//div[@class='container body-content']/div[4]/div/div[1]/div[1]/span/a/span")
    print(len(ids))
    total = total + len(ids)

    for img in ids:
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        time.sleep(6)

    print('Successfully downloaded', len(ids), 'documents in page', p)
    time.sleep(5)
    browser.execute_script("window.scrollBy(0,210)", "")
    try:
        next_button = browser.find_element(By.XPATH, "/html/body/div[4]/div[6]/div[3]/div[2]/form/button")
        next_button.click()
        time.sleep(6)
    except Exception as e:
        break

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

### DEED

time.sleep(3)
new_search = browser.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[4]/div[1]/span[2]/a").click()

time.sleep(5)
input_start_date = browser.find_element(By.XPATH, "//input[@id='Criteria_Filter_RecordingDateStart']")
start_date = '01/18/2023'
time.sleep(2)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH, "//input[@id='Criteria_Filter_RecordingDateEnd']")
end_date = '01/18/2023'
time.sleep(2)
input_end_date.send_keys(end_date)

# document type
time.sleep(3)
mortgage = Select(browser.find_element(By.XPATH, "//select[@id='Filter_DocumentType']"))
mortgage.select_by_visible_text('DEED')

time.sleep(3)
search = browser.find_element(By.XPATH, "//button[@id='adv-search-btn']").click()
time.sleep(4)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0

while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='container body-content']/div[4]"))
    total_pages += element_count
    show = browser.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[4]/div[3]/div[3]/form/button").click()
    time.sleep(5)
    ids = browser.find_elements(By.XPATH, "//div[@class='container body-content']/div[4]/div/div[1]/div[1]/span/a/span")
    print(len(ids))
    total = total + len(ids)

    for img in ids:
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        time.sleep(6)

    print('Successfully downloaded', len(ids), 'documents in page', p)
    time.sleep(5)
    browser.execute_script("window.scrollBy(0,210)", "")
    try:
        next_button = browser.find_element(By.XPATH, "/html/body/div[4]/div[6]/div[3]/div[2]/form/button")
        next_button.click()
        time.sleep(6)
    except Exception as e:
        break

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()