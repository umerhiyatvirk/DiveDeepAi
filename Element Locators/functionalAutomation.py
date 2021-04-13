from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)

list = []
list2 = []
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4 general x path
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)

#products = driver.find_elements_by_xpath("//div[@class='product']/h4")
#for product in products:
    #print(product.text)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

names = driver.find_elements_by_css_selector("p.product-name")
print(len(names))
for name in names:
    list2.append(name.text)
print(list2)

assert list == list2

driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
print(driver.find_element_by_class_name("promoInfo").text)


driver.close()


