from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\NC-DURHAM'
chrome_options = Options()

chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "https://rodweb.dconc.gov/web/"
browser.get(url)
browser.maximize_window()

# Accept
time.sleep(5)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")   # getting page scroll
time.sleep(4)
click_accept = browser.find_element(By.XPATH,"//button[@id='submitDisclaimerAccept']")
click_accept.click()

time.sleep(8)
records = browser.find_element(By.XPATH,"//a[@class='ss-action ss-action-form ss-utility-box ss-action-page-search ui-link'][1]")
records.click()
time.sleep(4)

time.sleep(3)
input_start_date = browser.find_element(By.XPATH,"//input[@id='field_RecordingDateID_DOT_StartDate']")
start_date = '09/15/2022'
time.sleep(3)
input_start_date.send_keys(start_date)

time.sleep(2)
input_end_date = browser.find_element(By.XPATH,"//input[@id='field_RecordingDateID_DOT_EndDate']")
end_date = '09/15/2022'
time.sleep(3)
input_end_date.send_keys(end_date)

# Selecting Document type
time.sleep(3)
browser.execute_script("window.scrollBy(0,800)","")
time.sleep(3)
input_box = browser.find_element(By.ID,"field_selfservice_documentTypes")
input_box.click()
time.sleep(5)
sending = browser.find_element(By.XPATH,"//input[@id='field_selfservice_documentTypes']").send_keys('mortgage')
time.sleep(5)
mortgage = browser.find_element(By.XPATH,"//ul[@id='field_selfservice_documentTypes-aclist']//parent::div//descendant::li[contains(text(),'MORTGAGE')][1]").click()
input_box.clear()
time.sleep(5)
sending = browser.find_element(By.XPATH,"//input[@id='field_selfservice_documentTypes']").send_keys('deed of trust')
time.sleep(5)
deed_of_trust = browser.find_element(By.XPATH,"//ul[@id='field_selfservice_documentTypes-aclist']//parent::div//descendant::li[contains(text(),'DEED OF TRUST')][1]").click()
time.sleep(3)
input_box.clear()
time.sleep(5)
search = browser.find_element(By.XPATH,"//a[contains(text(),'Search')]")
search.click()

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//li[@class='ui-li-static ui-body-inherit ui-last-child']"))
    total_pages += element_count

    ids = browser.find_elements(By.XPATH, "//div[@class='selfServiceSearchRowRight']/h1")
    document_number = []
    for d in ids:
        document_number.append(d.text[0:10])
    # print(len(document_number))
    print('Document Numbers:',document_number)

    total = total + len(document_number)
    for i in range(len(document_number)):
        if i <= len(document_number):
            doc_no = browser.find_element(By.XPATH, "//h1[contains(text(),'" + document_number[i] + "')]")
            doc_no.click()
            time.sleep(6)
            view = browser.find_element(By.XPATH, "//h1[contains(text(),'" + document_number[i] + "')]//parent::div//descendant::a[@title='View Document']")
            view.click()
            time.sleep(25)
            browser.switch_to.frame(browser.find_element(By.XPATH, ".//iframe[@class='ss-pdfjs-lviewer']"))
            time.sleep(5)
            document = browser.find_element(By.XPATH, "//button[@id='download']")
            document.click()
            time.sleep(20)
            browser.switch_to.default_content()
            time.sleep(5)
            browser.back()
            time.sleep(10)
            try:
                doc_no_1 = browser.find_element(By.XPATH, "//h1[contains(text(),'" + document_number[i + 1] + "')]")
                browser.execute_script("arguments[0].scrollIntoView(true);", doc_no_1)
                time.sleep(6)
                browser.execute_script("window.scrollBy(0,-150)", "")
                time.sleep(5)
            except Exception as e:
                time.sleep(10)

    print('Successfully downloaded', len(document_number), 'documents in page', p)
    time.sleep(10)
    browser.execute_script("window.scrollBy(0,210)", "")
    try:
        next_button = browser.find_element(By.XPATH, "//a[contains(text(),'Next')]")
        time.sleep(5)
        next_button.click()
        time.sleep(15)
    except Exception as e:
        break

    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

# DEED

time.sleep(5)
book_page = browser.find_element(By.XPATH,"//label[contains(text(),'Lot')]")
browser.execute_script("arguments[0].scrollIntoView();",book_page)

# removing datatypes
time.sleep(5)
removing = browser.find_elements(By.XPATH,"//li[@class='cblist-input-list transition-background']/p")
for r in removing:
    r.click()
    time.sleep(3)

# selecting deed
time.sleep(4)
input_box = browser.find_element(By.ID,'field_selfservice_documentTypes')
sending = browser.find_element(By.XPATH,"//input[@id='field_selfservice_documentTypes']").send_keys('deed')
time.sleep(3)
deed = browser.find_element(By.XPATH,"//ul[@id='field_selfservice_documentTypes-aclist']//parent::div//descendant::li[contains(text(),'DEED')][1]").click()
time.sleep(3)
input_box.clear()
time.sleep(4)
search = browser.find_element(By.XPATH,"//a[contains(text(),'Search')]")
search.click()

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(15)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//li[@class='ui-li-static ui-body-inherit ui-last-child']"))
    total_pages += element_count

    ids = browser.find_elements(By.XPATH, "//div[@class='selfServiceSearchRowRight']/h1")
    document_number = []
    for d in ids:
        document_number.append(d.text[0:10])
    #print(len(document_number))
    print('Document Numbers:', document_number)

    total = total + len(document_number)
    for i in range(len(document_number)):
        if i <= len(document_number):
            doc_no = browser.find_element(By.XPATH, "//h1[contains(text(),'" + document_number[i] + "')]")
            doc_no.click()
            time.sleep(6)
            view = browser.find_element(By.XPATH, "//h1[contains(text(),'" + document_number[i] + "')]//parent::div//descendant::a[@title='View Document']")
            view.click()
            time.sleep(25)
            browser.switch_to.frame(browser.find_element(By.XPATH, ".//iframe[@class='ss-pdfjs-lviewer']"))
            time.sleep(5)
            document = browser.find_element(By.XPATH, "//button[@id='download']")
            document.click()
            time.sleep(25)
            browser.switch_to.default_content()
            time.sleep(5)
            browser.back()
            time.sleep(10)
            try:
                doc_no_1 = browser.find_element(By.XPATH, "//h1[contains(text(),'" + document_number[i + 1] + "')]")
                browser.execute_script("arguments[0].scrollIntoView(true);", doc_no_1)
                time.sleep(6)
                browser.execute_script("window.scrollBy(0,-150)", "")
                time.sleep(5)
            except Exception as e:
                time.sleep(10)

    print('Successfully downloaded', len(document_number), 'documents in page', p)
    time.sleep(10)
    browser.execute_script("window.scrollBy(0,210)", "")
    try:
        next_button = browser.find_element(By.XPATH, "//a[contains(text(),'Next')]")
        time.sleep(5)
        next_button.click()
        time.sleep(15)
    except Exception as e:
        break
    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)
browser.quit()