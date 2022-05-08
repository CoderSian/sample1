from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

mobile_emulation = { "deviceName": "iPhone SE" } 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation) 
driver = webdriver.Chrome("/Users/a1234/Documents/coding/python/sample1/chromedriver",options=chrome_options)

#드라이버 초기화
# driver = webdriver.Chrome("/Users/a1234/Documents/coding/python/sample1/chromedriver")
# options = webdriver.ChromeOptions()
# options.EnableMobileEmulation("iPhone X")
#URL 얻기
driver.get("https://www.musinsa.com/auth/login?referer=https%3A%2F%2Fwww.musinsa.com")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/div/a[1]').click()
driver.implicitly_wait(5)

driver.find_element(By.ID, 'id_email_2').send_keys('dyddlydb@naver.com')
driver.find_element(By.ID, 'id_password_3').send_keys('4600')
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/form/fieldset/div[8]/button').click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, '/html/body/main/div[2]/section[1]/div/button').click()
driver.get('https://www.musinsa.com/snap?tabtype=today&sorttype=new')
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/div/article[2]/div/div[2]/button[2]').click()

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/section/div[2]/div[3]/div/div/div[1]/div[2]/button').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/section/div[2]/div[3]/div/div/div[2]/div[2]/button').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/section/div[2]/div[3]/div/div/div[3]/div[2]/button').click()

driver.get('https://www.musinsa.com/member/mission/snap-daily-like')

