from selenium import webdriver

driver= webdriver.Chrome("D:\\Softwares\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")


#using reg expression
#differ in using full versus reg exp in x_path and css_selector

#driver.find_element_by_xpath("//input[@type='submit']").click()
driver.find_element_by_xpath("//*[contains(@type,'submit')]").click()
#driver.find_element_by_css_selector('input[name="email"]').send_keys("umer")
print(driver.find_element_by_css_selector("[class*='alert-success']").text)
