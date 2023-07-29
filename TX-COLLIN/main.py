# Importing required libraries

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\TX-COLLIN'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "https://collin.tx.publicsearch.us/"
browser.get(url)
browser.maximize_window()

# Sign in
time.sleep(5)
sign_in = browser.find_element(By.XPATH,"//a[contains(text(),'Sign In')]") ## user name = ganisolo@superrito.com & password - Delete123
sign_in.click()
time.sleep(4)
user_name = browser.find_element(By.XPATH,"//input[@id='email']").send_keys('ganisolo@superrito.com')
time.sleep(4)
password = browser.find_element(By.XPATH,"//input[@class='password-input__input password-input__input--mask']").send_keys('Delete123')
time.sleep(5)
browser.find_element(By.XPATH,"//button[@class='user-form__submit-button user-form__button']").click()
print('Successfully Signed in')

time.sleep(5)
input_start_date = browser.find_element(By.XPATH,"//input[@data-tip='Starting Recorded Date']")
input_start_date.clear()
start_date = '04/22/2022'
time.sleep(5)
input_start_date.send_keys(start_date)

time.sleep(5)
input_end_date = browser.find_element(By.XPATH,"//input[@data-tip='Ending Recorded Date']")
input_end_date.clear()
end_date = '04/25/2022'
time.sleep(5)
input_end_date.send_keys(end_date)

# search
time.sleep(5)
search = browser.find_element(By.XPATH,"//button[@data-testid='searchSubmitButton']")
search.click()

# selecting document type
time.sleep(15)
document = browser.find_element(By.XPATH,"//input[@placeholder='Filter Document Types']").click()
time.sleep(5)
sending = browser.find_element(By.XPATH,"//input[@placeholder='Filter Document Types']").send_keys('DEED OF TRUST')
time.sleep(5)
mort = browser.find_elements(By.XPATH,"//div[@class='checkbox__controls']")
time.sleep(3)
length = 0
for m in mort:
    length+=1
    if length ==1:
        m.click()
        break
    time.sleep(3)
print('Successfully clicked the DEED OF TRUST datatype')

# To download
total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p+1
    print('Scrapping page:',p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='a11y-table']"))
    total_pages += element_count
    
    links = browser.find_elements(By.XPATH,"//td[@class='col-7']")
    hrefs = []
    for c in links:
        hrefs.append(c.text)
    print(hrefs)
    
    total = total+len(hrefs)
    
    for i in range(len(hrefs)):
        doc_no = browser.find_element(By.XPATH,"//span[contains(text(),'"+hrefs[i]+"')]")
        doc_no.click()
        time.sleep(6)
        browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        download = browser.find_element(By.XPATH,"//button[contains(text(),'Download')]")
        download.click()
        time.sleep(18)
        browser.back()
        time.sleep(5)
    
    print('Successfully downloaded',len(hrefs),'documents in page',p)
   
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    
    try:
        next_button = browser.find_element(By.XPATH,"//button[@class='pagination__page-jump'][@aria-label='next page']")
        time.sleep(5)
        next_button.click()
    except Exception as e:
        break
    time.sleep(5)
print('Total Pages: ',total_pages)
print('Total downloaded documents:',total)

#Deed

# Deselecting document type
time.sleep(5)
document = browser.find_element(By.XPATH,"//input[@placeholder='Filter Document Types']").click()
time.sleep(5)
sending = browser.find_element(By.XPATH,"//input[@placeholder='Filter Document Types']").send_keys('DEED OF TRUST')
time.sleep(5)

mort = browser.find_elements(By.XPATH,"//div[@class='checkbox__controls']")
time.sleep(3)
length = 0
for m in mort:
    length+=1
    if length ==1:
        m.click()
        break
    time.sleep(3)
print('Successfully deselected the DEED OF TRUST datatype')

# selecting document type
time.sleep(5)
document = browser.find_element(By.XPATH,"//input[@placeholder='Filter Document Types']").click()
time.sleep(5)
sending = browser.find_element(By.XPATH,"//input[@placeholder='Filter Document Types']").send_keys('DEED')
time.sleep(5)

mort = browser.find_elements(By.XPATH,"//div[@class='checkbox__controls']")
time.sleep(3)
length = 0
for m in mort:
    length+=1
    if length ==1:
        m.click()
        break
    time.sleep(3)
print('Successfully selected the DEED datatype')

# To download
total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p+1
    print('Scrapping page:',p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='a11y-table']"))
    total_pages += element_count
    
    links = browser.find_elements(By.XPATH,"//td[@class='col-7']")
    hrefs = []
    for c in links:
        hrefs.append(c.text)
    print(hrefs)
    
    total = total+len(hrefs)
    
    for i in range(len(hrefs)):
        doc_no = browser.find_element(By.XPATH,"//span[contains(text(),'"+hrefs[i]+"')]")
        doc_no.click()
        time.sleep(6)
        browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        download = browser.find_element(By.XPATH,"//button[contains(text(),'Download')]")
        download.click()
        time.sleep(18)
        browser.back()
        time.sleep(5)
    
    print('Successfully downloaded',len(hrefs),'documents in page',p)
   
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    
    try:
        next_button = browser.find_element(By.XPATH,"//button[@class='pagination__page-jump'][@aria-label='next page']")
        time.sleep(5)
        next_button.click()
    except Exception as e:
        break
    time.sleep(5)
print('Total Pages: ',total_pages)
print('Total downloaded documents:',total)
browser.quit()
