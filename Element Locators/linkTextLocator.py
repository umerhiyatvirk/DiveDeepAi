from selenium import webdriver

driver= webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")

driver.maximize_window()
driver.get("https://login.salesforce.com/")

driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_partial_link_text("Sandbox").click()

#driver.minimize_window()
#driver.close()
#driver.quit()