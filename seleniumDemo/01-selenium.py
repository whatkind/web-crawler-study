from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.4j4j.cn/beauty/photos/57218.html")
# driver.get("https://www.baidu.com")
# 将当前网页截图保存
# driver.save_screenshot('pic.png')
# 获取当前网页源代码
html = driver.page_source
print(html)
driver.quit()


# 百度输入搜索例子
def run():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id("kw").send_keys("python")
    driver.find_element_by_id("su").click()
    sleep(10)
    driver.close()


# 无头模式
def chrome_headless():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome = webdriver.Chrome(options=options)
    chrome.get('https://www.baidu.com/')
    html = chrome.page_source
    print(html)