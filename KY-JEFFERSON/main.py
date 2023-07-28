# Importing required libraries
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
import datetime as dt

# Chrome driver path
path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\KY - JEFFERSON'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)
url = 'https://search.jeffersondeeds.com/insttype.php'
browser.get(url)
browser.maximize_window()

time.sleep(5)
instrument_type1 = Select(browser.find_element(By.XPATH, "//select[@name='itype1' ]"))
instrument_type1.select_by_visible_text("MORTGAGE")

time.sleep(3)
instrument_type2 = Select(browser.find_element(By.XPATH, "//select[@name='itype2' ]"))
instrument_type2.select_by_visible_text("MTG ELEC REGIST")

input_start_date = browser.find_element(By.XPATH,"//input[@id='datepickerbdate']")
input_start_date.clear()
start_date = '06/26/2023' #dt.date.today().strftime('%m/%d/%Y')
time.sleep(3)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH,"//input[@id='datepickeredate']")
input_end_date.clear()
end_date = '06/26/2023'  #dt.date.today().strftime('%m/%d/%Y')
time.sleep(3)
input_end_date.send_keys(end_date)

# Click to search DEED records
time.sleep(3)
search_button = browser.find_element(By.XPATH,"//input[@value='Execute Search']")
search_button.click()
time.sleep(7)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p+1
    print('Scrapping page:',p)
    element_count = len(browser.find_elements(By.XPATH, '/html/body/table[3]/tbody'))
    total_pages += element_count
    try:
        links = browser.find_elements(By.XPATH,"//a[@name='view']")
        hrefs = []
        for c in links:
            hrefs.append(c.text)
        print('Total Documents:',len(hrefs))
        total = total+len(hrefs)
        for element in links:
            element.click()
            time.sleep(10)
        print('Successfully downloaded',len(hrefs),'documents in page',p)
    except Exception as e:
        break
    time.sleep(6)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if not browser.find_elements(By.LINK_TEXT,'Next'):
        break
    time.sleep(3)
    browser.find_element(By.LINK_TEXT,'Next').click()
    time.sleep(5)
print('Total Pages: ',total_pages)
print('Total downloaded documents:',total)

# DEED

time.sleep(10)
back_to_search = browser.find_element(By.XPATH,"//input[@id='home']").click()

time.sleep(5)
instrument_type1 = Select(browser.find_element(By.XPATH, "//select[@name='itype1' ]"))
instrument_type1.select_by_visible_text("DEED")

time.sleep(3)
instrument_type2 = Select(browser.find_element(By.XPATH, "//select[@name='itype2' ]"))
instrument_type2.select_by_visible_text("DEED W/VENDLIEN")

input_start_date = browser.find_element(By.XPATH,"//input[@id='datepickerbdate']")
input_start_date.clear()
start_date = '06/26/2023' #dt.date.today().strftime('%m/%d/%Y')
time.sleep(3)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH,"//input[@id='datepickeredate']")
input_end_date.clear()
end_date = '06/26/2023'  #dt.date.today().strftime('%m/%d/%Y')
time.sleep(3)
input_end_date.send_keys(end_date)

time.sleep(3)
search_button = browser.find_element(By.XPATH,"//input[@value='Execute Search']")
search_button.click()
time.sleep(7)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p+1
    print('Scrapping page:',p)
    element_count = len(browser.find_elements(By.XPATH, '/html/body/table[3]/tbody'))
    total_pages += element_count
    try:
        links = browser.find_elements(By.XPATH,"//a[@name='view']")
        hrefs = []
        for c in links:
            hrefs.append(c.text)
        print('Total Documents:',len(hrefs))
        total = total+len(hrefs)
        for element in links:
            element.click()
            time.sleep(10)
        print('Successfully downloaded',len(hrefs),'documents in page',p)
    except Exception as e:
        break
    time.sleep(6)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if not browser.find_elements(By.LINK_TEXT,'Next'):
        break
    time.sleep(3)
    browser.find_element(By.LINK_TEXT,'Next').click()
    time.sleep(5)
print('Total Pages: ',total_pages)
print('Total downloaded documents:',total)

browser.quit()