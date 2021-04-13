from selenium import webdriver

driver=webdriver.Chrome("D:\\Softwares\\chromedriver.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/#/practice-project")


#driver.find_element_by_id("agreeTerms").click()
driver.find_element_by_css_selector('input[name="email"]').send_keys("umer")

