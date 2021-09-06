# verify a valid betslip code

import time

from selenium import webdriver



driver = webdriver.Chrome(DRIVER_URL / "chromedriver.exe")

driver.get('https://web.bet9ja.com/Sport/Default.aspx')

# valid username
driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_Username"]').send_keys('{username}')

#valid password
driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_Password"]').send_keys('{password}')

driver.save_screenshot('BT1.png')

driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_lnkBtnLogin"]').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@class="odds"]/div/div[2]').click()
driver.save_screenshot('BT2.png')
time.sleep(4)

# to stake
a = driver.find_element_by_id('spanImporto')
a.find_element_by_tag_name('input').send_keys('100')
driver.save_screenshot('BT3.png')
time.sleep(2)
driver.find_element_by_class_name('dx').click()
time.sleep(3)
driver.save_screenshot('BT4.png')

# to switch to popup window and get the bet code
frame = driver.find_element_by_id('iframePrenotatoreSco')
driver.switch_to.frame(frame)
code = driver.find_element_by_xpath('//span[@class="number"]/span[1]').text
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@class="divTitle"]/a').click()# to close popup

# to input valid bet slip
driver.find_element_by_name('h$w$PC$cCoupon$txtPrenotatore').send_keys(code)
driver.save_screenshot('BT5.png')
driver.find_element_by_class_name('Load').click()
time.sleep(4)
driver.save_screenshot('BT6.png')