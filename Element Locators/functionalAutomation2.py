from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("discountAmt")

driver.close()
