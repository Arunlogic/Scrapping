from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\FL-HILLSBOROUGH'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path,options=chrome_options)

url = "https://pubrec6.hillsclerk.com/ORIPublicAccess/customSearch.html"
browser.get(url)
browser.maximize_window()

time.sleep(5)
doc_type = browser.find_element(By.XPATH,"//div[@id='ORI-Document Type']")
doc_type.click()

# selecting document type
time.sleep(4)
input_box = browser.find_element(By.XPATH,"//input[@class='chosen-search-input default']").click()
time.sleep(3)
mortgage = browser.find_element(By.XPATH,"//ul[@class='chosen-results']//parent::div//descendant::li[contains(text(),'(MTG) MORTGAGE')]").click()
time.sleep(3)
browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div/div[2]/div/div[1]/strong").click()
time.sleep(2)
input_box = browser.find_element(By.XPATH,"//ul[@class='chosen-choices']").click()
time.sleep(2)
mortgage_1 = browser.find_element(By.XPATH,"//ul[@class='chosen-results']//parent::div//descendant::li[contains(text(),'(MTGNDOC) MORTGAGE NO DOC STAMPS')]").click()
time.sleep(3)
browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div/div[2]/div/div[1]/strong").click()
time.sleep(2)
input_box = browser.find_element(By.XPATH,"//ul[@class='chosen-choices']").click()
time.sleep(2)
mortgage_2 = browser.find_element(By.XPATH,"//ul[@class='chosen-results']//parent::div//descendant::li[contains(text(),'(MTGNT) MORTGAGE EXEMPT TAXES')]").click()
time.sleep(3)
browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div/div[2]/div/div[1]/strong").click()
time.sleep(2)
input_box = browser.find_element(By.XPATH,"//ul[@class='chosen-choices']").click()
time.sleep(2)
mortgage_3 = browser.find_element(By.XPATH,"//ul[@class='chosen-results']//parent::div//descendant::li[contains(text(),'(MTGNIT) MORTGAGE NO INTANGIBLE TAXES')]").click()

time.sleep(3)
input_start_date = browser.find_element(By.XPATH,"//input[@id='OBKey__1634_1']")
input_start_date.clear()
start_date = '01/13/2020'
time.sleep(3)
input_start_date.send_keys(start_date)

time.sleep(2)
input_end_date = browser.find_element(By.XPATH,"//input[@id='OBKey__1634_2']")
input_end_date.clear()
end_date = '01/13/2020'
time.sleep(3)
input_end_date.send_keys(end_date)

# search
time.sleep(3)
search = browser.find_element(By.XPATH,"//button[@id='sub']")
search.click()
time.sleep(5)

total_pages = 0
total_downloaded = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='jsgrid-table']"))
    total_pages += element_count

    links = browser.find_elements(By.XPATH, "//*[@id='jsgrid-table']/div[2]/table/tbody/tr/td[6]/div/a")
    hrefs = []
    for c in links:
        hrefs.append(c.text)
    print(len(hrefs))
    print(hrefs)

    total_downloaded = total_downloaded + len(hrefs)

    for i in range(len(hrefs)):
        click_owner_name = browser.find_element(By.LINK_TEXT, hrefs[i])
        click_owner_name.click()
        time.sleep(12)
        browser.find_element(By.XPATH, "//div[@id='fancyContent']")
        browser.switch_to.frame(browser.find_element(By.XPATH, ".//iframe[@id='docDisplay']"))
        download = browser.find_element(By.XPATH, "//button[@id='download']")
        download.click()
        time.sleep(15)
        browser.switch_to.default_content()
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='fancyContent']/button").click()
        time.sleep(5)

    print('Successfully downloaded', len(hrefs), 'documents in page', p)

    try:
        next_page = browser.find_element(By.XPATH, "//a[contains(text(),'Next')]")
        next_page.click()
    except Exception as e:
        break
    time.sleep(3)

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total_downloaded)

# DEED

time.sleep(5)
doc_no_1 = browser.find_element(By.XPATH,"//div[@id='ORI-Book/Page']")
browser.execute_script("arguments[0].scrollIntoView(true);",doc_no_1)
time.sleep(4)
browser.execute_script("window.scrollBy(0,-300)","")

# removing datatypes
time.sleep(5)
removing = browser.find_elements(By.XPATH,"//a[@class='search-choice-close']")
for r in removing:
    r.click()
    time.sleep(3)

time.sleep(4)
input_box = browser.find_element(By.XPATH,"//input[@class='chosen-search-input default']").click()
time.sleep(3)
deed = browser.find_element(By.XPATH,"//ul[@class='chosen-results']//parent::div//descendant::li[contains(text(),'(D) DEED')]").click()

# search
time.sleep(3)
search = browser.find_element(By.XPATH,"//button[@id='sub']")
search.click()
time.sleep(5)

total_pages = 0
total_downloaded = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='jsgrid-table']"))
    total_pages += element_count

    links = browser.find_elements(By.XPATH, "//*[@id='jsgrid-table']/div[2]/table/tbody/tr/td[6]/div/a")
    hrefs = []
    for c in links:
        hrefs.append(c.text)
    print(len(hrefs))
    print(hrefs)

    total_downloaded = total_downloaded + len(hrefs)

    for i in range(len(hrefs)):
        click_owner_name = browser.find_element(By.LINK_TEXT, hrefs[i])
        click_owner_name.click()
        time.sleep(12)
        browser.find_element(By.XPATH, "//div[@id='fancyContent']")
        browser.switch_to.frame(browser.find_element(By.XPATH, ".//iframe[@id='docDisplay']"))
        download = browser.find_element(By.XPATH, "//button[@id='download']")
        download.click()
        time.sleep(15)
        browser.switch_to.default_content()
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id='fancyContent']/button").click()
        time.sleep(5)

    print('Successfully downloaded', len(hrefs), 'documents in page', p)

    try:
        next_page = browser.find_element(By.XPATH, "//a[contains(text(),'Next')]")
        next_page.click()
    except Exception as e:
        break
    time.sleep(3)

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total_downloaded)

browser.quit()