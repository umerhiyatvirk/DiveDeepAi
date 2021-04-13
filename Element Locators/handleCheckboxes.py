from selenium import webdriver

driver= webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()

driver.close()