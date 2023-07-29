# Importing required libraries
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\TX - HARRIS'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

# Opening brower
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

# Getting page
url = "https://www.cclerk.hctx.net/applications/websearch/Home.aspx"
browser.get(url)
browser.maximize_window()

# log in
time.sleep(5)
log_in = browser.find_element(By.XPATH,"//a[@id='ctl00_LoginStatus1']") # User Name: Harris12   Password: delete@321 
log_in.click()
time.sleep(4)
user_name = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_Login1_UserName']").send_keys('Harris12')
time.sleep(4)
password = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_Login1_Password']").send_keys('delete@321')
time.sleep(5)
checkbox = browser.find_element(By.XPATH,"//input[@type='checkbox']")
checkbox.click()
time.sleep(2)
log_in_1 = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_Login1_LoginButton']")
log_in_1.click()

# property records & real property
time.sleep(5)
property_records = browser.find_element(By.XPATH,"//a[contains(text(),'Property Records')]").click()
time.sleep(2)
real_property = browser.find_element(By.XPATH,"//a[contains(text(),'Real Property')]")
real_property.click()

# From date
time.sleep(4)
input_start_date = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtFrom']")
time.sleep(2)
input_start_date.send_keys('01/07/2020')
time.sleep(2)

# End date
time.sleep(4)
input_end_date = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtTo']")
time.sleep(2)
input_end_date.send_keys('01/07/2020')
time.sleep(2)

# Selecting instrument type
time.sleep(5)
instrument_type = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtInstrument']")
instrument_type.send_keys('D/T')  # Deed of Trust
time.sleep(2)

# Search
time.sleep(3)
search = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_btnSearch']")
search.click()
time.sleep(10)

# Counting the total pages & Counting the total documents & How much documents it's downloaded
total_pages = 0
total_downloaded = 0
p = 0
while True:
    time.sleep(7)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_UpdatePanelAddtoCart']"))
    total_pages += element_count
    try:
        flim_code = browser.find_elements(By.XPATH, "//a[contains(text(),'RP')]")
        codes = []
        for code in flim_code:
            codes.append(code.text)

        total_downloaded = total_downloaded + len(codes)

        for i in range(len(codes)):
            click_form = browser.find_element(By.LINK_TEXT, codes[i])
            click_form.click()
            time.sleep(12)

        print('Successfully downloaded', len(codes), 'documents in page', p)
        scroll_top = browser.find_element(By.XPATH, "//div[@title='Scroll Back to Top']").click()
        time.sleep(5)
        try:
            next_button = browser.find_element(By.XPATH, "//input[@value='Next']")
            time.sleep(4)
            next_button.click()
        except Exception as e:
            break
        time.sleep(5)
    except Exception as e:
        break
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total_downloaded)
time.sleep(6)

# For Warranty Deed

# property records & real property
time.sleep(5)
property_records = browser.find_element(By.XPATH,"//a[contains(text(),'Property Records')]").click()
time.sleep(2)
real_property = browser.find_element(By.XPATH,"//a[contains(text(),'Real Property')]")
real_property.click()

# From date
time.sleep(4)
input_start_date = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtFrom']")
time.sleep(2)
input_start_date.send_keys('01/07/2020')
time.sleep(2)

# End date
time.sleep(4)
input_end_date = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtTo']")
time.sleep(2)
input_end_date.send_keys('01/07/2020')
time.sleep(2)

# Selecting instrument type
time.sleep(5)
instrument_type = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtInstrument']")
instrument_type.send_keys('W/D')  # Warranty Deed
time.sleep(2)

# Search
time.sleep(3)
search = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_btnSearch']")
search.click()
time.sleep(10)

# Counting the total pages & Counting the total documents & How much documents it's downloaded
total_pages = 0
total_downloaded = 0
p = 0
while True:
    time.sleep(7)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_UpdatePanelAddtoCart']"))
    total_pages += element_count
    try:
        flim_code = browser.find_elements(By.XPATH, "//a[contains(text(),'RP')]")
        codes = []
        for code in flim_code:
            codes.append(code.text)

        total_downloaded = total_downloaded + len(codes)

        for i in range(len(codes)):
            click_form = browser.find_element(By.LINK_TEXT, codes[i])
            click_form.click()
            time.sleep(12)

        print('Successfully downloaded', len(codes), 'documents in page', p)
        scroll_top = browser.find_element(By.XPATH, "//div[@title='Scroll Back to Top']").click()
        time.sleep(5)
        try:
            next_button = browser.find_element(By.XPATH, "//input[@value='Next']")
            time.sleep(4)
            next_button.click()
        except Exception as e:
            break
        time.sleep(5)
    except Exception as e:
        break
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total_downloaded)
time.sleep(6)

browser.quit()
