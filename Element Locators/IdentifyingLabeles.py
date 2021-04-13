from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=ca")

driver.find_element_by_css_selector("#username").send_keys("umer")
driver.find_element_by_css_selector(".password").send_keys("divedeep")
driver.find_element_by_css_selector("#Login").click()



print(driver.find_element_by_xpath('//*[@id="usernamegroup"]/label').text)
print(driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div[3]/form/label') .text)