from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

chromedriver = 'C://chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(2)

def posting(id, pw, url, post_title, post_content):
    # 티스토리 접속
    driver.get('https://www.tistory.com/auth/login#')
    driver.find_element(By.XPATH, '//*[@id="cMain"]/div/div/div/a[1]').click()
    time.sleep(1)

    # 로그인
    username=driver.find_element(By.XPATH, '//*[@id="input-loginKey"]')
    username.send_keys(id)
    time.sleep(1)

    password=driver.find_element(By.XPATH, '//*[@id="input-password"]')
    password.send_keys(pw)
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
    time.sleep(1)

    # 글 작성 페이지 이동
    driver.get(f"{url}/manage/post")
    time.sleep(1)

    # 타이틀 작성
    title=driver.find_element(By.XPATH, '//*[@id="post-title-inp"]')
    title.send_keys(post_title)
    time.sleep(1)

    # 본문 작성
    iframe = driver.find_element(By.CSS_SELECTOR, ('iframe'))
    driver.switch_to.frame(iframe)
    content = driver.find_element(By.ID, 'tinymce')
    content.send_keys(post_content)
    driver.switch_to.default_content()
    time.sleep(1)

    #발행
    driver.find_element(By.CSS_SELECTOR, '#publish-layer-btn').click()
    driver.find_element(By.CSS_SELECTOR, '#publish-btn').click()
    time.sleep(1)

posting('id', 'pw', 'url', 'title', 'content')


while True:
    pass