from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='../../.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://tiki.vn/dien-thoai-may-tinh-bang/c1789')

driver.execute_script('window.scrollTo(0, 300)')
driver.implicitly_wait(3)

products = driver.find_elements(By.CLASS_NAME, 'product-item')

for p in products[:8]:
    title = p.find_element(By.CSS_SELECTOR, '.info h3')
    link = p.get_attribute('href')

    print(title.text)
    print(link)

driver.quit()


