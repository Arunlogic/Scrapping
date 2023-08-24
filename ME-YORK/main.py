from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

path  = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\ME-YORK'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path,options=chrome_options)

url = "https://www.searchiqs.com/MEYOR/LogIn.aspx"
browser.get(url)
browser.maximize_window()

# log in
time.sleep(4)
user_name =  browser.find_element(By.XPATH,"//input[@id='username']").send_keys('ionkings@giftelope.com')
time.sleep(2)
password =  browser.find_element(By.XPATH,"//input[@id='password']").send_keys('kings@123')
time.sleep(2)
log_in = browser.find_element(By.XPATH,"//input[@id='cmdLogin']").click()

time.sleep(4)
input_start_date = browser.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_txtFromDate']")
time.sleep(2)
input_start_date.send_keys('08/09/2017')
input_end_date = browser.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_txtThruDate']")
time.sleep(2)
input_end_date.send_keys('08/09/2017')


# document
time.sleep(2)
document = Select(browser.find_element(By.XPATH,"//select[@id='ContentPlaceHolder1_cboDocType']"))
document.select_by_visible_text('MORTGAGE')

# seaarch
time.sleep(2)
search = browser.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_cmdSearch']").click()
time.sleep(6)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='ContentPlaceHolder1_grdResults']/tbody"))
    total_pages += element_count

    ids = browser.find_elements(By.XPATH, "//table[@id='ContentPlaceHolder1_grdResults']/tbody/tr")
    a = []
    for doc in ids:
        if doc in browser.find_elements(By.XPATH, "//table[@id='ContentPlaceHolder1_grdResults']/tbody/tr[1]"):
            del doc
        else:
            a.append(doc)
    total += len(a)
    for i in range(len(a)):
        img = browser.find_element(By.XPATH,f"//table[@id='ContentPlaceHolder1_grdResults']/tbody/tr{[i + 2]}/td[1]/input[1]")
        img.click()
        time.sleep(5)
        browser.find_element(By.XPATH, "//button[@id='btnToolbarPrint']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[contains(text(),'Print/Download')]").click()
        time.sleep(8)
        browser.find_element(By.XPATH, "//button[@id='btnPPDDownloadPDF']").click()
        time.sleep(7)
        browser.back()
        time.sleep(3)

    print('Successfully downloaded', len(a), 'documents in page', p)

    time.sleep(5)
    try:
        next_button = browser.find_element(By.XPATH, "//a[@id='ContentPlaceHolder1_lbNext1'][@class='aspNetDisabled']")
        if next_button:
            break
        else:
            next_button.click()
            time.sleep(5)
    except Exception as e:
        break

    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

# DEED
time.sleep(2)
search = browser.find_element(By.XPATH,"//a[contains(text(),'Search')]").click()
time.sleep(4)

time.sleep(4)
input_start_date = browser.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_txtFromDate']")
time.sleep(2)
input_start_date.send_keys('08/09/2017')
input_end_date = browser.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_txtThruDate']")
time.sleep(2)
input_end_date.send_keys('08/09/2017')

# document
time.sleep(2)
document = Select(browser.find_element(By.XPATH,"//select[@id='ContentPlaceHolder1_cboDocType']"))
document.select_by_visible_text('DEED')

# search
time.sleep(2)
search = browser.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_cmdSearch']").click()
time.sleep(6)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='ContentPlaceHolder1_grdResults']/tbody"))
    total_pages += element_count

    ids = browser.find_elements(By.XPATH, "//table[@id='ContentPlaceHolder1_grdResults']/tbody/tr")
    a = []
    for doc in ids:
        if doc in browser.find_elements(By.XPATH, "//table[@id='ContentPlaceHolder1_grdResults']/tbody/tr[1]"):
            del doc
        else:
            a.append(doc)
    total+=len(a)
    for i in range(len(a)):
        img = browser.find_element(By.XPATH,f"//table[@id='ContentPlaceHolder1_grdResults']/tbody/tr{[i + 2]}/td[1]/input[1]")
        img.click()
        time.sleep(5)
        browser.find_element(By.XPATH, "//button[@id='btnToolbarPrint']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//button[contains(text(),'Print/Download')]").click()
        time.sleep(8)
        browser.find_element(By.XPATH, "//button[@id='btnPPDDownloadPDF']").click()
        time.sleep(7)
        browser.back()
        time.sleep(3)

    print('Successfully downloaded', len(a), 'documents in page', p)

    time.sleep(5)
    try:
        next_button = browser.find_element(By.XPATH, "//a[@id='ContentPlaceHolder1_lbNext1'][@class='aspNetDisabled']")
        if next_button:
            break
        else:
            next_button.click()
            time.sleep(5)
    except Exception as e:
        break

    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()

