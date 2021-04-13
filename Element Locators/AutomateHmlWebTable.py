from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
prices = driver.find_elements_by_xpath("//tr/td[5]/p")
sum=0
for price in prices:
    sum+=int(price.text)

print(sum)
totalAmount = driver.find_element_by_class_name("totAmt").text
print(totalAmount)
assert sum == int(totalAmount)



