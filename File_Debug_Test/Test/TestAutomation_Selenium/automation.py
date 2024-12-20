# selenium => browser automation tool
# selenium works with different kinds of browser drivers
# ------------------------------
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
#
# service = Service(executable_path='./chromedriver')
#
# options = Options()
# options.add_experimental_option('detach', True)  # this ensures chrome window does not close
#
# chrome_browser = webdriver.Chrome(service=service, options=options)
#
# print(chrome_browser)
# --------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# chrome_browser = webdriver.Chrome()
# chrome_browser.maximize_window()
# chrome_browser.get('write_here_a_specific_url')

# assert 'asdas..' in chrome_browser.title

# # This solves the issue with the Popup for those that encounter it:
# chrome_browser.implicitly_wait(2)
# popup = chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()

# user_message = chrome_browser.find_element(By.ID, 'user-message')
# user_message.clear()
# user_message.send_keys('I AM EXTRA COOOOL')

# time.sleep(2)
# assert 'Show Message' in chrome_browser.page_source
# show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# show_message_button.click()

# output_message = chrome_browser.find_element(By.ID, 'display')
# assert 'I AM EXTRA COOOOL' in output_message.text

# chrome_browser.close()