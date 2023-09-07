from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\NC-WATAUGA'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})
# Opening browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "http://72.15.246.185/WataugaNCNW/application.asp?resize=true"
browser.get(url)
browser.maximize_window()

browser.switch_to.frame(browser.find_element(By.ID, 'tabframe0'))
time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//input[@id='fromdate']")
input_start_date.click()
start_date = '08/08/2017'
time.sleep(2)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH, "//input[@id='todate']")
input_end_date.click()
end_date = '08/08/2017'
time.sleep(2)
input_end_date.send_keys(end_date)
time.sleep(2)

# advance search

advance_search = browser.find_element(By.XPATH, "//a[@id='advancedsearch']")
advance_search.click()

# book type
time.sleep(2)
book_type = Select(browser.find_element(By.XPATH, "//select[@id='availablebooktypes']"))
book_type.select_by_visible_text('BOOK OF RECORD')

# instrument type
time.sleep(2)
instrument = browser.find_element(By.XPATH, "//select[@id='instrumenttypes']").click()
time.sleep(2)
instrument = Select(browser.find_element(By.XPATH, "//select[@id='instrumenttypes']"))
time.sleep(2)
instrument.deselect_by_visible_text('ACKNOWLEDGMENT (ACK)')
time.sleep(2)
instrument.select_by_visible_text('DEED OF TRUST')

# search
time.sleep(3)
search = browser.find_element(By.XPATH, "//a[@id='search']")
search.click()
time.sleep(5)

# download

total_pages = 0
total = 0
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
        time.sleep(4)
        p = p + 1
        print('Scrapping page:', p)
        element_count = len(browser.find_elements(By.XPATH, "//div[@id='resultspane']/table"))
        total_pages += element_count

        records = browser.find_elements(By.XPATH, "//td[@class='col c2']/img")
        print(len(records))
        total += len(records)
        browser.switch_to.default_content()
        for r in records:
            browser.switch_to.frame(browser.find_element(By.ID, 'tabframe0'))
            r.click()
            time.sleep(5)
            browser.switch_to.default_content()
            time.sleep(2)
            browser.switch_to.frame(browser.find_element(By.ID, "tabframe3"))
            time.sleep(1)
            browser.switch_to.frame(browser.find_element(By.ID, "frameObject"))
            time.sleep(1)
            browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='imageObject']"))
            time.sleep(1)
            download = browser.find_element(By.XPATH, "//button[@id='open-button']").click()
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
time.sleep(4)

browser.switch_to.frame(browser.find_element(By.ID, 'tabframe0'))
time.sleep(2)
instrument.deselect_by_visible_text('DEED OF TRUST')
time.sleep(2)
instrument.select_by_visible_text('DEED')

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//a[@id='search']")
search.click()
time.sleep(5)

# download
total_pages = 0
total = 0
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
            time.sleep(5)
            browser.switch_to.default_content()
            time.sleep(2)
            browser.switch_to.frame(browser.find_element(By.ID, "tabframe3"))
            time.sleep(1)
            browser.switch_to.frame(browser.find_element(By.ID, "frameObject"))
            time.sleep(1)
            browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='imageObject']"))
            time.sleep(1)
            download = browser.find_element(By.XPATH, "//button[@id='open-button']").click()
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

browser.quit()

