from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://bologe.net/portal.php')
driver.maximize_window()
driver.implicitly_wait(30)
# 菠萝壳注册模块
driver.find_element_by_xpath("//li/a[text()='立即注册']").click()
driver.find_element_by_id('phone').send_keys('18820855535')
driver.find_element_by_xpath("//*[text()='免费获取手机动态码']").submit()
driver.find_element_by_name('verfiy').send_keys('85756')
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('huang1234')
driver.find_element_by_xpath("//*[@name='passwd_2']").send_keys("huang1234")
try:
    driver.find_element_by_id('registerformsubmit').submit()
except BaseException as msg:
    print(msg)

driver.quit()
