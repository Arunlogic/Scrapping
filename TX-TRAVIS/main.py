from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options

path = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"
path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\TX-TRAVIS'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,  # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

# Opening browser
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

# Getting page
url = "https://www.tccsearch.org/RealEstate/SearchEntry.aspx?e=newSession"
# http://www.tccsearch.org/
browser.get(url)
browser.maximize_window()
sleep(2)

# Accept Disclaimer
sleep(2)
accept = browser.find_element(By.XPATH, '//a[@id = "cph1_lnkAccept"]').click()

sleep(2)
real_estate = browser.find_element(By.XPATH, '//span[contains (text(), "Real Estate") and @tabindex = "-1" ]').click()
sleep(1)
search_docs = browser.find_element(By.XPATH, '//span[contains (text(), "Search Real Estate Index")]').click()

input_start_date = browser.find_element(By.XPATH, "//table[@id='cphNoMargin_f_ddcDateFiledFrom']//input")
input_start_date.click()
sleep(2)
input_start_date.send_keys('08/09/2017')
input_end_date = browser.find_element(By.XPATH, "//table[@id='cphNoMargin_f_ddcDateFiledTo']//input")
input_end_date.click()
sleep(2)
input_end_date.send_keys('08/09/2017')

# selecting document type
sleep(2)
browser.find_element(By.XPATH,
                     "//label[contains(text(),'DEED OF TRUST') and @for='cphNoMargin_f_dclDocType_42']").click()
sleep(3)
browser.find_element(By.XPATH,
                     "//label[contains(text(),'HOME EQUITY LOAN') and @for='cphNoMargin_f_dclDocType_54']").click()
sleep(3)
browser.find_element(By.XPATH, "//label[contains(text(),'TRUST') and @for='cphNoMargin_f_dclDocType_115']").click()
sleep(5)

# Click on search button
browser.find_element(By.XPATH, '//span[@id="cphNoMargin_SearchButtons2_btnSearch__3"]').click()
sleep(10)

# Display full count of records
browser.find_element(By.XPATH, '//a[text()="count again"]').click()
sleep(4)

# count of total records
total_records = int(browser.find_element(By.XPATH, '//span[contains (@id, "TotalRows")]').text)

total_documents = 0
total_pages = 0

# Looping through the documents and downloading

while True:
    try:
        print('Scrapping page:', total_pages + 1)

        # Locate and click document links on the current page
        image_links = browser.find_elements(By.XPATH, '//div[contains(text(), " View")]')
        d = 0

        for link in image_links:
            try:
                browser.execute_script("arguments[0].scrollIntoView();", link)
                link.click()
                sleep(5)

                main_page = browser.current_window_handle
                sleep(4)
                for handle in browser.window_handles:
                    if handle != main_page:
                        image_page = handle

                # change the control to image page
                browser.switch_to.window(image_page)
                sleep(4)

                try:
                    iframe = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//iframe[@id="ImageViewer1_ifrLTViewer"]'))
                    )
                    browser.switch_to.frame(iframe)

                    # locate and click on "Get Image Now" button within iframe
                    get_image = browser.find_element(By.XPATH, '//span[@id = "btnProcessNow__3"]')
                    sleep(4)
                    get_image.click()
                    sleep(5)

                except Exception as e:
                    print("Error:", e)
                sleep(2)

                try:
                    iframe2 = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//iframe[@id = "ifrImageWindow"]'))
                    )
                    browser.switch_to.frame(iframe2)
                    sleep(6)

                    save_element = WebDriverWait(browser, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="pdf"]/p/a'))
                    )
                    save_element.click()
                    sleep(4)

                    download = browser.find_element(By.ID, "open-button").click()
                    sleep(8)
                except Exception as e:
                    print("Error:", e)

                browser.switch_to.window(main_page)
                sleep(5)
                total_documents += 1
                d += 1

            except Exception as e:
                print(e)

        total_pages += 1

        # Click the "Next" arrow to navigate to the next page
        try:
            next_arrow = browser.find_element(By.XPATH, '//input[@id = "OptionsBar2_imgNext"]')
            is_disabled = next_arrow.get_attribute("disabled") is not None

            if is_disabled:
                break
            else:
                next_arrow.click()
                sleep(7)

        except NoSuchElementException:
            break  # Exit the loop if there are no more pages

    except Exception as ex:
        print("Error:", ex)
