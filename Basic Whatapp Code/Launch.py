from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(20)
element=driver.find_element(By.XPATH,"//div[text()='Log in with phone number']")
print(element.is_displayed())
a=driver.find_element(By.ID,"link-device-phone-number-code-screen-instructions").text
print(a)

b=driver.find_element(By.XPATH,"//div[@class='x1c4vz4f xs83m0k xdl72j9 x1g77sc7 x78zum5 xozqiw3 x1oa3qoh x12fk4p8 "
                               " x1r0jzty xeuugli x2lwn1j x1nhvcw1 xdt5ytf x1cy8zhl']").text
print(b)

driver.close()
