from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from selenium.webdriver.firefox.options import Options
# option=webdriver.FirefoxOptions()

# option.add_argument('headless')
option=Options()
option.headless=True
driver = webdriver.Firefox(firefox_options=option)
# driver = webdriver.PhantomJS('E:\\TGbot for translation\\Telegram-channel-translator\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')

driver.get("https://translate.google.com/")




# driver.findElement(By.xpath("//div[@class='value test']"));
#

#
# tree = html.fromstring(page_source)
# img_tag_texts=tree.xpath('//img[@id="screenshot-image"]')[0].attrib

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#print(len(driver.find_elements_by_class_name("VfPpkd-LgbsSe")))
# driver.find_element_by_class_name("WpHeLc VfPpkd-mRLv6 VfPpkd-RLmnJb").click()
#print((By.CSS_SELECTOR,".VfPpkd-LgbsSe"))
wait = WebDriverWait(driver,10)
# wait.until(EC.element_to_be_clickable((By.XPATH(".VfPpkd-LgbsSe")))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe']"))).click()
#(By.CSS_SELECTOR,".")
#VfPpkd-dgl2Hf-ppHlrf-sM5MNb
#driver.find_elements_by_class_name("VfPpkd-LgbsSe")[4]
#driver.find_elements_by_class_name("VfPpkd-LgbsSe")[4].click()


# elements = driver.find_elements_by_class_name("VfPpkd-LgbsSe")
# elements[1].click()
# print(elements)
html = driver.page_source
driver.find_element_by_xpath("//textarea[@class='er8xn']").send_keys("Привіт")
#VfPpkd-Bz112c-LgbsSe VfPpkd-Bz112c-LgbsSe-OWXEXe-e5LLRc-SxQuSe yHy1rc eT1oJ qiN4Vb itOtF IK3GNd
wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='VfPpkd-Bz112c-LgbsSe VfPpkd-Bz112c-LgbsSe-OWXEXe-e5LLRc-SxQuSe yHy1rc eT1oJ qiN4Vb itOtF IK3GNd']"))).click()

# print(driver.save_screenshot("123.png"))
print(driver.find_element_by_xpath("//span[@jsname='W297wb']").text)

#print(html)
driver.close()
def translate(text):
    driver = webdriver.Firefox(firefox_options=option)
    driver.get("https://translate.google.com/")

    try:
        wait = WebDriverWait(driver, 3)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe']"))).click()
    except:
        print("i guess no cookie")
    driver.find_element_by_xpath("//textarea[@class='er8xn']").send_keys(text)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH,
                                           "//button[@class='VfPpkd-Bz112c-LgbsSe VfPpkd-Bz112c-LgbsSe-OWXEXe-e5LLRc-SxQuSe yHy1rc eT1oJ qiN4Vb itOtF IK3GNd']"))).click()
    #print(driver.find_element_by_xpath("//span[@jsname='W297wb']").text)
    #print(driver.save_screenshot("123.png"))
    txt=driver.find_element_by_xpath("//span[@jsname='W297wb']").text
    driver.close()
    return txt
print(translate("Андрій побив рекорд"))