from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"
path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\MA-HAMPDEN'

chrome_options = Options()

chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})
# Opening browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "https://search.hampdendeeds.com/html/Hampden/V3/search.html#"
browser.get(url)
browser.maximize_window()

### RECORDED LAND - MORTGAGE

# recorded land
time.sleep(5)
date_range = browser.find_element(By.XPATH, "//div[@class='row mb-5']/div[1]/div/ul/li[6]/a").click()

time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//input[@id='W9FDTA']")
input_start_date.clear()
start_date = '08082017'
time.sleep(2)
input_start_date.send_keys(start_date)

time.sleep(2)
input_end_date = browser.find_element(By.XPATH, "//input[@id='W9TDTA']")
input_end_date.clear()
end_date = '08082017'
time.sleep(2)
input_end_date.send_keys(end_date)
time.sleep(2)

# document type

doc_type = Select(browser.find_element(By.XPATH, "//select[@id='W9ABR']"))
doc_type.select_by_visible_text('Mortgage')

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//input[@value='Search Records']")
search.click()
time.sleep(5)

# download

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='mainContent']/table"))
    total_pages += element_count
    doc_no = []
    records = browser.find_elements(By.XPATH, "//a[@title='View Document Image']/img")
    print(len(records))
    parent_handle = browser.current_window_handle
    total += len(records)

    for img in records:
        try:
            browser.execute_script("arguments[0].scrollIntoView(true);", img)
            time.sleep(2)
            img.click()
            time.sleep(5)
            all_handles = browser.window_handles
            for handle in all_handles:
                if handle != parent_handle:
                    browser.switch_to.window(handle)
                    time.sleep(2)
                    download = browser.find_element(By.XPATH, "//a[contains(text(),'Download the Image')][1]").click()
                    time.sleep(15)
                    browser.close()
            browser.switch_to.window(parent_handle)
            time.sleep(4)
        except Exception as e:
            break

    print('Successfully downloaded', len(records), 'documents in page', p)

    try:
        no_records = browser.find_element(By.XPATH, "//div[@class='mainContent']/table/tbody/tr/td/b")
        if no_records:
            break

    except Exception as e:
        next_button = browser.find_element(By.XPATH, "//form[@id='search']/div/div[4]/div[1]/div/a[2]").click()

    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

### DEED

# new search
time.sleep(4)
new_search = browser.find_element(By.XPATH, "//input[@value='New Search']").click()

# entry date
time.sleep(3)
entry = browser.find_element(By.XPATH, "//a[contains(text(),'Entry Date')]").click()

time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//input[@id='W9FDTA']")
input_start_date.clear()
start_date = '08082017'
time.sleep(2)
input_start_date.send_keys(start_date)

time.sleep(2)
input_end_date = browser.find_element(By.XPATH, "//input[@id='W9TDTA']")
input_end_date.clear()
end_date = '08082017'
time.sleep(2)
input_end_date.send_keys(end_date)
time.sleep(2)

# document type

doc_type = Select(browser.find_element(By.XPATH, "//select[@id='W9ABR']"))
doc_type.select_by_visible_text('*Deed document group')

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//form[@id='search']/div/input")
search.click()
time.sleep(5)

# download

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='mainContent']/table"))
    total_pages += element_count
    doc_no = []
    records = browser.find_elements(By.XPATH, "//a[@title='View Document Image']/img")
    print(len(records))
    parent_handle = browser.current_window_handle
    total += len(records)

    for img in records:
        try:
            browser.execute_script("arguments[0].scrollIntoView(true);", img)
            time.sleep(2)
            img.click()
            time.sleep(5)
            all_handles = browser.window_handles
            for handle in all_handles:
                if handle != parent_handle:
                    browser.switch_to.window(handle)
                    time.sleep(2)
                    download = browser.find_element(By.XPATH, "//a[contains(text(),'Download the Image')][1]").click()
                    time.sleep(15)
                    browser.close()
            browser.switch_to.window(parent_handle)
            time.sleep(4)
        except Exception as e:
            break

    print('Successfully downloaded', len(records), 'documents in page', p)

    try:
        no_records = browser.find_element(By.XPATH, "//div[@class='mainContent']/table/tbody/tr/td/b")
        if no_records:
            break

    except Exception as e:
        next_button = browser.find_element(By.XPATH, "//form[@id='search']/div/div[4]/div[1]/div/a[2]").click()

    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

