from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
import pyautogui as pyao

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\UT-UTAH'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.prompt_for_download': False,
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf,
    "download.directory_upgrade": True,
})

browser = webdriver.Chrome(executable_path=path,options=chrome_options)

url = "http://www.utahcounty.gov/LandRecords/Index.asp"
browser.get(url)
browser.maximize_window()

# document record search
time.sleep(5)
document_record_search = browser.find_element(By.XPATH,"//a[contains(text(),'Document Recording Search')] ")
document_record_search.click()

# Recording date
time.sleep(6)
input_start_date = browser.find_element(By.XPATH,"//input[@id='avEntryDate']")
input_start_date.clear()
start_date = '07/11/2023'
time.sleep(3)
input_start_date.send_keys(start_date)

time.sleep(3)
input_end_date = browser.find_element(By.XPATH,"//input[@id='avEndEntryDate']")
input_end_date.clear()
end_date = '07/11/2023'
time.sleep(3)
input_end_date.send_keys(end_date)
time.sleep(2)

# search
time.sleep(5)
search = browser.find_element(By.XPATH,"//input[@name='Submit3'][@value='  Search  ']")
search.click()
time.sleep(4)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(5)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//table[@width='100%']"))
    total_pages += element_count

    ids = browser.find_elements(By.XPATH, "//tr[@valign='top']/td/a")
    document_number = []
    for d in ids:
        document_number.append(d.text)
    print(len(document_number))
    print('Document Numbers:', document_number)

    total = total + len(document_number)

    for i in range(len(document_number)):
        parent_handle = browser.current_window_handle
        doc_no = browser.find_element(By.XPATH, "//a[contains(text(),'" + document_number[i] + "')]")
        doc_no.click()
        time.sleep(3)
        try:
            browser.find_element(By.XPATH,"//h1[contains(text(),'Document Detail')]/following-sibling::table/tbody/tr[3]/td[2][not(contains(text(),'WD - WARRANTY DEED') or contains(text(),'D TR - DEED OF TRUST'))]")
            time.sleep(3)
            browser.back()
            time.sleep(4)
        except Exception as e:
            time.sleep(2)
            image_viewer = browser.find_element(By.XPATH, "//input[@value='Document Image Viewer']")
            image_viewer.click()
            time.sleep(3)
            all_handles = browser.window_handles
            for handle in all_handles:
                if handle != parent_handle:
                    browser.switch_to.window(handle)
                    time.sleep(3)
                    browser.find_element(By.XPATH, "//img[@alt='Print']").click()
                    time.sleep(12)
                    pyao.press('esc')
                    time.sleep(4)
                    browser.close()
                    all_handles_1 = browser.window_handles
                    for handle_1 in all_handles_1:
                        if handle_1 != parent_handle and handle_1 != handle:
                            browser.switch_to.window(handle_1)
                            print('successfully switched')
                            time.sleep(8)
                            iframe = browser.find_element(By.XPATH, "//iframe[@id='iFramePdf']")
                            browser.switch_to.frame(iframe)
                            download = browser.find_element(By.XPATH, "//button[@id='open-button']").click()
                            time.sleep(14)
                            browser.close()
            browser.switch_to.window(parent_handle)
            for i in range(2):
                time.sleep(3)
                browser.back()
            time.sleep(4)
    
    print('Successfully downloaded', len(document_number), 'documents in page', p)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        time.sleep(5)
        next_button = browser.find_element(By.XPATH, "//a[contains(text(),'Next')]")
        next_button.click()
    except Exception as e:
        break

    time.sleep(5)
print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()