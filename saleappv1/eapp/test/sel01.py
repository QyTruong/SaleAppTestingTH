from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='../../.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://vnexpress.net/')

driver.execute_script('window.scrollTo(0, 2250)')
driver.implicitly_wait(3)

articles = driver.find_elements(By.CSS_SELECTOR, '#automation_TV0 > article')

for article in articles:
    title = article.find_element(By.TAG_NAME, 'h3')
    img = article.find_element(By.CSS_SELECTOR, '.thumb-art img, .thumb-art video, .thumb-art gif')


    print(title.text)
    print(img.get_attribute('src'))

driver.quit()

