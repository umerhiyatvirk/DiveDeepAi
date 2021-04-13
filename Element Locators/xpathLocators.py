from selenium import webdriver

driver= webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/#/practice-project")

#driver.find_element_by_xpath("//input[@name='email']").send_keys("umervirk.499@gmail.com")
driver.find_element_by_xpath("//button[@type='submit']").click()

#driver.minimize_window()
#driver.close()
#driver.quit()