### LAND COURT - MORTGAGE

time.sleep(5)
land_records = browser.find_element(By.XPATH, "//a[contains(text(),'Search Land Court Records')]").click()

# entry date
time.sleep(3)
entry = browser.find_element(By.XPATH, "//a[contains(text(),'Entry Date')]").click()

time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//input[@id='W9FDTA']")
input_start_date.clear()
start_date = '08082017'
time.sleep(2)
input_start_date.send_keys(start_date)

time.sleep(2)
input_end_date = browser.find_element(By.XPATH, "//input[@id='W9TDTA']")
input_end_date.clear()
end_date = '08082017'
time.sleep(2)
input_end_date.send_keys(end_date)
time.sleep(2)

# document type

doc_type = Select(browser.find_element(By.XPATH, "//select[@id='W9ABR']"))
doc_type.select_by_visible_text('Mortgage')

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//form[@id='search']/div/input")
search.click()
time.sleep(5)

# download

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='mainContent']/table"))
    total_pages += element_count
    doc_no = []
    records = browser.find_elements(By.XPATH, "//a[@title='View Document Image']/img")
    print(len(records))
    parent_handle = browser.current_window_handle
    total += len(records)

    for img in records:
        try:
            browser.execute_script("arguments[0].scrollIntoView(true);", img)
            time.sleep(2)
            img.click()
            time.sleep(5)
            all_handles = browser.window_handles
            for handle in all_handles:
                if handle != parent_handle:
                    browser.switch_to.window(handle)
                    time.sleep(2)
                    download = browser.find_element(By.XPATH, "//a[contains(text(),'Download the Image')][1]").click()
                    time.sleep(15)
                    browser.close()
            browser.switch_to.window(parent_handle)
            time.sleep(4)
        except Exception as e:
            break

    print('Successfully downloaded', len(records), 'documents in page', p)

    try:
        no_records = browser.find_element(By.XPATH, "//div[@class='mainContent']/table/tbody/tr/td/b")
        if no_records:
            break

    except Exception as e:
        next_button = browser.find_element(By.XPATH, "//form[@id='search']/div/div[4]/div[1]/div/a[2]").click()

    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

### DEED

time.sleep(5)
land_records = browser.find_element(By.XPATH, "//a[contains(text(),'Search Land Court Records')]").click()

# entry date
time.sleep(3)
entry = browser.find_element(By.XPATH, "//a[contains(text(),'Entry Date')]").click()

time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//input[@id='W9FDTA']")
input_start_date.clear()
start_date = '08082017'
time.sleep(2)
input_start_date.send_keys(start_date)

time.sleep(2)
input_end_date = browser.find_element(By.XPATH, "//input[@id='W9TDTA']")
input_end_date.clear()
end_date = '08082017'
time.sleep(2)
input_end_date.send_keys(end_date)
time.sleep(2)

# document type

doc_type = Select(browser.find_element(By.XPATH, "//select[@id='W9ABR']"))
doc_type.select_by_visible_text('*Deed document group')

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//form[@id='search']/div/input")
search.click()
time.sleep(5)

# download

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='mainContent']/table"))
    total_pages += element_count
    doc_no = []
    records = browser.find_elements(By.XPATH, "//a[@title='View Document Image']/img")
    print(len(records))
    parent_handle = browser.current_window_handle
    total += len(records)

    for img in records:
        try:
            browser.execute_script("arguments[0].scrollIntoView(true);", img)
            time.sleep(2)
            img.click()
            time.sleep(5)
            all_handles = browser.window_handles
            for handle in all_handles:
                if handle != parent_handle:
                    browser.switch_to.window(handle)
                    time.sleep(2)
                    download = browser.find_element(By.XPATH, "//a[contains(text(),'Download the Image')][1]").click()
                    time.sleep(15)
                    browser.close()
            browser.switch_to.window(parent_handle)
            time.sleep(4)
        except Exception as e:
            break

    print('Successfully downloaded', len(records), 'documents in page', p)

    try:
        no_records = browser.find_element(By.XPATH, "//div[@class='mainContent']/table/tbody/tr/td/b")
        if no_records:
            break

    except Exception as e:
        next_button = browser.find_element(By.XPATH, "//form[@id='search']/div/div[4]/div[1]/div/a[2]").click()

    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()