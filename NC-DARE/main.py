from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC


path  = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\NC-DARE'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})
browser = webdriver.Chrome(executable_path=path,options=chrome_options)

url= "http://www.courthousecomputersystems.com/darenc/"
browser.get(url)
browser.maximize_window()

# accept
time.sleep(2)
parent_handle = browser.current_window_handle
accept = browser.find_element(By.XPATH,"//a[contains(text(),'Click here to acknowledge this disclaimer and enter the site')]")
accept.click()
time.sleep(5)

all_handles = browser.window_handles
for handle in all_handles:
    if handle != parent_handle:
        browser.switch_to.window(handle)
time.sleep(5)
browser.maximize_window()
browser.switch_to.frame(browser.find_element(By.ID, "subapp_LRSearch_0"))
time.sleep(1)
advance = browser.find_element(By.XPATH, "//span[@id='levelTab_Advanced']").click()
time.sleep(4)
input_start_date = browser.find_element(By.XPATH, "//input[@id='advfromdate']")
input_start_date.click()
start_date = '08/03/2023'
time.sleep(2)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH, "//input[@id='advtodate']")
input_end_date.click()
end_date = '08/03/2023'
time.sleep(2)
input_end_date.send_keys(end_date)
time.sleep(2)

time.sleep(2)
doc_type = browser.find_element(By.XPATH, "//button[@id='doctypes_dialog']")
doc_type.click()

# book type
time.sleep(3)
doc = browser.find_element(By.XPATH, "//label[contains(text(),'D/T') and @for='125']").click()
time.sleep(1)
click_ok = browser.find_element(By.XPATH, "//button[contains(text(),'Ok')]").click()

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//button[@id='btnAdvancedSearch']")
search.click()
time.sleep(5)
browser.switch_to.default_content()

# download
total_pages = 0
total = 0
p = 0
time.sleep(3)
while True:

    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    browser.switch_to.frame(browser.find_element(By.ID, "subapp_LRSearch_0"))
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='gridTrad']/tbody/tr/td/table[1]/tbody"))
    total_pages += element_count

    records = browser.find_elements(By.XPATH, "//td[@class='dx_grid_cell Cell_Image dxgv']/img")
    total += len(records)

    max_doc = Select(browser.find_element(By.XPATH, "//select[@class='records_per_page']"))
    max_doc.select_by_visible_text('500')
    time.sleep(5)
    browser.switch_to.default_content()
    time.sleep(3)

    for r in records:
        browser.switch_to.frame(browser.find_element(By.ID, "subapp_LRSearch_0"))
        r.click()
        time.sleep(12)
        browser.switch_to.default_content()
        time.sleep(2)
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='subapp_Image']"))
        time.sleep(3)
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='imageIframe']"))
        time.sleep(3)
        download = browser.find_element(By.XPATH, "//button[@id='download']/span").click()
        time.sleep(8)
        browser.switch_to.default_content()
        back = browser.find_element(By.XPATH, "//span[contains(text(),'Consolidated Index')]").click()
        time.sleep(3)

    browser.switch_to.frame(browser.find_element(By.ID, "subapp_LRSearch_0"))
    print('Successfully downloaded', len(records), 'documents in page', p)

    try:
        total_count_pages = browser.find_element(By.XPATH, "//label[@class='of_pagecount']").text
        words = total_count_pages.split()
        for word in words:
            if word.isdigit():
                a = int(word)
        input_value = browser.find_element(By.XPATH, "//input[@class='page_number']")
        number = input_value.get_attribute('value')
        if int(number) < int(a):
            next_button = browser.find_element(By.XPATH, "//button[@id='gridTrad$PagerBarTNext']").click()
        else:
            break
    except Exception as e:
        break
    time.sleep(2)

print('Total Pages: ', total_pages)
print('Total downloaded documents: ', total)
print('Successfully downloaded all DEED OF TRUST documents')

browser.switch_to.default_content()
back = browser.find_element(By.XPATH, "//span[contains(text(),'Consolidated Index')]").click()
time.sleep(2)

browser.switch_to.frame(browser.find_element(By.ID, "subapp_LRSearch_0"))
edit = browser.find_element(By.XPATH, "//button[@title='Edit Search Criteria']/div").click()
time.sleep(2)
doc_type = browser.find_element(By.XPATH, "//button[@id='doctypes_dialog']")
doc_type.click()

# book type
time.sleep(3)
doc = browser.find_element(By.XPATH, "//label[contains(text(),'D/T') and @for='125']").click()
time.sleep(1)
doc_1 = browser.find_element(By.XPATH, "//label[contains(text(),'DEED') and @for='133']").click()
click_ok = browser.find_element(By.XPATH, "//button[contains(text(),'Ok')]").click()

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//button[@id='btnAdvancedSearch']")
search.click()
time.sleep(5)
browser.switch_to.default_content()
# download

total_pages = 0
total = 0
p = 0
time.sleep(3)
while True:

    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    browser.switch_to.frame(browser.find_element(By.ID, "subapp_LRSearch_0"))
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='gridTrad']/tbody/tr/td/table[1]/tbody"))
    total_pages += element_count

    records = browser.find_elements(By.XPATH, "//td[@class='dx_grid_cell Cell_Image dxgv']/img")
    total += len(records)

    max_doc = Select(browser.find_element(By.XPATH, "//select[@class='records_per_page']"))
    max_doc.select_by_visible_text('500')
    time.sleep(5)
    browser.switch_to.default_content()
    time.sleep(3)

    for r in records:
        browser.switch_to.frame(browser.find_element(By.ID, "subapp_LRSearch_0"))
        r.click()
        time.sleep(12)
        browser.switch_to.default_content()
        time.sleep(2)
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='subapp_Image']"))
        time.sleep(3)
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='imageIframe']"))
        time.sleep(3)
        download = browser.find_element(By.XPATH, "//button[@id='download']/span").click()
        time.sleep(8)
        browser.switch_to.default_content()
        back = browser.find_element(By.XPATH, "//span[contains(text(),'Consolidated Index')]").click()
        time.sleep(3)

    browser.switch_to.frame(browser.find_element(By.ID, "subapp_LRSearch_0"))
    print('Successfully downloaded', len(records), 'documents in page', p)

    try:
        total_count_pages = browser.find_element(By.XPATH, "//label[@class='of_pagecount']").text
        words = total_count_pages.split()
        for word in words:
            if word.isdigit():
                a = int(word)
        input_value = browser.find_element(By.XPATH, "//input[@class='page_number']")
        number = input_value.get_attribute('value')
        if int(number) < int(a):
            next_button = browser.find_element(By.XPATH, "//button[@id='gridTrad$PagerBarTNext']").click()
        else:
            break
    except Exception as e:
        break
    time.sleep(2)
print('Total Pages: ', total_pages)
print('Total downloaded documents: ', total)
print('Successfully downloaded all DEED documents')
browser.switch_to.default_content()
browser.close()
browser.switch_to.window(parent_handle)
browser.quit()





