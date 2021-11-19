from selenium import webdriver
import time

path = "C:\swing\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("http://zzzscore.com/1to50/")
num = 1
btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

while num <= 50:
    for btn in btns:
        if btn.text == str(num):
            btn.click()
            print(str(num) + "클릭")
            num = num + 1
