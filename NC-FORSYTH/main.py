from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"
path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\NC-FORSYTH'

chrome_options = Options()

chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})
# Opening browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "http://www.forsythdeeds.com/disclaimer.php"
browser.get(url)
browser.maximize_window()

# accept
time.sleep(4)
while True:
    try:
        accept = browser.find_element(By.XPATH, "//input[@id='Accept']").click()
    except Exception as e:
        break
    break

time.sleep(4)
input_start_date = browser.find_element(By.ID, "start_date")
input_start_date.click()
start_date = '08/02/2023'
time.sleep(2)
input_start_date.send_keys(start_date)

time.sleep(2)
input_end_date = browser.find_element(By.ID, "end_date")
input_end_date.click()
end_date = '08/02/2023'
time.sleep(3)
input_end_date.send_keys(end_date)
time.sleep(2)

# bood type

book_type = Select(browser.find_element(By.XPATH, "//select[@id='bookcode']"))
book_type.select_by_visible_text('REAL ESTATE')
time.sleep(3)

dt = browser.find_element(By.XPATH, "//input[@id='D/T']").click()
time.sleep(2)

mtg = browser.find_element(By.XPATH, "//input[@id='MTG']").click()
time.sleep(3)

# search
search = browser.find_element(By.XPATH,
                              "//form[@id='frmlookup_form']/table/tbody/tr[4]/td[3]/table/tbody/tr[4]/td/input[1]")
search.click()
time.sleep(5)

# check all
check_all = browser.find_element(By.XPATH, "//div[@align='center'][2]/table/tbody/tr[3]/td/input").click()
time.sleep(3)

display_details = browser.find_element(By.XPATH, "//div[@align='center'][2]/table/tbody/tr[3]/td/input[3]").click()
time.sleep(3)

# download

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "/html/body/table/tbody/tr/td/table[1]/tbody"))
    total_pages += element_count
    records = browser.find_elements(By.XPATH, "//a[contains(text(),'PDF')]")
    total += len(records)

    for pdf in records:
        browser.execute_script("arguments[0].scrollIntoView(true);", pdf)
        pdf.click()
        time.sleep(20)

    print('Successfully downloaded', len(records), 'documents in page', p)
    time.sleep(2)
    break
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

### DEED

# back to search

time.sleep(3)
back_search = browser.find_element(By.XPATH, "//input[@value='Search Screen']").click()

time.sleep(3)
input_start_date = browser.find_element(By.ID, "start_date")
input_start_date.click()
start_date = '08/02/2023'
time.sleep(2)
input_start_date.send_keys(start_date)

time.sleep(2)
input_end_date = browser.find_element(By.ID, "end_date")
input_end_date.click()
end_date = '08/02/2023'
time.sleep(3)
input_end_date.send_keys(end_date)
time.sleep(2)

# bood type

book_type = Select(browser.find_element(By.XPATH, "//select[@id='bookcode']"))
book_type.select_by_visible_text('REAL ESTATE')
time.sleep(3)

dt = browser.find_element(By.XPATH, "//input[@id='D/T']").click()
time.sleep(2)

mtg = browser.find_element(By.XPATH, "//input[@id='MTG']").click()
time.sleep(3)

deed = browser.find_element(By.XPATH, "//input[@id='DEED']").click()
time.sleep(3)

# search
search = browser.find_element(By.XPATH,
                              "//form[@id='frmlookup_form']/table/tbody/tr[4]/td[3]/table/tbody/tr[4]/td/input[1]")
search.click()
time.sleep(5)

# check all
check_all = browser.find_element(By.XPATH, "//div[@align='center'][2]/table/tbody/tr[3]/td/input").click()
time.sleep(3)

display_details = browser.find_element(By.XPATH, "//div[@align='center'][2]/table/tbody/tr[3]/td/input[3]").click()
time.sleep(3)

# download

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "/html/body/table/tbody/tr/td/table[1]/tbody"))
    total_pages += element_count
    records = browser.find_elements(By.XPATH, "//a[contains(text(),'PDF')]")
    total += len(records)

    for pdf in records:
        browser.execute_script("arguments[0].scrollIntoView(true);", pdf)
        pdf.click()
        time.sleep(20)

    print('Successfully downloaded', len(records), 'documents in page', p)
    time.sleep(2)
    break
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()