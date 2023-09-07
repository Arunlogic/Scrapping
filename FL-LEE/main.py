from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\FL-LEE'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.prompt_for_download': False,
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf,
    "download.directory_upgrade": True,
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "https://or.leeclerk.org/LandMarkWeb/"
browser.get(url)
browser.maximize_window()

time.sleep(5)
document = browser.find_element(By.XPATH, "//img[@alt='Document Search Icon']")
document.click()

time.sleep(3)
accept = browser.find_element(By.XPATH, "//a[contains(text(),'Accept')]")
accept.click()

# select
time.sleep(4)
select = browser.find_element(By.XPATH, "//a[@id='documentTypeSelection-DocumentType']")
select.click()

# selecting document type
time.sleep(4)
mortgage = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-59']").click()
time.sleep(3)
m_1 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-194']").click()
time.sleep(3)
m_2 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-60']").click()
time.sleep(3)
m_3 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-61']").click()
time.sleep(3)
m_4 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-159']").click()
time.sleep(3)
m_5 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-160']").click()

# clicking select
time.sleep(3)
sele = 0
select1 = browser.find_elements(By.XPATH, "//a[@class='btn btn-primary'][@data-dismiss='modal']")
for ele in select1:
    sele += 1
    if sele == 2:
        ele.click()
print('Successfully selected document types')

# Recording date
time.sleep(3)
input_start_date = browser.find_element(By.XPATH, "//input[@id='beginDate-DocumentType']")
input_start_date.clear()
start_date = '09/21/2022'
time.sleep(2)
input_start_date.send_keys(start_date)

input_end_date = browser.find_element(By.XPATH, "//input[@id='endDate-DocumentType']")
input_end_date.clear()
end_date = '09/21/2022'
time.sleep(2)
input_end_date.send_keys(end_date)
time.sleep(2)

# submit
time.sleep(1)
submit = browser.find_element(By.XPATH, "//a[@id='submit-DocumentType']")
submit.click()

time.sleep(5)
browser.execute_script("window.scrollBy(0,220)", "")

links = browser.find_elements(By.XPATH, "//td[@class='tablecell nowordbreak'][3]")
hrefs = []
for c in links:
    hrefs.append(c.text)
print(len(hrefs))
print(hrefs)

# Counting the total pages & Counting the total mortgage documents & How much documents it's downloaded

time.sleep(5)
total_pages = 0
total_downloaded = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='resultsTable']"))
    total_pages += element_count
    display_records = Select(browser.find_element(By.XPATH, "//select[@name='resultsTable_length']"))
    display_records.select_by_visible_text('100')
    time.sleep(4)
    links = browser.find_elements(By.XPATH, "//td[@class='tablecell nowordbreak'][3]")
    hrefs = []
    for c in links:
        hrefs.append(c.text)
    total_downloaded = total_downloaded + len(hrefs)

    for i in range(len(hrefs)):
        click_form = browser.find_element(By.XPATH, "//td[contains(text(),'" + hrefs[i] + "')]")
        click_form.click()
        time.sleep(4)
        click_view = browser.find_element(By.XPATH, "//a[@id='idViewGroup']")
        click_view.click()
        time.sleep(3)
        view_all_pages = browser.find_element(By.XPATH, "//li[@id='DocumentViewButtonAll']")
        view_all_pages.click()
        time.sleep(12)
        get_back = browser.find_element(By.XPATH, "//a[@id='returnToSearchButton']").click()
        time.sleep(5)

    print('Successfully downloaded', len(hrefs), 'documents in page', p)
    try:
        time.sleep(3)
        next_page = browser.find_element(By.XPATH,
                                         "//a[@class='paginate_button next' and not(@id='resultsTable_next')]")
        next_page.click()
    except Exception as e:
        break
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total_downloaded)

### DEED

time.sleep(5)
doc_no_1 = browser.find_element(By.XPATH, "//a[@id='searchCriteriaName-tab']")
browser.execute_script("arguments[0].scrollIntoView(true);", doc_no_1)
time.sleep(4)
browser.execute_script("window.scrollBy(0,-100)", "")

# select
time.sleep(4)
clear_dtype = browser.find_element(By.XPATH, "//a[@id='documentTypeClear-DocumentType']").click()
time.sleep(3)
select = browser.find_element(By.XPATH, "//a[@id='documentTypeSelection-DocumentType']")
select.click()

# Deselecting document type

time.sleep(4)
mortgage = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-59']").click()
time.sleep(3)
m_1 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-194']").click()
time.sleep(3)
m_2 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-60']").click()
time.sleep(3)
m_3 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-61']").click()
time.sleep(3)
m_4 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-159']").click()
time.sleep(3)
m_5 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-160']").click()
time.sleep(3)

# Selecting deed
deed = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-19']").click()
time.sleep(3)
deed_1 = browser.find_element(By.XPATH, "//input[@id='dt-DocumentType-139']").click()

# clicking select
time.sleep(3)
sele = 0
select1 = browser.find_elements(By.XPATH, "//a[@class='btn btn-primary'][@data-dismiss='modal']")
for ele in select1:
    sele += 1
    if sele == 2:
        ele.click()
print('Successfully selected document types')

# submit
time.sleep(3)
submit = browser.find_element(By.XPATH, "//a[@id='submit-DocumentType']")
submit.click()

time.sleep(5)
browser.execute_script("window.scrollBy(0,220)", "")

# Counting the total pages & Counting the total mortgage documents & How much documents it's downloaded

time.sleep(5)
total_pages = 0
total_downloaded = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//table[@id='resultsTable']"))
    total_pages += element_count
    display_records = Select(browser.find_element(By.XPATH, "//select[@name='resultsTable_length']"))
    display_records.select_by_visible_text('100')
    time.sleep(4)
    links = browser.find_elements(By.XPATH, "//td[@class='tablecell nowordbreak'][3]")
    hrefs = []
    for c in links:
        hrefs.append(c.text)
    total_downloaded = total_downloaded + len(hrefs)

    for i in range(len(hrefs)):
        click_form = browser.find_element(By.XPATH, "//td[contains(text(),'" + hrefs[i] + "')]")
        click_form.click()
        time.sleep(4)
        click_view = browser.find_element(By.XPATH, "//a[@id='idViewGroup']")
        click_view.click()
        time.sleep(3)
        view_all_pages = browser.find_element(By.XPATH, "//li[@id='DocumentViewButtonAll']")
        view_all_pages.click()
        time.sleep(12)
        get_back = browser.find_element(By.XPATH, "//a[@id='returnToSearchButton']").click()
        time.sleep(5)

    print('Successfully downloaded', len(hrefs), 'documents in page', p)

    try:
        time.sleep(3)
        next_page = browser.find_element(By.XPATH,
                                         "//a[@class='paginate_button next' and not(@id='resultsTable_next')]")
        next_page.click()
    except Exception as e:
        break
    time.sleep(5)

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total_downloaded)

browser.quit()