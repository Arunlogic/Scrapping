from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"
path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\NC-CABARRUS'

# chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})
# Opening browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "http://www.cabarrusncrod.org/Opening.asp"
browser.get(url)
browser.maximize_window()

# accept
time.sleep(4)
accept = browser.find_element(By.XPATH, "//a[contains(text(),'Acknowledge Disclaimer to Begin Searching Records')]")
accept.click()

# Full system
time.sleep(3)
full_system = browser.find_element(By.XPATH, "//div[@class='mainContent'][2]/a")
full_system.click()

# recorded date
time.sleep(4)
recorded_date = browser.find_element(By.XPATH, "//span[contains(text(),'Recorded Date')]")
recorded_date.click()

time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//div[@id='VWGTCMD_24']/div[2]/div[2]/div[1]/div/div/div[3]/input")
start_date = '08/08/2017'
time.sleep(2)
input_start_date.send_keys(start_date)

time.sleep(2)
input_end_date = browser.find_element(By.XPATH, "//div[@id='VWGTCMD_24']/div[2]/div[2]/div[1]/div/div/div[2]/input")
end_date = '08/08/2017'
time.sleep(3)
input_end_date.send_keys(end_date)
time.sleep(2)

# document type

doc_type = browser.find_element(By.XPATH,
                                "//div[@id='VWGTCMD_24']/div[2]/div[2]/div[1]/div/div/div[6]/input").send_keys('D-TR')

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//div[@id='VWG_25']/div/div/div/table/tbody/tr/td/span")
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
    element_count = len(browser.find_elements(By.XPATH, "//div[@id='VWGDGVBODY_152']"))
    total_pages += element_count
    doc_no = []
    records = browser.find_elements(By.XPATH,
                                    "//div[@id='VWGDGVBODY_152']/div/div/div/div[4]/div/div/div/div/div//span")
    for ids in records:
        doc_no.append(ids.text)
    print(doc_no)
    parent_handle = browser.current_window_handle
    total += len(doc_no)
    for i in range(len(doc_no)):
        docs = browser.find_element(By.XPATH, "//span[contains(text(),'" + doc_no[i] + "')]")
        docs.click()
        time.sleep(3)
        # image = browser.find_element(By.XPATH, "//div[@id='VWG_159']/div/div/div/table/tbody/tr/td").click()
        image = browser.find_element(By.XPATH, "//span[@class='Button-FontData'][contains(text(),'Image')]")
        browser.execute_script("arguments[0].click();", image)
        time.sleep(4)
        all_windows = browser.window_handles
        for window in all_windows:
            if window != parent_handle:
                browser.switch_to.window(window)
                time.sleep(2)
                browser.switch_to.frame(browser.find_element(By.XPATH, "//frame[@id='fraImage']"))
                download = browser.find_element(By.XPATH, "//button[@id='open-button']").click()
                time.sleep(12)
                browser.close()
        browser.switch_to.window(parent_handle)
        time.sleep(3)
    print('Successfully downloaded', len(doc_no), 'documents in page', p)
    break
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)
'''
time.sleep(3)
b = browser.find_element(By.XPATH,"//span[@class='Button-FontData'][contains(text(),'Image')]")
browser.execute_script("arguments[0].click();", b)
'''

### DEED

# index search
time.sleep(4)
index_search = browser.find_element(By.XPATH, "//span[@id='TXT_11']").click()

# document type
time.sleep(3)
doc_type = browser.find_element(By.XPATH, "//div[@id='VWGTCMD_24']/div[2]/div[2]/div[1]/div/div/div[6]/input")
doc_type.clear()
time.sleep(2)
doc_type = browser.find_element(By.XPATH,
                                "//div[@id='VWGTCMD_24']/div[2]/div[2]/div[1]/div/div/div[6]/input").send_keys('DEED')

# search
time.sleep(2)
search = browser.find_element(By.XPATH, "//div[@id='VWG_25']/div/div/div/table/tbody/tr/td/span")
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
    element_count = len(browser.find_elements(By.XPATH, "//div[@id='VWGDGVBODY_152']"))
    total_pages += element_count
    doc_no = []
    records = browser.find_elements(By.XPATH,
                                    "//div[@id='VWGDGVBODY_152']/div/div/div/div[4]/div/div/div/div/div//span")
    for ids in records:
        doc_no.append(ids.text)
    print(doc_no)
    parent_handle = browser.current_window_handle
    total += len(doc_no)
    for i in range(len(doc_no)):
        docs = browser.find_element(By.XPATH, "//span[contains(text(),'" + doc_no[i] + "')]")
        docs.click()
        time.sleep(3)
        # image = browser.find_element(By.XPATH, "//div[@id='VWG_159']/div/div/div/table/tbody/tr/td").click()
        image = browser.find_element(By.XPATH, "//span[@class='Button-FontData'][contains(text(),'Image')]")
        browser.execute_script("arguments[0].click();", image)
        time.sleep(4)
        all_windows = browser.window_handles
        for window in all_windows:
            if window != parent_handle:
                browser.switch_to.window(window)
                time.sleep(2)
                browser.switch_to.frame(browser.find_element(By.XPATH, "//frame[@id='fraImage']"))
                download = browser.find_element(By.XPATH, "//button[@id='open-button']").click()
                time.sleep(12)
                browser.close()
        browser.switch_to.window(parent_handle)
        time.sleep(3)

    print('Successfully downloaded', len(doc_no), 'documents in page', p)
    break
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()