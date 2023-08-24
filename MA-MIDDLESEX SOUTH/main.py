from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

path = 'C://IonIdea//Chrome Web Driver_114//chromedriver'

path_to_save_pdf = 'C:\\IonIdea\\County_Downloaded_Documents\\MA-MIDDLESEX SOUTH'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True,            # Give True to download & Give False to view
    'download.default_directory': path_to_save_pdf
})

browser = webdriver.Chrome(executable_path=path,options=chrome_options)

url = "http://www.masslandrecords.com/MiddlesexSouth/"
browser.get(url)
browser.maximize_window()

# search criteria
time.sleep(4)
search_criteria = browser.find_element(By.XPATH,"//a[contains(text(),'Search Criteria')]").click()
time.sleep(3)
records = browser.find_element(By.XPATH,"//a[@id='Navigator1_SearchCriteria1_LinkButton04']").click()

# Recording date
time.sleep(6)
input_start_date = browser.find_element(By.XPATH,"//input[@id='SearchFormEx1_ACSTextBox_DateFrom']")
input_start_date.clear()
start_date = '06/05/2023'
time.sleep(3)
input_start_date.send_keys(start_date)

time.sleep(3)
input_end_date = browser.find_element(By.XPATH,"//input[@id='SearchFormEx1_ACSTextBox_DateTo']")
input_end_date.clear()
end_date = '06/05/2023'
time.sleep(3)
input_end_date.send_keys(end_date)
time.sleep(5)

# select document type
document = Select(browser.find_element(By.XPATH,"//select[@id='SearchFormEx1_ACSDropDownList_DocumentType']"))
document.select_by_visible_text('MORTGAGE')

# search
time.sleep(4)
search = browser.find_element(By.XPATH,"//input[@id='SearchFormEx1_btnSearch']")
search.click()
time.sleep(3)

# To ADD TO CART

# alert = browser.find_element(By.ID,'MessageBoxCtrl1_buttonmbatCLIENTOK')
try:
    alert = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'MessageBoxCtrl1_buttonmbatCLIENTOK')))
    print("There is no records")
    time.sleep(4)
    alert.click()

except Exception as e:
    total_pages = 0
    total = 0
    p = 0
    while True:
        time.sleep(5)
        p = p + 1
        print('Scrapping page:', p)
        element_count = len(browser.find_elements(By.XPATH, "//table[@style='table-layout: fixed; width: 100%;']"))
        total_pages += element_count

        odd_records = browser.find_elements(By.XPATH, "//tr[@class='DataGridRow']/td[3]/a")
        odd = []
        for o in odd_records:
            odd.append(o.text)
        print('Odd records:', odd)
        o = len(odd)
        total = total + len(odd)
        for i in range(len(odd)):
            doc_no = browser.find_element(By.XPATH, "//a[contains(text(),'" + odd[i] + "')]")
            doc_no.click()
            time.sleep(4)
            add_basket = browser.find_element(By.XPATH, "//a[@id='DocDetails1_ButAddToBasket']")
            add_basket.click()
            time.sleep(4)
            next_b = browser.find_element(By.XPATH, "//input[@id='OrderCriteriaCtrl1_ImageButton_Next']")
            next_b.click()
            time.sleep(6)
        basket = browser.find_element(By.XPATH, "//a[@id='Navigator1_Basket']")
        basket.click()
        time.sleep(5)
        selecting = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_SelectAll']")
        selecting.click()
        time.sleep(5)
        download = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_LinkButtonDownload']")
        download.click()
        time.sleep(2 * 60)
        main_window = browser.current_window_handle
        all_windows = browser.window_handles
        for window in all_windows:
            if window != main_window:
                browser.switch_to.window(window)
                browser.close()
        browser.switch_to.window(main_window)
        time.sleep(5)
        clearing = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_ClearButton']").click()
        time.sleep(3)
        removing = browser.find_element(By.XPATH, "//input[@id='BasketCtrl1_ImageButton1']").click()
        time.sleep(4)

        even_records = browser.find_elements(By.XPATH, "//tr[@class='DataGridAlternatingRow']/td[3]/a")
        try:
            if not even_records:
                print('There are no even records')
                e = 0
                break
            else:
                even = []
                for e in even_records:
                    even.append(e.text)
                print('Even records:', even)
                e = len(even)
                total = total + len(even)
                for i in range(len(even)):
                    doc_no = browser.find_element(By.XPATH, "//a[contains(text(),'" + even[i] + "')]")
                    doc_no.click()
                    time.sleep(4)
                    add_basket = browser.find_element(By.XPATH, "//a[@id='DocDetails1_ButAddToBasket']")
                    add_basket.click()
                    time.sleep(4)
                    next_b = browser.find_element(By.XPATH, "//input[@id='OrderCriteriaCtrl1_ImageButton_Next']")
                    next_b.click()
                    time.sleep(6)

                basket = browser.find_element(By.XPATH, "//a[@id='Navigator1_Basket']")
                basket.click()
                time.sleep(5)
                selecting = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_SelectAll']")
                selecting.click()
                time.sleep(5)
                download = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_LinkButtonDownload']")
                download.click()
                time.sleep(2 * 60)
                main_window = browser.current_window_handle
                all_windows = browser.window_handles
                for window in all_windows:
                    if window != main_window:
                        browser.switch_to.window(window)
                        browser.close()
                browser.switch_to.window(main_window)
                time.sleep(5)
                clearing = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_ClearButton']").click()
                time.sleep(3)
                removing = browser.find_element(By.XPATH, "//input[@id='BasketCtrl1_ImageButton1']").click()
                time.sleep(4)
        except Exception as e:
            print(e)

        print('Successfully downloaded', o + e, 'documents in page', p)
        try:
            next_button = browser.find_element(By.XPATH, "//a[@id='DocList1_LinkButtonNext']")
            time.sleep(4)
            next_button.click()
        except Exception as e:
            time.sleep(4)
            break

    print('Total Pages: ', total_pages)
    print('Total documents:', total)

