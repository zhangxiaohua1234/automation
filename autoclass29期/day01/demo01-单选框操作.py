from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

# from webdriver_manager.chrome import webdriver

mydriver = webdriver.Chrome()


mydriver.get(r"D:\autoclass29期\selenium_demo\selenium_demo\selenium.html")

# XPATH查找
xpath_str1 = "/html/body/div[2]/div[2]/div/form/div[3]/label[1]"
xpath_str2 = "/html/body/div[2]/div[2]/div/form/div[3]/label[2]"

radio1 = mydriver.find_element(by=By.XPATH, value=xpath_str1)
radio2 = mydriver.find_element(by=By.XPATH, value=xpath_str2)

for i in range(3):
    if radio1.is_selected():
        radio2.click()
    else:
        radio1.click()