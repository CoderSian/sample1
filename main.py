from selenium import webdriver
from selenium.webdriver.common.by import By

#드라이버 초기화
driver = webdriver.Chrome("/Users/a1234/Documents/coding/python/sample1/chromedriver")
#URL 얻기
driver.get("https://www.musinsa.com/auth/login?referer=https%3A%2F%2Fwww.musinsa.com")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/div/a[1]').click()
driver.implicitly_wait(5)

driver.find_element(By.ID, 'id_email_2').send_keys('dyddlydb@naver.com')
driver.find_element(By.ID, 'id_password_3').send_keys('4600')
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/form/fieldset/div[8]/button[1]').click()
driver.implicitly_wait(5)