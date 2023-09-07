from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pyao

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\TX-NUECES'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "https://nueces.tx.publicsearch.us/search/advanced"
browser.get(url)
browser.maximize_window()

# advance search
time.sleep(5)
advance_search = browser.find_element(By.XPATH, "//a[contains(text(),'Advanced Search')]")
advance_search.click()

# sign in
time.sleep(4)
sign_in = browser.find_element(By.XPATH,
                               "//a[contains(text(),'Sign In')]")  ## user name = ganisolo@superrito.com & password - Delete123
sign_in.click()
time.sleep(3)
user_name = browser.find_element(By.XPATH, "//input[@id='email']").send_keys('ganisolo@superrito.com')
time.sleep(2)
password = browser.find_element(By.XPATH,
                                "//input[@class='password-input__input password-input__input--mask']").send_keys(
    'Delete123')
time.sleep(3)
browser.find_element(By.XPATH, "//button[@class='user-form__submit-button user-form__button']").click()
print('Successfully Signed in')

time.sleep(5)
cart = browser.find_element(By.XPATH, "//div[@data-testid='cart']")
cart.click()
time.sleep(3)
while True:
    try:
        clear_cart = browser.find_element(By.XPATH, "//button[contains(text(),'Empty Shopping Cart')]")
        clear_cart.click()
    except Exception as e:
        break

time.sleep(3)
close_cart = browser.find_element(By.XPATH,
                                  "//div[@class='css-tr1wtg css-tr1wtg--active']//parent::li//descendant::button[@data-testid='workspaceCloseButton']")
close_cart.click()

time.sleep(3)
start_date = '09/20/2022'
input_start_date = browser.find_element(By.XPATH, "//input[@id='recordedDateRange']")
time.sleep(2)
input_start_date.send_keys(Keys.CONTROL, 'a')
time.sleep(2)
input_start_date.send_keys(Keys.BACKSPACE)
time.sleep(2)
input_start_date.send_keys(start_date)

time.sleep(2)
end_date = '09/20/2022'
input_end_date = browser.find_element(By.XPATH, "//input[@aria-label='end date']")
time.sleep(2)
input_end_date.send_keys(Keys.CONTROL, 'a')
time.sleep(2)
input_end_date.send_keys(Keys.BACKSPACE)
time.sleep(2)
input_end_date.send_keys(end_date)

# Selecting document type

dtypes_index = [2, 3]
for i in range(len(dtypes_index)):
    document_1 = browser.find_element(By.XPATH, "//input[@id='docTypes-input']").click()
    time.sleep(2)
    sending_1 = browser.find_element(By.XPATH, "//input[@id='docTypes-input']").send_keys('equity')
    time.sleep(2)
    security_1 = browser.find_elements(By.XPATH, "//div[@class='checkbox__controls']")
    time.sleep(2)
    length = 0
    for m in security_1:
        length += 1
        if length == dtypes_index[i]:
            m.click()
    time.sleep(3)

time.sleep(3)
dtypes_index = [3]
for i in range(len(dtypes_index)):
    document = browser.find_element(By.XPATH, "//input[@id='docTypes-input']").click()
    time.sleep(2)
    sending = browser.find_element(By.XPATH, "//input[@id='docTypes-input']").send_keys('DEED OF TRUST')
    time.sleep(2)
    mort = browser.find_elements(By.XPATH, "//div[@class='checkbox__controls']")
    time.sleep(2)
    length = 0
    for m in mort:
        length += 1
        if length == dtypes_index[i]:
            m.click()
    time.sleep(3)

dtypes_index = [1]
for i in range(len(dtypes_index)):
    document_1 = browser.find_element(By.XPATH, "//input[@id='docTypes-input']").click()
    time.sleep(2)
    sending_1 = browser.find_element(By.XPATH, "//input[@id='docTypes-input']").send_keys('extension')
    time.sleep(2)
    security_1 = browser.find_elements(By.XPATH, "//div[@class='checkbox__controls']")
    time.sleep(2)
    length = 0
    for m in security_1:
        length += 1
        if length == dtypes_index[i]:
            m.click()
    time.sleep(3)

print('Successfully clicked data types')

# Search
time.sleep(4)
browser.execute_script("window.scrollBy(0,600)", "")
time.sleep(2)
search = browser.find_element(By.XPATH, "//button[@class='css-1aabfxg']")
search.click()
time.sleep(10)

links = browser.find_elements(By.XPATH, "//td[@class='col-7']")
hrefs = []
for c in links:
    hrefs.append(c.text)
