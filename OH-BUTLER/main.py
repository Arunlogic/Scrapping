from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"
path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\OH-BUTLER'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

# Opening browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

# Getting page
url = "https://countyfusion13.kofiletech.us/countyweb/loginDisplay.action?countyname=ButlerOH"
browser.get(url)
browser.maximize_window()
sleep(7)

# Click on Login as Guest
browser.find_element(By.XPATH, '//input[@value = "Login as Guest"]').click()

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
browser.find_element(By.XPATH, '//div[@id = "instTree_easyui_tree_2"]/span[2]').click()
sleep(2)
# deed
browser.find_element(By.XPATH, '//div[@id = "instTree_easyui_tree_70"]').click()
sleep(3)
browser.find_element(By.XPATH, '//div[@id = "instTree_easyui_tree_2"]/span[2]').click()
sleep(5)

# Mortgage documents
browser.find_element(By.XPATH, '//div[@id = "instTree_easyui_tree_7"]/span[@class = "tree-hit tree-collapsed"]').click()
sleep(2)
# Mortgage
browser.find_element(By.XPATH, '//div[@id = "instTree_easyui_tree_25"]').click()
sleep(3)
browser.find_element(By.XPATH, '//div[@id = "instTree_easyui_tree_7"]/span[@class ="tree-hit tree-expanded"]').click()
sleep(4)

try:
    iframe3 = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@id = "criteriaframe"]')))
    browser.switch_to.frame(iframe3)
    sleep(5)
except Exception as e:
    print(e)

# From date
from_date = browser.find_element(By.XPATH, '//input[@id = "_easyui_textbox_input6"]')
from_date.clear()
sleep(2)
from_date.send_keys('08/22/2023')
sleep(3)

# To date
to_date = browser.find_element(By.XPATH, '//input[@id = "_easyui_textbox_input7"]')
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
docs_count = len(browser.find_elements(By.XPATH, '//div/span/a[@class = "link"]'))

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
        save_button = browser.find_element(By.XPATH, '//img[@title="Save Image"]')
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
        sleep(7)

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
