# Importing requiring libraries

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
import datetime as dt

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\GA - MUSCOGEE'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

# Opening Chrome browser
time.sleep(3)
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

# Getting county page
time.sleep(3)
url = "http://er-web.muscogeecourts.com/recorder/web/splash.jsp"
browser.get(url)
browser.maximize_window()

# Accept
time.sleep(5)
click_accept = browser.find_element(By.XPATH,"//input[@value='I Acknowledge']")
click_accept.click()

input_start_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDStart']")
time.sleep(3)
input_start_date.clear()
start_date = '07/24/2019' #dt.date.today().strftime('%m/%d/%Y')
time.sleep(4)
input_start_date.send_keys(start_date)


input_end_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDEnd']")
time.sleep(4)
input_end_date.clear()
end_date = '07/24/2019'  #dt.date.today().strftime('%m/%d/%Y')
time.sleep(5)
input_end_date.send_keys(end_date)

# To Uncheck box to Search Specific Document Types
time.sleep(5)
check_box = browser.find_element(By.XPATH,"//input[@name='AllDocuments']")
check_box.click()

# Selecting dropdown options
time.sleep(5)
drop_down = Select(browser.find_element(By.XPATH,"//select[@name='__search_select']"))
drop_down.select_by_visible_text('SECURITY DEED')

# Search button
time.sleep(8)
search_button = browser.find_element(By.XPATH,"//input[@value='Search']")
search_button.click()
time.sleep(8)

# Counting the total pages & Counting the total documents & How much documents it's downloaded
total_pages = 0
Total_Documents = []
total_downloaded = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//*[@id='searchResultsTable']"))
    total_pages += element_count

    links = browser.find_elements(By.XPATH, "//a[contains(text(),'SECURITY DEED')]")
    hrefs = []
    for c in links:
        Total_Documents.append(c)
        hrefs.append(c.text)

    total_downloaded = total_downloaded + len(hrefs)
    '''
    for i in range(len(hrefs)):
        click_mortgage_form = browser.find_element(By.LINK_TEXT, hrefs[i])
        click_mortgage_form.click()
        time.sleep(2)
        click_view_image = browser.find_element(By.XPATH, "//a[@class='generator']")
        click_view_image.click()
        time.sleep(20)
        browser.back()
        time.sleep(3)
    print('Successfully downloaded', len(hrefs), 'documents in page', p)
    '''
    if not browser.find_elements(By.LINK_TEXT, 'Next'):
        break

    time.sleep(3)
    browser.find_element(By.LINK_TEXT, 'Next').click()

print('Total Pages: ', total_pages)
print('Total Security Deed Documents: ', len(Total_Documents))
print('Total downloaded documents:', total_downloaded)

# Getting home page

time.sleep(5)
for p in range(total_pages - 1):
    browser.back()
    time.sleep(3)

time.sleep(3)
browser.back()
time.sleep(5)

input_start_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDStart']")
time.sleep(3)
input_start_date.clear()
start_date = '07/24/2019' #dt.date.today().strftime('%m/%d/%Y')
time.sleep(4)
input_start_date.send_keys(start_date)


input_end_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDEnd']")
time.sleep(4)
input_end_date.clear()
end_date = '07/24/2019' #dt.date.today().strftime('%m/%d/%Y')
time.sleep(5)
input_end_date.send_keys(end_date)

# To Uncheck box to Search Specific Document Types
time.sleep(5)
check_box = browser.find_element(By.XPATH,"//input[@name='AllDocuments']")
check_box.click()
time.sleep(3)
check_box.click()
time.sleep(4)

# Selecting Warranty Deed & Warranty Deed(Re-Record) Documents
drop_down = Select(browser.find_element(By.XPATH,"//select[@name='__search_select']"))
drop_down.deselect_by_visible_text('SECURITY DEED')
time.sleep(4)
drop_down.select_by_visible_text('WARRANTY DEED')
time.sleep(4)
drop_down.select_by_visible_text('WARRANTY DEED (RE-RECORD)')

# Search button
time.sleep(4)
search_button = browser.find_element(By.XPATH,"//input[@value='Search']")
search_button.click()
time.sleep(8)

# Counting the total pages & Counting the total documents & How much documents it's downloaded
total_pages = 0
Total_Documents = []
total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//*[@id='searchResultsTable']"))
    total_pages += element_count

    links = browser.find_elements(By.XPATH, "//a[contains(text(),'WARRANTY DEED')]")
    hrefs = []
    for c in links:
        Total_Documents.append(c)
        hrefs.append(c.text)

    total = total + len(hrefs)
    for i in range(len(hrefs)):
        click_deed_form = browser.find_element(By.LINK_TEXT, hrefs[i])
        click_deed_form.click()
        time.sleep(5)
        click_view_image = browser.find_element(By.XPATH, "//a[@class='generator'][2]")
        click_view_image.click()
        time.sleep(20)
        browser.back()
        time.sleep(5)
    print('Successfully downloaded', len(hrefs), 'documents in page', p)

    if not browser.find_elements(By.LINK_TEXT, 'Next'):
        break

    time.sleep(3)
    browser.find_element(By.LINK_TEXT, 'Next').click()
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total WARRANTY DEED Documents: ', len(Total_Documents))
print('Total downloaded documents:', total)

# Quiting from web page
browser.quit()

