# Importing required libraries

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
import datetime as dt

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\PA - CHESTER'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)
url = 'https://chesterpa.countygovernmentrecords.com/ChesterRecorder/web/splash.jsp'
browser.get(url)
browser.maximize_window()

# Acknowledge
time.sleep(5)
click_accept = browser.find_element(By.XPATH,"//input[@value='I Acknowledge']")
click_accept.click()
time.sleep(5)

# Log in as public-user
public_login = browser.find_element(By.XPATH,"//input[@value='Public Login']")
public_login.click()
time.sleep(5)

# Under Recording
input_start_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDStart']")  #name="RecordingDateIDStart"
time.sleep(3)
input_start_date.clear()
start_date = '08/02/2017' #dt.date.today().strftime('%m/%d/%Y')
time.sleep(3)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDEnd']")
time.sleep(3)
input_end_date.clear()
end_date = '08/02/2017' #dt.date.today().strftime('%m/%d/%Y')
time.sleep(4)
input_end_date.send_keys(end_date)

# To Uncheck box to Search Specific Document Types
check_box = browser.find_element(By.XPATH,"//input[@name='AllDocuments']")
time.sleep(2)
check_box.click()
time.sleep(2)
# Replace the number of times you want to scroll

for i in range(3):
    drop_down = browser.find_element(By.XPATH,"//select[@name='__search_select']")     # Scroll to the end of the page
    time.sleep(2)                                                                # it will take 2 seconds to load more records

element = Select(drop_down)
time.sleep(4)
element.select_by_visible_text('Mortgage')
time.sleep(4)
element.select_by_visible_text('Re-Recorded Mortgage')

# Click to search Mortgage records
search_button = browser.find_element(By.XPATH,"//input[@class='search']")
search_button.click()
time.sleep(2)

# Counting the total pages & Counting the total documents & How much documents it's downloaded
total_pages = 0
Total_Documents = []
total = 0
p = 0
while True:
    time.sleep(3)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//*[@id='searchResultsTable']"))
    total_pages += element_count

    links = browser.find_elements(By.XPATH, ".//a[contains(text(),'Mortgage')]")
    hrefs = []
    for c in links:
        Total_Documents.append(c)
        hrefs.append(c.text)

    total = total + len(hrefs)
    '''
    for i in range(len(hrefs)):
        click_mortgage_form = browser.find_element(By.LINK_TEXT, hrefs[i])
        click_mortgage_form.click()
        time.sleep(3)
        click_view_image = browser.find_element(By.XPATH, "//a[@class='generator']")
        click_view_image.click()
        time.sleep(20)
        browser.back()
        time.sleep(4)
    print('Successfully downloaded', len(hrefs), 'documents in page', p)
    '''
    if not browser.find_elements(By.LINK_TEXT, 'Next'):
        break

    browser.find_element(By.LINK_TEXT, 'Next').click()
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total DEED Documents: ', len(Total_Documents))
# print(Total_Documents)
print('Total downloaded documents:', total)

# DEED

time.sleep(5)
for p in range(total_pages - 1):
    browser.back()
    time.sleep(3)

time.sleep(3)
browser.back()
time.sleep(5)

input_start_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDStart']")  #name="RecordingDateIDStart"
time.sleep(3)
input_start_date.clear()
start_date = '08/02/2017' #dt.date.today().strftime('%m/%d/%Y')
time.sleep(3)
input_start_date.send_keys(start_date)


input_end_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDEnd']")
time.sleep(3)
input_end_date.clear()
end_date = '08/02/2017' #dt.date.today().strftime('%m/%d/%Y')
time.sleep(4)
input_end_date.send_keys(end_date)

time.sleep(3)
check_box = browser.find_element(By.XPATH,"//input[@name='AllDocuments']")
check_box.click()
time.sleep(4)
check_box.click()

for i in range(3):
    drop_down = browser.find_element(By.XPATH,"//select[@name='__search_select']")     # Scroll to the end of the page
    time.sleep(2)                                                                # it will take 2 seconds to load more records

element = Select(drop_down)
element.deselect_by_visible_text('Mortgage')
time.sleep(4)
element.deselect_by_visible_text('Re-Recorded Mortgage')
time.sleep(4)
element.select_by_visible_text('Deed')
time.sleep(4)
element.select_by_visible_text('Re-Recorded Deed')

time.sleep(5)
search_button = browser.find_element(By.XPATH,"//input[@class='search']")
search_button.click()

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
Total_Documents = []
total = 0
p = 0
while True:
    time.sleep(3)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//*[@id='searchResultsTable']"))
    total_pages += element_count

    links = browser.find_elements(By.XPATH, ".//a[contains(text(),'Deed')]")
    hrefs = []
    for c in links:
        Total_Documents.append(c)
        hrefs.append(c.text)

    total = total + len(hrefs)

    for i in range(len(hrefs)):
        click_mortgage_form = browser.find_element(By.LINK_TEXT,hrefs[i])
        click_mortgage_form.click()
        time.sleep(3)
        click_view_image = browser.find_element(By.XPATH,"//a[@class='generator']")
        click_view_image.click()
        time.sleep(15)
        browser.back()
        time.sleep(4)
    print('Successfully downloaded',len(hrefs),'documents in page',p)

    if not browser.find_elements(By.LINK_TEXT, 'Next'):
        break

    browser.find_element(By.LINK_TEXT, 'Next').click()

print('Total Pages: ', total_pages)
print('Total DEED Documents: ', len(Total_Documents))
# print(Total_Documents)
print('Total downloaded documents:', total)

browser.quit()