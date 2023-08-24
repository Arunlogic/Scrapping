from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

#path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\NC-ROCKINGHAM'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})
# Opening browser
browser = webdriver.Chrome(options=chrome_options)
#browser = webdriver.Chrome(executable_path=path,options=chrome_options)

url="http://www.courthousecomputersystems.com/RockinghamNC/"
browser.get(url)
browser.maximize_window()

# accept
time.sleep(6)
parent_handle = browser.current_window_handle
accept = browser.find_element(By.XPATH,"//a[contains(text(),'Click here to acknowledge this disclaimer and enter the site')]")
accept.click()
time.sleep(5)

all_handles = browser.window_handles
for handle in all_handles:
    if handle != parent_handle:
        browser.switch_to.window(handle)
time.sleep(2)
browser.maximize_window()
browser.switch_to.frame(browser.find_element(By.ID, 'tabframe0'))
time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//input[@id='fromdate']")
input_start_date.click()
start_date = '08/08/2017'
time.sleep(3)
input_start_date.send_keys(start_date)

time.sleep(3)
input_end_date = browser.find_element(By.XPATH, "//input[@id='todate']")
input_end_date.click()
end_date = '08/08/2017'
time.sleep(3)
input_end_date.send_keys(end_date)
time.sleep(2)

# advance search
time.sleep(2)
advance_search = browser.find_element(By.XPATH, "//a[@id='advancedsearch']")
advance_search.click()

# book type
time.sleep(3)
book_type = Select(browser.find_element(By.XPATH, "//select[@id='availablebooktypes']"))
book_type.select_by_visible_text('DEED')

# instrument type
time.sleep(4)
instrument = browser.find_element(By.XPATH, "//select[@id='instrumenttypes']").click()
time.sleep(3)
instrument = Select(browser.find_element(By.XPATH, "//select[@id='instrumenttypes']"))
time.sleep(2)
instrument.deselect_by_visible_text('AGREEMENT')
instrument.select_by_visible_text('DEED OF TRUST')

# search
time.sleep(3)
search = browser.find_element(By.XPATH, "//a[@id='search']")
search.click()
time.sleep(5)

# select all documents

total_pages = 0
p = 0

while True:
    try:
        alert = WebDriverWait(browser, 2).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert_text = alert.text
        if "This is the last page" in alert_text:
            alert.dismiss()
            break

        else:
            alert.accept()
            break
    except Exception as e:
        p = p + 1
        print('Selected all documents in page no:', p)
        time.sleep(1)
        element_count = len(browser.find_elements(By.XPATH, "//div[@id='directoryresultspane']/table"))
        total_pages += element_count
        time.sleep(2)
        select_all = browser.find_element(By.XPATH, "//img[@title='Click this button to select all rows on this page']")
        select_all.click()
        time.sleep(2)
        next_button = browser.find_element(By.ID, "nextpage").click()
        time.sleep(2)

print('Total Pages: ', total_pages)

time.sleep(5)
display_documents = browser.find_element(By.XPATH,"//img[@title='Click this button to display documents for the parties you have selected']")
display_documents.click()

# download

total_pages = 0
total = 0
p = 0
time.sleep(3)
while True:
    try:
        alert = WebDriverWait(browser, 2).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert_text = alert.text
        if "This is the last page" in alert_text:
            alert.dismiss()
            break

        else:
            alert.accept()
            break
    except Exception as e:
        time.sleep(4)
        p = p + 1
        print('Scrapping page:', p)
        element_count = len(browser.find_elements(By.XPATH, "//div[@id='resultspane']/table"))
        total_pages += element_count

        records = browser.find_elements(By.XPATH, "//td[@class='col c2']/img")
        total += len(records)
        browser.switch_to.default_content()
        for r in records:
            browser.switch_to.frame(browser.find_element(By.ID, 'tabframe0'))
            r.click()
            time.sleep(10)
            browser.switch_to.default_content()
            back = browser.find_element(By.XPATH, "//a[contains(text(),'Real Property Index')]").click()
            time.sleep(3)
        browser.switch_to.frame(browser.find_element(By.ID, 'tabframe0'))
        print('Successfully downloaded', len(records), 'documents in page', p)
        next_button = browser.find_element(By.ID, "nextpage").click()
        time.sleep(2)

print('Total Pages: ', total_pages)
print('Total downloaded documents: ', total)
print('Successfully downloaded all DEED OF TRUST documents')

browser.switch_to.default_content()
back = browser.find_element(By.XPATH, "//a[contains(text(),'Real Property Index')]").click()
time.sleep(3)

browser.switch_to.frame(browser.find_element(By.ID, 'tabframe0'))
instrument.deselect_by_visible_text('DEED OF TRUST')
time.sleep(2)
instrument.select_by_visible_text('DEED')

# search
time.sleep(3)
search = browser.find_element(By.XPATH, "//a[@id='search']")
search.click()
time.sleep(5)

# select all documents

total_pages = 0
p = 0

while True:
    try:
        alert = WebDriverWait(browser, 2).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert_text = alert.text
        if "This is the last page" in alert_text:
            alert.dismiss()
            break

        else:
            alert.accept()
            break
    except Exception as e:
        p = p + 1
        print('Selected all documents in page no:', p)
        time.sleep(1)
        element_count = len(browser.find_elements(By.XPATH, "//div[@id='directoryresultspane']/table"))
        total_pages += element_count
        time.sleep(2)
        select_all = browser.find_element(By.XPATH, "//img[@title='Click this button to select all rows on this page']")
        select_all.click()
        time.sleep(2)
        next_button = browser.find_element(By.ID, "nextpage").click()
        time.sleep(2)

print('Total Pages: ', total_pages)

time.sleep(5)
display_documents = browser.find_element(By.XPATH,"//img[@title='Click this button to display documents for the parties you have selected']")
display_documents.click()

# download
total_pages = 0
total = 0
p = 0
time.sleep(3)
while True:
    try:
        alert = WebDriverWait(browser, 2).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert_text = alert.text
        if "This is the last page" in alert_text:
            alert.dismiss()
            break

        else:
            alert.accept()
            break
    except Exception as e:
        time.sleep(4)
        p = p + 1
        print('Scrapping page:', p)
        element_count = len(browser.find_elements(By.XPATH, "//div[@id='resultspane']/table"))
        total_pages += element_count

        records = browser.find_elements(By.XPATH, "//td[@class='col c2']/img")
        total += len(records)
        browser.switch_to.default_content()
        for r in records:
            browser.switch_to.frame(browser.find_element(By.ID, 'tabframe0'))
            r.click()
            time.sleep(10)
            browser.switch_to.default_content()
            back = browser.find_element(By.XPATH, "//a[contains(text(),'Real Property Index')]").click()
            time.sleep(3)
        browser.switch_to.frame(browser.find_element(By.ID, 'tabframe0'))
        print('Successfully downloaded', len(records), 'documents in page', p)
        next_button = browser.find_element(By.ID, "nextpage").click()
        time.sleep(2)

print('Total Pages: ', total_pages)
print('Total downloaded documents: ', total)
print('Successfully downloaded all DEED documents')

browser.close()
browser.switch_to.window(parent_handle)
browser.quit()




