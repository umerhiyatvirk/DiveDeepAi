from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
#driver.find_element_by_xpath("//div[@class='products']/div")
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
originalAmt=float(driver.find_element_by_class_name("discountAmt").text)
driver.find_element_by_css_selector(".promocode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
time.sleep(10)
discountAmt=float(driver.find_element_by_class_name("discountAmt").text)
assert discountAmt < originalAmt
print("Original Amount:",originalAmt)
print("Discount Amount:",discountAmt)


