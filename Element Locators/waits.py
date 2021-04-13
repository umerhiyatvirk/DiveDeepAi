import time
from selenium import webdriver

driver= webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#implicit waits
#explicit waits
#pause the test for few seconds using time class

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
products= driver.find_elements_by_xpath("//div[@class='product-action']/button")

for product in products:
    product.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
#driver.find_element_by_xpath("//div[@class='action-block']/button").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