print(len(hrefs))
print(hrefs)

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='a11y-table']"))
    total_pages += element_count
    time.sleep(4)
    links = len(browser.find_elements(By.XPATH, "//td[@class='col-7']"))
    link = browser.find_element(By.XPATH, "//td[@class='col-7']")
    link.click()
    time.sleep(5)

    for i in range(links):
        if i < links:
            add_to_cart = browser.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]").click()
            time.sleep(4)
            total += 1
            add = browser.find_element(By.XPATH, "//span[contains(text(),'Add')]").click()
            time.sleep(4)
            try:
                next_result = browser.find_element(By.XPATH, "//button[contains(text(),'Next Result')]")
                next_result.click()
                time.sleep(8)
            except Exception as e:
                break
    time.sleep(3)

    print('Successfully', links, 'documents added to cart')
    back = browser.find_element(By.XPATH, "//button[contains(text(),'Back to Results')]").click()
    time.sleep(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    try:
        next_button = browser.find_element(By.XPATH, "//button[@aria-disabled='false'][@aria-label='next page']")
        next_button.click()
    except Exception as e:
        break
    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total added documents:', total)

time.sleep(5)
cart = browser.find_element(By.XPATH, "//div[@data-testid='cart']")
time.sleep(5)
cart.click()

time.sleep(5)
place_order = browser.find_element(By.XPATH, "//a[@data-testid='orderButton']")
place_order.click()

time.sleep(12)
download_all = browser.find_element(By.XPATH, "//a[@class='css-sj7ztf'][1]")
download_all.click()
time.sleep(2 * 60)
print('Successfully downloaded', total, 'documents in', total_pages, 'pages')

close_cart = browser.find_element(By.XPATH,
                                  "//div[@class='css-tr1wtg css-tr1wtg--active']//parent::li//descendant::button[@data-testid='workspaceCloseButton']")
close_cart.click()
time.sleep(4)

### DEED

back = browser.find_element(By.XPATH, "//div[@class='search-results-header__edit-search']/a/div/img").click()

time.sleep(5)
browser.execute_script("window.scrollBy(0,750)", "")
removing_type = browser.find_elements(By.XPATH, "//button[@class='react-tokenized-select__remove-button']/img")
removing_type.reverse()
for r in range(len(removing_type)):
    removing_type[r].click()
    time.sleep(3)

# Selecting deed document type

dtypes_index_1 = [6, 14]
for i in range(len(dtypes_index_1)):
    document_1 = browser.find_element(By.XPATH, "//input[@id='docTypes-input']").click()
    time.sleep(2)
    sending_1 = browser.find_element(By.XPATH, "//input[@id='docTypes-input']").send_keys('deed')
    time.sleep(2)
    security_1 = browser.find_elements(By.XPATH, "//div[@class='checkbox__controls']")
    time.sleep(2)
    length = 0
    for m in security_1:
        length += 1
        if length == dtypes_index_1[i]:
            m.click()
    time.sleep(3)

print('Successfully clicked data types')

# Search
time.sleep(5)
browser.execute_script("window.scrollBy(0,600)", "")
time.sleep(3)
search = browser.find_element(By.XPATH, "//button[@class='css-1aabfxg']")
search.click()
time.sleep(15)

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@class='a11y-table']"))
    total_pages += element_count
    time.sleep(4)
    links = len(browser.find_elements(By.XPATH, "//td[@class='col-7']"))
    link = browser.find_element(By.XPATH, "//td[@class='col-7']")
    link.click()
    time.sleep(5)

    for i in range(links):
        if i < links:
            add_to_cart = browser.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]").click()
            time.sleep(4)
            total += 1
            add = browser.find_element(By.XPATH, "//span[contains(text(),'Add')]").click()
            time.sleep(4)
            try:
                next_result = browser.find_element(By.XPATH, "//button[contains(text(),'Next Result')]")
                next_result.click()
                time.sleep(8)
            except Exception as e:
                break
    time.sleep(3)

    print('Successfully', links, 'documents added to cart')
    back = browser.find_element(By.XPATH, "//button[contains(text(),'Back to Results')]").click()
    time.sleep(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    try:
        next_button = browser.find_element(By.XPATH, "//button[@aria-disabled='false'][@aria-label='next page']")
        next_button.click()
    except Exception as e:
        break
    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total added documents:', total)

time.sleep(5)
cart = browser.find_element(By.XPATH, "//div[@data-testid='cart']")
time.sleep(5)
cart.click()

time.sleep(5)
place_order = browser.find_element(By.XPATH, "//a[@data-testid='orderButton']")
place_order.click()

time.sleep(12)
download_all = browser.find_element(By.XPATH, "//a[@class='css-sj7ztf'][1]")
download_all.click()
time.sleep(2 * 60)
print('Successfully downloaded', total, 'documents in', total_pages, 'pages')
close_cart = browser.find_element(By.XPATH,
                                  "//div[@class='css-tr1wtg css-tr1wtg--active']//parent::li//descendant::button[@data-testid='workspaceCloseButton']")
close_cart.click()
time.sleep(2)

browser.quit()