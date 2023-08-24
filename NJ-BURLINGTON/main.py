from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait, Select

path  = "C://IonIdea//Chrome Web Driver_116//chromedriver-win64//chromedriver"
path_to_save_pdf =  'C:\\IonIdea\\County_Downloaded_Documents\\NJ-BURLINGTON'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})
# Opening browser
browser = webdriver.Chrome(executable_path=path,options=chrome_options)

url = "http://press.co.burlington.nj.us/Press/clerk/ClerkHome.aspx?op=basic"
browser.get(url)
browser.maximize_window()

# Go to Document Search page and fill in details
sleep(3)
browser.find_element(By.XPATH, '//a[@title = "By Document Type"]').click()
sleep(2)

# Document type
doc_types = ['MORTGAGE', 'DEED']

for doc in doc_types:

    doc_type = browser.find_element(By.XPATH, '//select[@name = "ctl00$ContentPlaceHolder1$ddlDocTypeTab2"]')
    ActionChains(browser).move_to_element(doc_type).click().send_keys(doc).perform()
    sleep(3)

    sleep(2)
    input_start_date = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtFromTab2']")
    input_start_date.clear()
    start_date = '08/02/2023'
    sleep(2)
    input_start_date.send_keys(start_date)

    input_end_date = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtToTab2']")
    input_end_date.clear()
    end_date = '08/02/2023'
    sleep(2)
    input_end_date.send_keys(end_date)
    sleep(2)
    # show records
    show = Select(browser.find_element(By.XPATH,"//select[@id='ctl00_ContentPlaceHolder1_ddlShowRecTab2']"))
    show.select_by_visible_text('100')

    # total records
    sleep(2)
    total = Select(browser.find_element(By.XPATH,"//select[@id='ctl00_ContentPlaceHolder1_ddlTotalRecTab2']"))
    total.select_by_visible_text('2000')
    sleep(2)

    # Search records
    sleep(2)
    search = browser.find_element(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_btnSearchTab2']")
    search.click()
    sleep(20)

    total_documents = 0

    try:
        image_link = browser.find_element(By.XPATH, '//input[@type = "image"]')
        image_link.click()
        sleep(3)
        image_page = browser.current_window_handle

        iframe = browser.find_element(By.XPATH, '//iframe[@id = "ctl00_ContentPlaceHolder1_ifrmElection"]')
        browser.switch_to.frame(iframe)
        sleep(2)

        frame1 = browser.find_element(By.XPATH, '//frame[@name = "InstViewerHeadFrame"]')
        browser.switch_to.frame(frame1)

        while True:
            display_image = browser.find_element(By.XPATH, '//input[@id = "btnImage"]')
            display_image.click()
            sleep(4)

            browser.switch_to.window(image_page)
            sleep(3)

            iframe = browser.find_element(By.XPATH,
                                          '//iframe[@id = "ctl00_ContentPlaceHolder1_ifrmElection"]')  # Re-locate the element
            browser.switch_to.frame(iframe)
            sleep(3)

            frame2 = browser.find_element(By.XPATH, '//frame[@name = "InstViewerBodyFrame"]')
            browser.switch_to.frame(frame2)
            sleep(3)

            get_image = browser.find_element(By.XPATH, '//img[@title = "View as PDF"]')
            sleep(2)
            get_image.click()
            sleep(30)

            total_documents += 1
            #print('Successfully downloaded', total_documents, 'documents.')

            browser.switch_to.window(image_page)
            sleep(3)

            iframe = browser.find_element(By.XPATH,
                                          '//iframe[@id = "ctl00_ContentPlaceHolder1_ifrmElection"]')  # Re-locate the element
            browser.switch_to.frame(iframe)
            sleep(2)

            frame1 = browser.find_element(By.XPATH, '//frame[@name = "InstViewerHeadFrame"]')
            browser.switch_to.frame(frame1)

            try:
                next_button = browser.find_element(By.XPATH, '//input[@id = "btnNext"]')

                is_disabled = next_button.get_attribute("disabled") is not None

                if is_disabled:
                    print("Next button is disabled. No more",doc,"documents.")
                    break
                else:
                    next_button.click()
                    sleep(5)

            except NoSuchElementException:
                print("No more pages to navigate.")
                break

    except Exception as e:
        print(e)

    print("Total",doc,"documents downloaded: ", total_documents)

    browser.switch_to.default_content()
    search = browser.find_element(By.XPATH, '//a[@id = "ctl00_ContentPlaceHolder1_hypBasic"]')
    search.click()
    sleep(8)

browser.quit()
