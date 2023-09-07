from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\FL-SAINT LUCIE'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path, options=chrome_options)

url = "https://acclaimweb.stlucieclerk.com/"
browser.get(url)
browser.maximize_window()

# instrument
time.sleep(4)
instrument = browser.find_element(By.XPATH, "//div[@class='row text-center']/div[3]/a/img").click()

time.sleep(4)
instrument_no = browser.find_element(By.XPATH, "//input[@id='InstrumentNumber']").send_keys('4340986')

time.sleep(2)
search = browser.find_element(By.XPATH, "//input[@id='SearchBtn']").click()
time.sleep(6)

# Counting the total pages & Counting the total documents & How much documents it's downloaded

total_pages = 0
total = 0
p = 0
while True:
    time.sleep(4)
    p = p + 1
    print('Scrapping page:', p)
    element_count = len(browser.find_elements(By.XPATH, "//div[@id='SearchResultGrid']"))
    total_pages += element_count
    time.sleep(2)
    link = browser.find_elements(By.XPATH, "//tbody[@role='rowgroup']/tr/td[8]")
    images = browser.find_elements(By.XPATH,
                                   "//tbody[@role='rowgroup']/tr/td[8][contains(text(),'DEED') or contains(text(),'MTG')]")
    a = []
    index = []
    for e in images:
        a.append(e.text)
    time.sleep(2)
    for c in link:
        for w in a:
            if c.text == w:
                x = link.index(c) + 1
                index.append(x)
                break

    total = total + len(index)

    for ind in index:
        parent_handle = browser.current_window_handle
        browser.find_element(By.XPATH, f"//tbody[@role='rowgroup']/tr{[ind]}/td[8]").click()
        time.sleep(6)
        all_handles = browser.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                browser.switch_to.window(handle)
                time.sleep(2)
                save = browser.find_element(By.XPATH, "//button[@id='undefined_wdv1_toolbar_Button_Save']").click()
                time.sleep(6)
                browser.close()
                all_handles_1 = browser.window_handles
                for handle_1 in all_handles_1:
                    if handle_1 != parent_handle and handle_1 != handle:
                        browser.switch_to.window(handle_1)
                        time.sleep(2)
                        browser.close()
        browser.switch_to.window(parent_handle)
        time.sleep(3)

    print('Successfully downloaded', len(index), 'documents in page', p)
    search = browser.find_element(By.XPATH, "//input[@id='SearchBtn']")
    browser.execute_script("arguments[0].scrollIntoView(true);", search)
    time.sleep(2)
    try:
        next_button = browser.find_element(By.XPATH, "//a[@title='Go to the next page']").click()
        time.sleep(3)

    except Exception as e:
        break

print('Total Pages: ', total_pages)
print('Total downloaded documents:', total)

browser.quit()

