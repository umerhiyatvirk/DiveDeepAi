from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

value="umer"
driver.find_element_by_id("name").send_keys(value)
driver.find_element_by_id("confirmbtn").click()

time.sleep(2)

alert = driver.switch_to.alert
alertText = alert.text
assert value in alertText
#alert.accept()
alert.dismiss()