import time

from selenium import webdriver #webdriver is class#selenium is a package
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
my_options = Options()
my_options.add_argument('--start-maximized')
#my_options.add_argument('--window-size=800,600')

#my_options.headless = False

                                             #ctrl+right click to see the definitation for that class
my_driver=webdriver.Chrome(options=my_options)  #object is created for class chrome
my_driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#my_driver.maximize_window()
time.sleep(5)
element_username= my_driver.find_element(By.NAME,"username")
#by os the class , class is type
#my_driver.find_element(by=By.NAME, value="username")
element_username.send_keys("admin")                                                      #cntrl +f to open the element search bar
element_password=my_driver.find_element(By.NAME, "password")
element_password.send_keys("admin123")
# element_login_btn=my_driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main" "orangehrm-login-button")
element_login_btn=my_driver.find_element(By.XPATH, '//form/div[3]/button')
element_login_btn.click() # xpath#address to web element webpage
time.sleep(10)

element_pim =my_driver.find_element(By.XPATH,"//span[text()='PIM']")
element_pim.click()
time.sleep(5)
add_employee_btn=my_driver.find_element(By.XPATH,"//button[text()=' Add ']")
add_employee_btn.click()
time.sleep(5)
first_name=my_driver.find_element(By.NAME,"firstName")
first_name.send_keys("Rabin")
time.sleep(2)
middle_name=my_driver.find_element(By.NAME,"middleName")
middle_name.send_keys("S")
time.sleep(3)
last_name=my_driver.find_element(By.NAME,"lastName")
last_name.send_keys("raju")
time.sleep(3)
#employee_id=my_driver.find_element(By.XPATH,"0373")
#employee_id.send_keys("21001061")
#time.sleep(10)
save_btn=my_driver.find_element(By.XPATH,"//button[@type='save']")
save_btn.click()
time.sleep(3)


