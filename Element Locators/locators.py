from selenium import webdriver

driver= webdriver.Chrome(executable_path="D:\\Softwares\\chromedriver.exe")


driver.get("https://scholarships.bahria.edu.pk/peef-online-application/")

driver.find_element_by_name("item_meta[121]").send_keys("a")


driver.close()

