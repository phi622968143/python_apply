from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import wget
import time

path = "C:/Users/User/Desktop/chromedriver.exe"  # chromedriver 的路徑
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get("https://www.pinterest.jp/")

log = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="fullpage-wrapper"]/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div'))
)
log.click()

acc = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
)
acc.send_keys("garry910311@gmail.com")
pa = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
)
pa.send_keys("622968143")
b = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div[2]/div/div/div/div/div/div[4]/form/div[7]/button'))
)
b.click()
s = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="searchBoxContainer"]/div/div/div[2]/input'))
)
s.click()
time.sleep(2)
keyw = "要找的關鍵字"
s.send_keys(keyw)
s.send_keys(Keys.RETURN)

# 收集圖片,根據關鍵字開資料夾
path = os.path.join(keyw)
os.mkdir(path)
c = 0
scroll_count = 0
max_scroll_count = 30
i=[]
while scroll_count < max_scroll_count:
    #每次下滑都要重新檢查元素是否在
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="pin"] img'))
    )
    imgs = driver.find_elements(By.CSS_SELECTOR, 'div[data-test-id="pin"] img')
    #找到沒存過的圖就下載
    for img in imgs:
        if img.get_attribute("src") not in i:
            i.append(img.get_attribute("src"))
        else:
            break
        save = os.path.join(path, keyw + str(c) + ".jpg")
        wget.download(img.get_attribute("src"), save)
        c += 1
    #完成後下滑
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #等待頁更新完成後進行下次掃描下載
    time.sleep(10)
    scroll_count += 1

driver.close()
