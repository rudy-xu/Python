import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# 切换窗口的函数
def to_new_handler(driver, *have_handlers):
  # 句柄切换，拿到所有句柄(窗口)
  handlers = driver.window_handles

  for h in handlers:
    if h not in have_handlers:
      driver.switch_to.window(h)

  return driver


service = Service('./msedgedriver.exe')

# 设置浏览器 options
options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()

# 打开网页
driver.get("https://www.douban.com/")

# =============== By.Selector 查找元素
readBook_ele = driver.find_element(by=By.CSS_SELECTOR, value='#anony-nav > div.anony-nav-links > ul > li:nth-child(1) > a').click()

# 切换窗口
readBook_handler = driver.current_window_handle
to_new_handler(driver, readBook_handler)
print("当前页面是：" + driver.title)

# =============== By.ID 查找元素
input_ele = driver.find_element(by=By.ID, value="inp-query")
time.sleep(2)
input_ele.send_keys("余华")

# =============== By.Xpath 查找元素
search_ele = driver.find_element(by=By.XPATH, value='//*[@id="db-nav-book"]/div[1]/div/div[2]/form/fieldset/div[2]').click()
time.sleep(2)

# 页面滚动
driver.execute_script("window.scrollBy(0,800)")
time.sleep(2)

# 打开链接
driver.find_element(by=By.LINK_TEXT, value="许三观卖血记").click()
time.sleep(2)

electricBook_ele = driver.find_element(by=By.CSS_SELECTOR, value='#db-nav-book > div.nav-secondary > div > ul > li:nth-child(2) > a')
electricBook_ele.click()

# 切换窗口
xuSanGuan_handler = driver.current_window_handle
to_new_handler(driver, readBook_handler, xuSanGuan_handler)
print("当前页面是：" + driver.title)
time.sleep(5)

# 关闭当前窗口
driver.close()

#关闭浏览器
time.sleep(5)
driver.quit()
