import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
products = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for product in products:
    product.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,7)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name('promoBtn').click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element_by_class_name("promoInfo").text)

