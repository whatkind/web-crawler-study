from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.huya.com/g/1663#cate-1-116")
n = 1
try:
    while True:
        print('=============================>第'+str(n)+"页")
        n += 1
        sleep(5)
        html = driver.page_source
        # print(html)
        names = driver.find_elements_by_xpath('//i[@class="nick"]')
        members = driver.find_elements_by_xpath('//i[@class="js-num"]')
        links = driver.find_elements_by_xpath('//a[@class="title"]')
        pics = driver.find_elements_by_xpath('//img[@class="pic"]')
        for name, member, link, pic in zip(names, members, links, pics):
            print('主播：' + name.text, '观看人数：' + member.text)
            print('房间', link.get_attribute('href'))
            print('封面', pic.get_attribute('data-original'))
            print("\r\n")
        if html.find('laypage_next') != -1:
            driver.find_element_by_xpath('//a[@class="laypage_next"]').click()
        else:
            break
except Exception as e:
    print('程序报错', e)
finally:
    sleep(3)
    driver.quit()
