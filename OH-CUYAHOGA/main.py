# Importing required libraries
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path  = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\OH-CUYAHOGA'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

# Opening browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

# Getting page
url = "https://cuyahoga.oh.publicsearch.us/search/advanced"
browser.get(url)
browser.maximize_window()

# Sign in
time.sleep(5)
sign_in = browser.find_element(By.XPATH,"//a[contains(text(),'Sign In')]")
sign_in.click()      # ## user name = ganisolo@superrito.com & password - Delete123
time.sleep(5)
user_name = browser.find_element(By.XPATH,"//input[@id='email']").send_keys('ganisolo@superrito.com')
time.sleep(4)
password = browser.find_element(By.XPATH,"//input[@class='password-input__input password-input__input--mask']").send_keys('Delete123')
time.sleep(4)
browser.find_element(By.XPATH,"//button[@class='user-form__submit-button user-form__button']").click()
print('Successfully Signed in')

def documents(docu_type):
    time.sleep(5)
    start_date = '09/11/2023'
    input_start_date = browser.find_element(By.XPATH,"//input[@id='recordedDateRange']")
    time.sleep(2)
    input_start_date.send_keys(Keys.CONTROL, 'a')
    time.sleep(2)
    input_start_date.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    input_start_date.send_keys(start_date)
    
    time.sleep(2)
    end_date = '09/14/2023'
    input_end_date = browser.find_element(By.XPATH,"//input[@aria-label='end date']")
    time.sleep(2)
    input_end_date.send_keys(Keys.CONTROL, 'a')
    time.sleep(2)
    input_end_date.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    input_end_date.send_keys(end_date)
    
    # doc_type
    if docu_type=='Mortgage':
        # Selecting document type

        time.sleep(5)
        document = browser.find_element(By.XPATH,"//input[@id='docTypes-input']").click()
        time.sleep(2)
        sending = browser.find_element(By.XPATH,"//input[@id='docTypes-input']").send_keys('MORTGAGE')
        time.sleep(2)

        mort = browser.find_elements(By.XPATH,"//div[@class='checkbox__controls']")
        time.sleep(1)
        length = 0
        for m in mort:
            length+=1
            if length ==1:
                m.click()
                break
            time.sleep(3)
    
    else:
        # Selecting document type

        time.sleep(3)
        document = browser.find_element(By.XPATH,"//input[@id='docTypes-input']").click()
        time.sleep(2)
        sending = browser.find_element(By.XPATH,"//input[@id='docTypes-input']").send_keys('DEED')
        time.sleep(2)

        mort = browser.find_elements(By.XPATH,"//div[@class='checkbox__controls']")
        time.sleep(2)
        length = 0
        for m in mort:
            length+=1
            if length ==1:
                m.click()
                break
            time.sleep(3)
        print('Successfully clicked DEED')
        
    # Search
    time.sleep(3)
    browser.execute_script("window.scrollBy(0,600)","")
    time.sleep(3)
    search = browser.find_element(By.XPATH,"//button[@class='css-1aabfxg']")
    search.click()
    time.sleep(12)
    
    # download
    total_pages = 0
    total = 0
    p = 0
    while True:
        time.sleep(8)
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
        links = browser.find_element(By.XPATH,"//td[@class='col-7']").click()
        time.sleep(8)
        for i in range(len(hrefs)):
            download = browser.find_element(By.XPATH,"//button[contains(text(),'Download')]")
            download.click()
            time.sleep(28)
            try:
                next_result = browser.find_element(By.XPATH,"//button[contains(text(),'Next Result')]")
                next_result.click()
                time.sleep(10)
            except Exception as e:
                break

        back_to_results = browser.find_element(By.XPATH,"//button[contains(text(),'Back to Results')]").click() 
        time.sleep(8)
        
        print('Successfully downloaded',len(hrefs),'documents in page',p)


        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

        try:
            next_button = browser.find_element(By.XPATH,"//button[@aria-disabled='false'][@aria-label='next page']")
            next_button.click()
        except Exception as e:
            break
        time.sleep(5)
    print('Total Pages: ',total_pages)
    print('Total downloaded documents:',total)
    
    edit = browser.find_element(By.XPATH,"//div[@class='search-results-header__row']/div/div[4]/a/div/img").click()
    time.sleep(8)
    removing_type = browser.find_elements(By.XPATH,"//button[@class='react-tokenized-select__remove-button']")
    for re in removing_type:
        re.click()
        time.sleep(3)
    
documents('Mortgage')

#documents('Deed')

browser.quit()


    