print("Total records: ", total_records)
print("Total documents downloaded: ", total_documents)
print("Total pages: ", total_pages)

# new search
new_search = browser.find_element(By.XPATH, "//a[contains(text(),'New Search')][1]").click()
sleep(3)

input_start_date = browser.find_element(By.XPATH, "//table[@id='cphNoMargin_f_ddcDateFiledFrom']//input")
input_start_date.click()
sleep(2)
input_start_date.send_keys('08/09/2017')
input_end_date = browser.find_element(By.XPATH, "//table[@id='cphNoMargin_f_ddcDateFiledTo']//input")
input_end_date.click()
sleep(2)
input_end_date.send_keys('08/09/2017')

# selecting document type
sleep(2)
browser.find_element(By.XPATH, "//label[contains(text(),'DEED') and @for='cphNoMargin_f_dclDocType_41']").click()
sleep(3)
browser.find_element(By.XPATH,
                     "//label[contains(text(),'WARRANTY DEED') and @for='cphNoMargin_f_dclDocType_125']").click()
sleep(5)

# Click on search button
browser.find_element(By.XPATH, '//span[@id="cphNoMargin_SearchButtons2_btnSearch__3"]').click()
sleep(10)

# Display full count of records
browser.find_element(By.XPATH, '//a[text()="count again"]').click()
sleep(4)

# count of total records
total_records = int(browser.find_element(By.XPATH, '//span[contains (@id, "TotalRows")]').text)

total_documents = 0
total_pages = 0

# Looping through the documents and downloading

while True:
    try:
        print('Scrapping page:', total_pages + 1)

        # Locate and click document links on the current page
        image_links = browser.find_elements(By.XPATH, '//div[contains(text(), " View")]')
        d = 0

        for link in image_links:
            try:
                browser.execute_script("arguments[0].scrollIntoView();", link)
                link.click()
                sleep(5)

                main_page = browser.current_window_handle
                sleep(4)
                for handle in browser.window_handles:
                    if handle != main_page:
                        image_page = handle

                # change the control to image page
                browser.switch_to.window(image_page)
                sleep(4)

                try:
                    iframe = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//iframe[@id="ImageViewer1_ifrLTViewer"]'))
                    )
                    browser.switch_to.frame(iframe)

                    # locate and click on "Get Image Now" button within iframe
                    get_image = browser.find_element(By.XPATH, '//span[@id = "btnProcessNow__3"]')
                    sleep(4)
                    get_image.click()
                    sleep(5)

                except Exception as e:
                    print("Error:", e)
                sleep(2)

                try:
                    iframe2 = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//iframe[@id = "ifrImageWindow"]'))
                    )
                    browser.switch_to.frame(iframe2)
                    sleep(6)

                    save_element = WebDriverWait(browser, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="pdf"]/p/a'))
                    )
                    save_element.click()
                    sleep(4)

                    download = browser.find_element(By.ID, "open-button").click()
                    sleep(8)
                except Exception as e:
                    print("Error:", e)

                browser.switch_to.window(main_page)
                sleep(5)
                total_documents += 1
                d += 1

            except Exception as e:
                print(e)

        total_pages += 1

        # Click the "Next" arrow to navigate to the next page
        try:
            next_arrow = browser.find_element(By.XPATH, '//input[@id = "OptionsBar2_imgNext"]')
            is_disabled = next_arrow.get_attribute("disabled") is not None

            if is_disabled:
                break
            else:
                next_arrow.click()
                sleep(7)

        except NoSuchElementException:
            break  # Exit the loop if there are no more pages

    except Exception as ex:
        print("Error:", ex)
print("Total records: ", total_records)
print("Total documents downloaded: ", total_documents)
print("Total pages: ", total_pages)

# Close the browser
browser.quit()

