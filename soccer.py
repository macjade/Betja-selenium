# valid stake amount for soccer

import time

from selenium import webdriver


driver = webdriver.Chrome("C:\\Users\\PrayingReconciliatio\\Desktop\\selenium\\chromedriver.exe")

driver.get('https://web.bet9ja.com/Sport/Default.aspx')

# valid username
driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_Username"]').send_keys('macjade')

#valid password
driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_Password"]').send_keys('JA08162500447')

driver.save_screenshot('S1.png')

driver.find_element_by_xpath('//*[@id="h_w_cLogin_ctrlLogin_lnkBtnLogin"]').click()

time.sleep(3)
driver.save_screenshot('S2.png')

# To select soccer
driver.find_element_by_xpath("//*[@title='Soccer ']").click()
driver.find_element_by_id('c415112').click()  # To Select UEFA National League
driver.save_screenshot('S3.png')
driver.find_element_by_xpath('//*[@id="G11463"]/div[1]/div/a').click()  # To click on view

# To select market for iceland vs switzerland
text = 'France - Germany'
element = driver.find_element_by_xpath('//*[@ng-click="openSubEventDetail(subEvent.SubEventID)" and text()="' + text + '"]')
driver.execute_script('arguments[0].scrollIntoView();', element)
driver.save_screenshot("S4.png")
element.click()
# To select over 1.5 goals
value_from_page = driver.find_elements_by_css_selector('.SEItem.ng-scope > div.SECQ.ng-binding')
odds = (e.text for e in value_from_page if e.is_displayed())
print(odds)

game = 'O/U 1.5'

if list(set(game) & set(odds)) == ['O/U 1.5']:
    print(list(set(game) & set(odds)))
    found_game = list(set(game) & set(odds))
    element = driver.find_elements_by_xpath('//div[@class="ng-binding"]/text()="' + str(found_game) + '"')
    driver.execute_script('arguments[0].scrollIntoView();', element)
    #value_from_page = driver.find_elements_by_css_selector('.SEOdd.g1 > div.SEOddLnk.ng-binding')
    #odds = (e.text for e in value_from_page if e.is_displayed())
    #print(odds)

    #goals = "1.33"

    #if list(set(goals) & set(odds)) == ['1.33']:
     #   found_goal = list(set(goals) & set(odds))
      #  driver.find_elements_by_xpath('//div[@class="SEOddLnk" and text()="' + str(found_goal) + '"]').click()