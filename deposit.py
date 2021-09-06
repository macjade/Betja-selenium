# valid amount(>= 100) and confirm

import time

from selenium import webdriver

driver = webdriver.Chrome(DRIVER_URL / "chromedriver.exe")

driver.get('https://web.bet9ja.com/Sport/Default.aspx')
window_before = driver.window_handles[0]

# valid username
driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_Username"]').send_keys('{username}')

#valid password
driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_Password"]').send_keys('{password}')

driver.save_screenshot('D1.png')

driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_lnkBtnLogin"]').click()

time.sleep(3)
driver.save_screenshot('D2.png')

# to deposit
# switching to new window
driver.find_element_by_class_name('btnDeposit').click()
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
driver.save_screenshot('D3.png')

driver.find_element_by_class_name('webpay').click()
driver.save_screenshot('D4.png')

driver.find_element_by_name('webPay-deposit-amount').send_keys('100')
driver.find_element_by_xpath('//*[@data-amount="100"]').click()
driver.save_screenshot('D5.png')

driver.find_element_by_id('webPay-submit-form').click()
time.sleep(3)
driver.find_element_by_id('webPay-submit').click()
driver.save_screenshot('D6.png')