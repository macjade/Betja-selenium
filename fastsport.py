# enter text to generate fastest sport

import time

from selenium import webdriver


driver = webdriver.Chrome("C:\\Users\\PrayingReconciliatio\\Desktop\\selenium\\chromedriver.exe")

driver.get('https://web.bet9ja.com/Sport/Default.aspx')

# valid username
driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_Username"]').send_keys('macjade')

#valid password
driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_Password"]').send_keys('JA08162500447')

driver.save_screenshot('FS1.png')

driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_lnkBtnLogin"]').click()

time.sleep(3)
driver.save_screenshot('FS2.png')

FSC = driver.find_element_by_id('FBCodPub')
FSC.find_element_by_tag_name('input').send_keys('729')

FSD = driver.find_element_by_class_name('FSSE')
FSD.find_element_by_tag_name('input').send_keys('1 & Under')

driver.save_screenshot('FS3.png')

driver.find_element_by_class_name('FSConfirm').click()