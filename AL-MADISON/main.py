from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options


path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\AL MADISON'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path,options=chrome_options)

url = "https://madisonprobate.countygovservices.com/Search/SearchType?key=all_books"
browser.get(url)
browser.maximize_window()

# log in
time.sleep(6)
mail = browser.find_element(By.XPATH,"//input[@id='email']").send_keys('yibikek815@datakop.com')
time.sleep(3)
password = browser.find_element(By.XPATH,"//input[@id='password']").send_keys('yibikek815@123')
time.sleep(3)
keep_remember = browser.find_element(By.XPATH,"//input[@id='rememberMe']").click()
time.sleep(2)
sign_in = browser.find_element(By.XPATH,"//button[contains(text(),'Sign in')]").click()

# selecting instrument type
time.sleep(8)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
drop_down = browser.find_element(By.XPATH,"//*[@id='instrumenttypecombo']/div/div[3]/input").click()
time.sleep(2)
document = browser.find_element(By.XPATH,"//li[contains(text(),'Mortgage (MORTGAGE)')][4]").click()
time.sleep(4)

# Recording date

input_start_date = browser.find_element(By.XPATH,"//input[@id='startdatepicker']")
input_start_date.click()
start_date = '02/05/2023'
time.sleep(3)
input_start_date.send_keys(start_date)

time.sleep(3)
input_end_date = browser.find_element(By.XPATH,"//input[@id='enddatepicker']")
input_end_date.click()
end_date = '02/07/2023'
time.sleep(3)
input_end_date.send_keys(end_date)
time.sleep(2)

# Click to search  records
time.sleep(3)
search_button = browser.find_element(By.XPATH,"//div[contains(text(),'Search')]/i")
search_button.click()
time.sleep(5)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p+1
    print('Scrapping page:',p)
    element_count = len(browser.find_elements(By.XPATH,"//*[@id='gridResults']"))
    total_pages += element_count
    try:
        links = browser.find_elements(By.XPATH,"//*[@id='gridResults']/tbody/tr/td[5]/div")
        hrefs = []
        for c in links:
            hrefs.append(c.text)
        print(len(hrefs))
        print(hrefs)
        total = total+len(hrefs)
        for i in range(len(hrefs)):
            if i<=len(hrefs):
                doc_name = browser.find_element(By.XPATH,"//div[contains(text(),'"+hrefs[i]+"')]").click()
                time.sleep(2)
                view = browser.find_element(By.XPATH,"//div[contains(text(),'"+hrefs[i]+"')]//ancestor::tr/td/div/button").click()
                parent_handle = browser.current_window_handle
                all_handles = browser.window_handles
                for handle in all_handles:
                    if handle!=parent_handle:
                        browser.switch_to.window(handle)
                        time.sleep(3)
                        browser.execute_script("window.scrollTo(0,150);")
                        time.sleep(3)
                        download_instrument = browser.find_element(By.XPATH,"//div[contains(text(),'Download Instrument')]").click()
                        time.sleep(5)
                        download = browser.find_element(By.XPATH,"//div[@class='btn btn-primary']").click()
                        time.sleep(25)
                        browser.close()
                browser.switch_to.window(parent_handle)
                try:
                    doc_no_1 = browser.find_element(By.XPATH,"//div[contains(text(),'"+hrefs[i+1]+"')]")
                    browser.execute_script("arguments[0].scrollIntoView(true);",doc_no_1)
                    time.sleep(3)
                    browser.execute_script("window.scrollBy(0,-60)","")
                    time.sleep(3)
                except Exception as e:
                    time.sleep(5)
        time.sleep(6)
        print('Successfully downloaded',len(hrefs),'documents in page',p)
    except Exception as e:
        break
    time.sleep(6)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if not browser.find_elements(By.XPATH,"//span[@class='ui-iggrid-nextpagelabel']"):
        break
    time.sleep(3)
    browser.find_element(By.XPATH,"//span[@class='ui-iggrid-nextpagelabel']").click()
    time.sleep(2)
    browser.execute_script("window.scrollTo(0,0);")
    time.sleep(5)
print('Total Pages: ',total_pages)
print('Total downloaded documents:',total)

# DEED

browser.back()

# selecting instrument type
time.sleep(4)
drop_down = browser.find_element(By.XPATH,"//*[@id='instrumenttypecombo']/div/div[3]/input").click()
time.sleep(2)
document = browser.find_element(By.XPATH,"//li[contains(text(),'Deed (DEED)')][3]").click()
time.sleep(4)

# Click to search  records
time.sleep(3)
search_button = browser.find_element(By.XPATH,"//div[contains(text(),'Search')]/i")
search_button.click()
time.sleep(5)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p+1
    print('Scrapping page:',p)
    element_count = len(browser.find_elements(By.XPATH,"//*[@id='gridResults']"))
    total_pages += element_count
    try:
        links = browser.find_elements(By.XPATH,"//*[@id='gridResults']/tbody/tr/td[5]/div")
        hrefs = []
        for c in links:
            hrefs.append(c.text)
        print(len(hrefs))
        print(hrefs)
        total = total+len(hrefs)
        for i in range(len(hrefs)):
            if i<=len(hrefs):
                doc_name = browser.find_element(By.XPATH,"//div[contains(text(),'"+hrefs[i]+"')]").click()
                time.sleep(2)
                view = browser.find_element(By.XPATH,"//div[contains(text(),'"+hrefs[i]+"')]//ancestor::tr/td/div/button").click()
                parent_handle = browser.current_window_handle
                all_handles = browser.window_handles
                for handle in all_handles:
                    if handle!=parent_handle:
                        browser.switch_to.window(handle)
                        time.sleep(3)
                        browser.execute_script("window.scrollTo(0,150);")
                        time.sleep(3)
                        download_instrument = browser.find_element(By.XPATH,"//div[contains(text(),'Download Instrument')]").click()
                        time.sleep(5)
                        download = browser.find_element(By.XPATH,"//div[@class='btn btn-primary']").click()
                        time.sleep(25)
                        browser.close()
                browser.switch_to.window(parent_handle)
                try:
                    doc_no_1 = browser.find_element(By.XPATH,"//div[contains(text(),'"+hrefs[i+1]+"')]")
                    browser.execute_script("arguments[0].scrollIntoView(true);",doc_no_1)
                    time.sleep(3)
                    browser.execute_script("window.scrollBy(0,-60)","")
                    time.sleep(3)
                except Exception as e:
                    time.sleep(5)
        time.sleep(6)
        print('Successfully downloaded',len(hrefs),'documents in page',p)
    except Exception as e:
        break
    time.sleep(6)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if not browser.find_elements(By.XPATH,"//span[@class='ui-iggrid-nextpagelabel']"):
        break
    time.sleep(3)
    browser.find_element(By.XPATH,"//span[@class='ui-iggrid-nextpagelabel']").click()
    time.sleep(2)
    browser.execute_script("window.scrollTo(0,0);")
    time.sleep(5)
print('Total Pages: ',total_pages)
print('Total downloaded documents:',total)

browser.quit()