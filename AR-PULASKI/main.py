from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\AR-PULASKI'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "http://69.152.184.8/search/"
browser.get(url)
browser.maximize_window()

# accept
time.sleep(4)
accept = browser.find_element(By.XPATH, "//input[@id='Accept']").click()

time.sleep(3)
instrument = browser.find_element(By.XPATH, "//div[@id='accordion']/div[2]/h3/a/img").click()
time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//input[@id='start_date_instrumenttype']")
input_start_date.clear()
start_date = '01/18/2023'
time.sleep(2)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH, "//input[@id='end_date_instrumenttype']")
input_end_date.clear()
end_date = '01/18/2023'
time.sleep(2)
input_end_date.send_keys(end_date)

# document type
time.sleep(3)
mortgage = browser.find_element(By.XPATH, "//div[@id='instrumenttype_category_containerDiv']/input[36]").click()
time.sleep(2)
deed = browser.find_element(By.XPATH, "//div[@id='instrumenttype_category_containerDiv']/input[87]").click()
time.sleep(3)

search = browser.find_element(By.XPATH, "//div[@id='tabs-2']/div[1]/a[1]/img").click()
time.sleep(4)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0

while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='content_frame']"))
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='results']/tbody"))
    total_pages += element_count
    ids = browser.find_elements(By.XPATH, "//table[@id='results']/tbody/tr/td[9]/a")
    print(len(ids))
    total = total + len(ids)

    for img in ids:
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        img.click()
        time.sleep(14)

    print('Successfully downloaded', len(ids), 'documents in page', p)
    time.sleep(3)
    try:
        next_button = browser.find_element(By.XPATH, "//a[@class='paginate_button next'][@id='results_next']").click()
    except Exception as e:
        break
    time.sleep(5)
    browser.switch_to.default_content()

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()