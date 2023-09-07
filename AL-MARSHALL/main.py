from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\AL-MARSHALL'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "http://www.deedlookup.org/"
browser.get(url)
browser.maximize_window()

time.sleep(5)
browser.switch_to.frame(browser.find_element(By.XPATH, "//frame[@name='SearchSelection']"))
time.sleep(1)
grantee = browser.find_element(By.XPATH, "//input[@value='   Grantor or Grantee  ']").click()

time.sleep(4)
document_type = Select(browser.find_element(By.XPATH, "//select[@name='HTMINSTRUTYPEREF']"))
document_type.select_by_visible_text('MORTGAGE')

time.sleep(2)
from_month = Select(browser.find_element(By.XPATH, "//select[@name='fmonth']"))
from_month.select_by_visible_text('AUG')

time.sleep(2)
from_date = Select(browser.find_element(By.XPATH, "//select[@name='fday']"))
from_date.select_by_visible_text('04')

time.sleep(2)
from_year = Select(browser.find_element(By.XPATH, "//select[@name='fyear']"))
from_year.select_by_visible_text('2017')

time.sleep(2)
to_month = Select(browser.find_element(By.XPATH, "//select[@name='tmonth']"))
to_month.select_by_visible_text('AUG')

time.sleep(2)
to_date = Select(browser.find_element(By.XPATH, "//select[@name='tday']"))
to_date.select_by_visible_text('04')

time.sleep(2)
to_year = Select(browser.find_element(By.XPATH, "//select[@name='tyear']"))
to_year.select_by_visible_text('2017')

time.sleep(2)
search = browser.find_element(By.XPATH, "//input[@value='Search']").click()
time.sleep(3)
browser.switch_to.default_content()

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0

while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    browser.switch_to.frame(browser.find_element(By.XPATH, "//frame[@name='results']"))
    element_count = len(browser.find_elements(By.XPATH, "//body[@alink='maroon'][@link='maroon']"))
    total_pages += element_count
    ids = browser.find_elements(By.XPATH, "//body[@alink='maroon'][@link='maroon']/p/font[3]/table/tbody/tr/td/font/a")
    print(len(ids))
    total = total + len(ids)
    browser.switch_to.default_content()
    time.sleep(2)

    for img in ids:
        browser.switch_to.frame(browser.find_element(By.XPATH, "//frame[@name='results']"))
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        browser.switch_to.default_content()
        time.sleep(6)
        try:
            browser.switch_to.frame(browser.find_element(By.XPATH, "//frame[@name='summary']"))
            download = browser.find_element(By.XPATH,
                                            "//a[contains(text(),'DOWNLOAD THE DEED IN PDF FORMAT ')]").click()
            time.sleep(3)
            view = browser.find_element(By.XPATH, "//button[@id='open-button']").click()
            browser.switch_to.default_content()
            time.sleep(6)
        except Exception as e:
            break

    print('Successfully downloaded', len(ids), 'documents in page', p)
    break
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

### DEED

browser.switch_to.frame(browser.find_element(By.XPATH, "//frame[@name='SearchSelection']"))
time.sleep(3)
document_type = Select(browser.find_element(By.XPATH, "//select[@name='HTMINSTRUTYPEREF']"))
document_type.select_by_visible_text('DEED')

time.sleep(2)
search = browser.find_element(By.XPATH, "//input[@value='Search']").click()
time.sleep(3)
browser.switch_to.default_content()

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0

while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    browser.switch_to.frame(browser.find_element(By.XPATH, "//frame[@name='results']"))
    element_count = len(browser.find_elements(By.XPATH, "//body[@alink='maroon'][@link='maroon']"))
    total_pages += element_count
    ids = browser.find_elements(By.XPATH, "//body[@alink='maroon'][@link='maroon']/p/font[3]/table/tbody/tr/td/font/a")
    print(len(ids))
    total = total + len(ids)
    browser.switch_to.default_content()
    time.sleep(2)

    for img in ids:
        browser.switch_to.frame(browser.find_element(By.XPATH, "//frame[@name='results']"))
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        browser.switch_to.default_content()
        time.sleep(6)
        try:
            browser.switch_to.frame(browser.find_element(By.XPATH, "//frame[@name='summary']"))
            download = browser.find_element(By.XPATH,
                                            "//a[contains(text(),'DOWNLOAD THE DEED IN PDF FORMAT ')]").click()
            time.sleep(3)
            view = browser.find_element(By.XPATH, "//button[@id='open-button']").click()
            browser.switch_to.default_content()
            time.sleep(6)
        except Exception as e:
            break

    print('Successfully downloaded', len(ids), 'documents in page', p)
    break
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()