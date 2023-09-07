from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\IonIdea\County_Downloaded_Documents\IL-DEKALB'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "http://lrs.dekalbrecorder.com/Search/Index"
browser.get(url)
browser.maximize_window()

# log in
time.sleep(4)
user_name = browser.find_element(By.XPATH, "//input[@id='Username']").send_keys('ionaccess')
time.sleep(2)
password = browser.find_element(By.XPATH, "//input[@id='Password']").send_keys('delete123')
time.sleep(2)
log_in = browser.find_element(By.XPATH, "//input[@id='userLogin']").click()
print('Successfully log in')

# land records
time.sleep(6)
element = browser.find_element(By.XPATH, "//a[contains(text(),'Search Land Records')]")
actions = ActionChains(browser)
actions.move_to_element(element).perform()
# records = browser.find_element(By.XPATH,"//a[contains(text(),'Search Land Records')]")
time.sleep(3)

records_1 = browser.find_element(By.XPATH, "//a[contains(text(),'Document Type')]").click()
# records_1 = browser.find_element(By.XPATH,"//li[@class='has_dropdown current']/ul/li[6]/a").click()
time.sleep(6)

# document types
mtg = Select(browser.find_element(By.XPATH, "//select[@id='oDocumentType_InstrumentCodes']"))
mtg.select_by_visible_text('F2 - Mtg')
time.sleep(3)

input_start_date = browser.find_element(By.XPATH, "//input[@id='oAdditional_DateFiledFrom']")
start_date = '08/08/2017'
time.sleep(3)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH, "//input[@id='oAdditional_DateFiledTo']")
end_date = '08/08/2017'
time.sleep(3)
input_end_date.send_keys(end_date)

# search
time.sleep(3)
search = browser.find_element(By.XPATH, "//button[@id='search']").click()
time.sleep(8)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0

while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='dataTables_scrollBody']/table"))
    total_pages += element_count

    images = browser.find_elements(By.XPATH, "//table[@id='documents']/tbody/tr/td[11]/a[1]/img")
    total = total + len(images)
    parent_handle = browser.current_window_handle

    for img in images:
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        time.sleep(5)
        seperate_window = browser.find_element(By.XPATH,
                                               "//body[@orient='portrait']/div[5]/div[3]/div/button[2]/span").click()
        time.sleep(2)
        all_handles = browser.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                browser.switch_to.window(handle)
                time.sleep(6)
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='image_iframe']"))
                time.sleep(3)
                save = browser.find_element(By.XPATH, "//div[@id='imageDiv']/menu/ul/li[2]").click()
                time.sleep(15)
                browser.close()
        browser.switch_to.window(parent_handle)
        # back = browser.find_element(By.XPATH,"//body[@orient='portrait']/div[5]/div[1]/div/a[1]/span").click()
        time.sleep(3)

    print('Successfully downloaded', len(images), 'documents in page', p)
    time.sleep(5)
    browser.execute_script("window.scrollBy(0,210)", "")
    try:
        next_button = browser.find_element(By.XPATH, "//a[contains(text(),'Next')]")
        next_button.click()
        time.sleep(10)
    except Exception as e:
        break

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

### DEED

# land records
time.sleep(6)
element = browser.find_element(By.XPATH, "//a[contains(text(),'Search Land Records')]")
actions = ActionChains(browser)
actions.move_to_element(element).perform()
time.sleep(3)

records_1 = browser.find_element(By.XPATH, "//a[contains(text(),'Document Type')]").click()
time.sleep(6)

# document types
mtg = Select(browser.find_element(By.XPATH, "//select[@id='oDocumentType_InstrumentCodes']"))
mtg.select_by_visible_text('A1 - WD')
time.sleep(3)

input_start_date = browser.find_element(By.XPATH, "//input[@id='oAdditional_DateFiledFrom']")
start_date = '08/08/2017'
time.sleep(3)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH, "//input[@id='oAdditional_DateFiledTo']")
end_date = '08/08/2017'
time.sleep(3)
input_end_date.send_keys(end_date)

# search
time.sleep(3)
search = browser.find_element(By.XPATH, "//button[@id='search']").click()
time.sleep(8)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0

while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='dataTables_scrollBody']/table"))
    total_pages += element_count

    images = browser.find_elements(By.XPATH, "//table[@id='documents']/tbody/tr/td[11]/a[1]/img")
    total = total + len(images)
    parent_handle = browser.current_window_handle

    for img in images:
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        time.sleep(5)
        seperate_window = browser.find_element(By.XPATH,
                                               "//body[@orient='portrait']/div[5]/div[3]/div/button[2]/span").click()
        time.sleep(2)
        all_handles = browser.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                browser.switch_to.window(handle)
                time.sleep(6)
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='image_iframe']"))
                time.sleep(3)
                save = browser.find_element(By.XPATH, "//div[@id='imageDiv']/menu/ul/li[2]").click()
                time.sleep(15)
                browser.close()
        browser.switch_to.window(parent_handle)
        time.sleep(3)

    print('Successfully downloaded', len(images), 'documents in page', p)
    time.sleep(5)
    browser.execute_script("window.scrollBy(0,210)", "")
    try:
        next_button = browser.find_element(By.XPATH, "//a[contains(text(),'Next')]")
        next_button.click()
        time.sleep(10)
    except Exception as e:
        break

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()