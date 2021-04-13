from selenium import webdriver

driver= webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radioButtons= driver.find_elements_by_name("radioButton")
print(len(radioButtons))

radioButtons[1].click()
assert radioButtons[1].is_selected()

driver.close()