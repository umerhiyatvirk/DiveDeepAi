from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")



driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)