# DEED

time.sleep(5)
# select document type
document = Select(browser.find_element(By.XPATH,"//select[@id='SearchFormEx1_ACSDropDownList_DocumentType']"))
document.select_by_visible_text('DEED')

# search
time.sleep(5)
search = browser.find_element(By.XPATH,"//input[@id='SearchFormEx1_btnSearch']")
search.click()
time.sleep(3)
# To ADD TO CART

# alert = browser.find_element(By.ID,'MessageBoxCtrl1_buttonmbatCLIENTOK')
try:
    alert = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'MessageBoxCtrl1_buttonmbatCLIENTOK')))
    print("There is no records")
    time.sleep(4)
    alert.click()

except Exception as e:
    total_pages = 0
    total = 0
    p = 0
    while True:
        time.sleep(5)
        p = p + 1
        print('Scrapping page:', p)
        element_count = len(browser.find_elements(By.XPATH, "//table[@style='table-layout: fixed; width: 100%;']"))
        total_pages += element_count

        odd_records = browser.find_elements(By.XPATH, "//tr[@class='DataGridRow']/td[3]/a")
        odd = []
        for o in odd_records:
            odd.append(o.text)
        print('Odd records:', odd)
        o = len(odd)
        total = total + len(odd)
        for i in range(len(odd)):
            doc_no = browser.find_element(By.XPATH, "//a[contains(text(),'" + odd[i] + "')]")
            doc_no.click()
            time.sleep(4)
            add_basket = browser.find_element(By.XPATH, "//a[@id='DocDetails1_ButAddToBasket']")
            add_basket.click()
            time.sleep(4)
            next_b = browser.find_element(By.XPATH, "//input[@id='OrderCriteriaCtrl1_ImageButton_Next']")
            next_b.click()
            time.sleep(6)
        basket = browser.find_element(By.XPATH, "//a[@id='Navigator1_Basket']")
        basket.click()
        time.sleep(5)
        selecting = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_SelectAll']")
        selecting.click()
        time.sleep(5)
        download = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_LinkButtonDownload']")
        download.click()
        time.sleep(2 * 60)
        main_window = browser.current_window_handle
        all_windows = browser.window_handles
        for window in all_windows:
            if window != main_window:
                browser.switch_to.window(window)
                browser.close()
        browser.switch_to.window(main_window)
        time.sleep(5)
        clearing = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_ClearButton']").click()
        time.sleep(3)
        removing = browser.find_element(By.XPATH, "//input[@id='BasketCtrl1_ImageButton1']").click()
        time.sleep(4)

        even_records = browser.find_elements(By.XPATH, "//tr[@class='DataGridAlternatingRow']/td[3]/a")
        try:
            if not even_records:
                print('There are no even records')
                e = 0
                break
            else:
                even = []
                for e in even_records:
                    even.append(e.text)
                print('Even records:', even)
                e = len(even)
                total = total + len(even)
                for i in range(len(even)):
                    doc_no = browser.find_element(By.XPATH, "//a[contains(text(),'" + even[i] + "')]")
                    doc_no.click()
                    time.sleep(4)
                    add_basket = browser.find_element(By.XPATH, "//a[@id='DocDetails1_ButAddToBasket']")
                    add_basket.click()
                    time.sleep(4)
                    next_b = browser.find_element(By.XPATH, "//input[@id='OrderCriteriaCtrl1_ImageButton_Next']")
                    next_b.click()
                    time.sleep(6)

                basket = browser.find_element(By.XPATH, "//a[@id='Navigator1_Basket']")
                basket.click()
                time.sleep(5)
                selecting = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_SelectAll']")
                selecting.click()
                time.sleep(5)
                download = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_LinkButtonDownload']")
                download.click()
                time.sleep(2 * 60)
                main_window = browser.current_window_handle
                all_windows = browser.window_handles
                for window in all_windows:
                    if window != main_window:
                        browser.switch_to.window(window)
                        browser.close()
                browser.switch_to.window(main_window)
                time.sleep(5)
                clearing = browser.find_element(By.XPATH, "//a[@id='BasketCtrl1_ClearButton']").click()
                time.sleep(3)
                removing = browser.find_element(By.XPATH, "//input[@id='BasketCtrl1_ImageButton1']").click()
                time.sleep(4)
        except Exception as e:
            print(e)

        print('Successfully downloaded', o + e, 'documents in page', p)
        try:
            next_button = browser.find_element(By.XPATH, "//a[@id='DocList1_LinkButtonNext']")
            time.sleep(4)
            next_button.click()
        except Exception as e:
            time.sleep(4)
            break

    print('Total Pages: ', total_pages)
    print('Total documents:', total)
browser.quit()

