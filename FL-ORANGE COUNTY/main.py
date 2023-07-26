from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\Orange County\\Mortgage'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path,options = chrome_options)
url = 'http://or.occompt.com/recorder/web/'
browser.get(url)
browser.maximize_window()

# Accept
click_accept = browser.find_element(By.XPATH,"//input[@value='I Accept']")
click_accept.click()
time.sleep(4)

# Under Recording
input_start_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDStart']")
start_date = '07/24/2019'            #dt.date.today().strftime('%m/%d/%Y')
time.sleep(4)
input_start_date.send_keys(start_date)


input_end_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDEnd']")
end_date = '07/24/2019'        #    dt.date.today().strftime('%m/%d/%Y')         # month/date/year  datetime.date.today().strftime('%Y-%m-%d')
time.sleep(4)
input_end_date.send_keys(end_date)

# To Uncheck box to Search Specific Document Types
time.sleep(5)
check_box = browser.find_element(By.XPATH,"//input[@name='AllDocuments']")
check_box.click()

# Replace the number of times you want to scroll

for i in range(3):
    drop_down = browser.find_element(By.XPATH,"//select[@name='__search_select']")     # Scroll to the end of the page
    time.sleep(2)                                                                # it will take 2 seconds to load more records

user_document_type_input = 'Mortgage'   # Mortgage
element = Select(drop_down)
element.select_by_visible_text(user_document_type_input)
time.sleep(9)

# Click to search Mortgage records
search_button = browser.find_element(By.XPATH,"//input[@class='search']")
search_button.click()
time.sleep(10)

# To download
# Counting the total pages & Counting the total mortgage documents & How much documents it's downloaded


total_pages = 0
total_downloaded = 0
p = 0
while True:
    time.sleep(10)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//*[@id='searchResultsTable']/tbody/tr[1]/td[1]/strong/a"))
    total_pages += element_count

    links = browser.find_elements(By.XPATH, ".//a[contains(text(),'Mortgage')]")
    hrefs = []
    for c in links:
        hrefs.append(c.text)
    total_downloaded = total_downloaded + len(hrefs)

    for i in range(len(hrefs)):
        click_mortgage_form = browser.find_element(By.LINK_TEXT, hrefs[i])
        click_mortgage_form.click()
        time.sleep(4)
        click_view_image = browser.find_element(By.XPATH, "//a[@class='generator']")
        click_view_image.click()
        time.sleep(20)
        browser.back()
        time.sleep(8)
    print('Successfully downloaded', len(hrefs), 'documents in page', p)

    if not browser.find_elements(By.LINK_TEXT, 'Next'):
        break

    browser.find_element(By.LINK_TEXT, 'Next').click()
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total Mortgage Documents: ', total_downloaded)
print('Total downloaded documents:', total_downloaded)

# DEED

time.sleep(5)
for p in range(total_pages - 1):
    browser.back()
    time.sleep(3)

time.sleep(3)
browser.back()
time.sleep(5)

# Under Recording
input_start_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDStart']")
start_date = '07/24/2019'            #dt.date.today().strftime('%m/%d/%Y')
time.sleep(4)
input_start_date.send_keys(start_date)


input_end_date = browser.find_element(By.XPATH,"//input[@name='RecordingDateIDEnd']")
end_date =   '07/24/2019'        #    dt.date.today().strftime('%m/%d/%Y')         # month/date/year  datetime.date.today().strftime('%Y-%m-%d')
time.sleep(4)
input_end_date.send_keys(end_date)


# To Uncheck box to Search Specific Document Types
time.sleep(5)
check_box = browser.find_element(By.XPATH,"//input[@name='AllDocuments']")
check_box.click()

for i in range(3):
    drop_down = browser.find_element(By.XPATH,"//select[@name='__search_select']")    # Scroll to the end of the page
    time.sleep(2)                                                                # it will take 2 seconds to load more records

user_document_type_input = 'Deed'  # Deed
element = Select(drop_down)
time.sleep(3)
element.select_by_visible_text(user_document_type_input)

# Click to search Deed records
time.sleep(5)
search_button = browser.find_element(By.XPATH,"//input[@class='search']")
search_button.click()

# Counting the total pages & Counting the total deed documents & How much documents it's downloaded

total_pages = 0
deed_total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//*[@id='searchResultsTable']/tbody/tr[1]/td[1]/strong/a"))
    total_pages += element_count

    links = browser.find_elements(By.XPATH, ".//a[contains(text(),'Deed')]")
    hrefs = []
    for c in links:
        if c in browser.find_elements(By.XPATH, "//a[contains(text(),'Tax Deed Sales')]"):
            del c
        else:
            hrefs.append(c.text)

    deed_total = deed_total + len(hrefs)
    for i in range(len(hrefs)):
        click_deed_form = browser.find_element(By.LINK_TEXT, hrefs[i])
        click_deed_form.click()
        time.sleep(2)
        click_view_image = browser.find_element(By.XPATH, "//a[@class='generator']")
        click_view_image.click()
        time.sleep(10)
        browser.back()
        time.sleep(3)
    print('Successfully downloaded', len(hrefs), 'documents in page', p)

    if not browser.find_elements(By.LINK_TEXT, 'Next'):
        break

    time.sleep(3)
    browser.find_element(By.LINK_TEXT, 'Next').click()

print('Total Pages: ', total_pages)
print('Total Deed Documents: ',deed_total )
print('Total downloaded documents:', deed_total)

browser.quit()