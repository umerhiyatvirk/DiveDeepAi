from selenium import webdriver
#import selenium.webdriver.support.select.Select

driver=webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

dropdown= Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)
#dropdown.select_by_value("M")
