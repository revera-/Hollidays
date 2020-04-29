## логирование в системе lara@lara.ru / 123123

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_login():

    #логин
    driver = webdriver.Chrome('/home/lara/PycharmProjects/chromedriver_linux64/chromedriver')
    driver.implicitly_wait(5)
    driver.get("https://tms-lite-test1.artlogics.ru/")
    time.sleep(5)

    driver.find_element_by_name("login").click()
    driver.find_element_by_name("login").clear()
    driver.find_element_by_name("login").send_keys("lara@lara.ru")
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("123123")
    driver.find_element_by_name("password").send_keys(Keys.ENTER)
    time.sleep(5)

    # выбор представления
    driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/div/div").click()
    driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/div/div[2]/div[4]/span").click()
    time.sleep(5)


    #найти накладную через фильтр в поле
    driver.find_element_by_xpath(
        "//div[@id='root']/div/div[3]/div/table/thead/tr/th[2]/div/div[2]/div/button/i").click()
    driver.find_element_by_name("orderNumber").clear()
    driver.find_element_by_name("orderNumber").send_keys("107651741")
    driver.find_element_by_name("orderNumber").send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//div[@id='root']/div/div[3]/div").click()
    time.sleep(2)
    #driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div[3]/button[4]/i").click() #очистка фильтров
    #time.sleep(2)


    #ввести данные в гриде в поле Сумма заказа
    driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/button/i").click()
    ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
        "//div[@id='fieldModal']/div[2]/div/div/div/div/div[66]/div")))).double_click().perform() #двойной клик по полю для перемещия в свое представление
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='fieldModal']/div[3]/div[2]/button[2]").click()
    time.sleep(1)

    #устанавливаем значение в поле в гриде = 100
    driver.find_element_by_xpath("//div[@id='root']/div/div[3]/div/table/tbody/tr/td[3]/div/div").click()
    time.sleep(1)
    driver.find_element_by_name("orderAmountExcludingVAT").clear()
    driver.find_element_by_name("orderAmountExcludingVAT").send_keys("100")
    driver.find_element_by_xpath("//div[3]/div/div[3]/button[2]").click()
    time.sleep(5)

    # очищаем значение в 0
    driver.find_element_by_xpath("//div[@id='root']/div/div[3]/div/table/tbody/tr/td[3]/div/div").click()
    driver.find_element_by_name("orderAmountExcludingVAT").clear()
    driver.find_element_by_name("orderAmountExcludingVAT").send_keys("0")
    driver.find_element_by_name("orderAmountExcludingVAT").send_keys(Keys.ENTER)
    #driver.find_element_by_xpath("//div[3]/div/div[3]/button[2]").click()
    time.sleep(5)



    #logout
    driver.find_element_by_xpath("//div[@id='root']/header/div/div[4]/div[2]/div/div").click()
    driver.find_element_by_xpath("//div[@id='root']/header/div/div[4]/div[2]/div/div[2]/div[2]").click()
    time.sleep(5)






    driver.quit()

test_login()
