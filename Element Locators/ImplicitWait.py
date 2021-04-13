from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.implicitly_wait(5)
# wait until 5 seconds if object is not displayed
#Global wait
#1.5 second to reach next page- execution will resume in 1.5 seconds
#if object do not show up at all, then max time your test waits for 5 seconds
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count )
products = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for product in products:
    product.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
#driver.find_element_by_xpath("//div[@class='action-block']/button").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#driver.find_element_by_class_name("promoCode")
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name('promoBtn').click()
print(driver.find_element_by_class_name("promoInfo").text)