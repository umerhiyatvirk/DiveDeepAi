from selenium import webdriver

driver= webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")

#driver.maximize_window()
driver.get("https://login.salesforce.com/?locale=eu")

driver.find_element_by_css_selector(".username").send_keys("umer")
driver.find_element_by_css_selector("#password").send_keys("virk")
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_css_selector("[class*='loginError']").text)



