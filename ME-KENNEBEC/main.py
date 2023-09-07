from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"
path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\ME-KENNEBEC'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

# Opening browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

# Getting page
url = "https://countyfusion3.kofiletech.us/countyweb/login.do?countyname=KennebecME"
browser.get(url)
browser.maximize_window()
sleep(7)

# log in

user_name = browser.find_element(By.XPATH, "//input[@name='username']").send_keys('ionaccess')
sleep(2)
password = browser.find_element(By.XPATH, "//input[@name='password']").send_keys('delete123')
sleep(2)
log_in = browser.find_element(By.XPATH, "//input[@value='Login']").click()
print('Successfully log in')

# Accept disclaimer
try:
    iframe = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@name = "bodyframe"]'))
    )
    browser.switch_to.frame(iframe)
    sleep(5)
except Exception as e:
    print("Error:", e)

accept_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//input[@id = "accept"]'))
)
accept_button.click()

# Go to Document Search page and fill in details
try:
    iframe1 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@name = "bodyframe"]')))
    browser.switch_to.frame(iframe1)
    sleep(5)
except Exception as e:
    print(e)

browser.find_element(By.XPATH, "//tr[@id='datagrid-row-r1-2-0']/td/div").click()
sleep(5)

main_page = browser.current_window_handle

try:
    iframe2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@id = "dynSearchFrame"]')))
    browser.switch_to.frame(iframe2)
    sleep(5)
except Exception as e:
    print(e)

# Uncheck 'All Documents Type'
browser.find_element(By.XPATH, '//span[@class ="tree-title"]/b[contains (text(), "All Document Types")]').click()
sleep(4)

# deed documents
browser.find_element(By.XPATH, '//div[@id = "instTree_easyui_tree_7"]/span[4]').click()
sleep(3)

# Mortgage documents

browser.find_element(By.XPATH, '//div[@id = "instTree_easyui_tree_16"]/span[4]').click()
sleep(3)

try:
    iframe3 = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@id = "criteriaframe"]')))
    browser.switch_to.frame(iframe3)
    sleep(5)
except Exception as e:
    print(e)

# From date
from_date = browser.find_element(By.XPATH, '//input[@id = "_easyui_textbox_input4"]')
from_date.clear()
sleep(2)
from_date.send_keys('08/22/2023')
sleep(3)

# To date
to_date = browser.find_element(By.XPATH, '//input[@id = "_easyui_textbox_input5"]')
to_date.clear()
sleep(2)
to_date.send_keys('08/22/2023')
sleep(3)

browser.switch_to.default_content()
sleep(7)

try:
    iframe4 = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@name = "bodyframe"]')))
    browser.switch_to.frame(iframe4)
    sleep(5)
except Exception as e:
    print(e)

try:
    iframe5 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@id = "dynSearchFrame"]')))
    browser.switch_to.frame(iframe5)
    sleep(5)
except Exception as e:
    print(e)

search_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//img[@id= "imgSearch"]')))
search_button.click()
sleep(15)

# Get handles of all open windows
window_handles = browser.window_handles

# Switch to the new window
new_window_handle = window_handles[-1]
browser.switch_to.window(new_window_handle)
sleep(5)

browser.switch_to.default_content()
sleep(5)

try:
    iframe6 = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@name = "bodyframe"]')))
    browser.switch_to.frame(iframe6)
    sleep(5)
except Exception as e:
    print(e)

try:
    iframe7 = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@id = "resultFrame"]')))
    browser.switch_to.frame(iframe7)
    sleep(5)
except Exception as e:
    print(e)

try:
    iframe8 = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@id = "resultListFrame"]')))
    browser.switch_to.frame(iframe8)
    sleep(5)
except Exception as e:
    print(e)

# total documents
docs_count = len(browser.find_elements(By.XPATH, '//div/span/a[@class = "linksm"]'))

# count of downloaded documents
d = 0

# Locate and click first document link
try:
    doc_link = browser.find_element(By.XPATH, '//div/span/a[@id = "inst0"]')
    doc_link.click()
    sleep(2)

except Exception as e:
    print(e)
    sleep(2)

# Download all documents
while d < docs_count:

    browser.switch_to.window(window_handles[-1])
    sleep(4)

    browser.switch_to.default_content()
    sleep(4)

    try:
        iframe8 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//iframe[@name = "bodyframe"]')))
        browser.switch_to.frame(iframe8)
        sleep(5)
    except Exception as e:
        print(e)

    try:
        iframe9 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//iframe[@id = "resnavframe"]')))
        browser.switch_to.frame(iframe9)
        sleep(5)

        # locate and click on "Save" button within iframe
        save_button = browser.find_element(By.XPATH, '//img[@id = "img0"]')
        sleep(3)
        save_button.click()
        sleep(5)

    except Exception as e:
        print(e)
        sleep(2)

    browser.switch_to.window(window_handles[-1])
    sleep(5)

    browser.switch_to.default_content()
    sleep(5)

    try:
        iframe10 = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//iframe[@id = "dialogframe"]')))
        browser.switch_to.frame(iframe10)
        sleep(6)

        download_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type = "button" and @value = "Download"]')))
        download_button.click()
        sleep(3)
        accept = browser.find_element(By.XPATH, "//input[@value='Accept']").click()
        sleep(10)

        d += 1
        print('Successfully downloaded', d, 'documents.')

    except Exception as e:
        print(e)

    browser.switch_to.window(window_handles[-1])
    sleep(5)

    browser.switch_to.default_content()
    sleep(5)

    if d < docs_count:
        try:
            iframe11 = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//iframe[@name = "bodyframe"]')))
            browser.switch_to.frame(iframe11)
            sleep(4)

            iframe12 = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//iframe[@id = "documentFrame"]')))
            browser.switch_to.frame(iframe12)
            sleep(4)

            next_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@id = "nextimg"]')))
            next_button.click()
            sleep(7)

        except Exception as e:
            print(e)

print("Total records: ", docs_count)
print("Total documents downloaded: ", d)

# Close the browser
browser.quit()
