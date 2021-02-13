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
