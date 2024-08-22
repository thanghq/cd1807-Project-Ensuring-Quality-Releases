# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (ts + '\t')

def login (user, password):
    print (timestamp() + 'Starting the browser...')
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print (timestamp() + 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID,"user-name").send_keys(user)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    print(timestamp() + 'Login with username {:s} and password {:s} successfully.'.format(user, password))
    return driver


def add_to_cart(driver, count):
    print (timestamp() +'Add items to cart')
    for i in range(count):
        element = "a[id='item_" + str(i) + "_title_link']"  
        driver.find_element(By.CSS_SELECTOR, element).click()  
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()  
        product = driver.find_element(By.CSS_SELECTOR, '.inventory_details_name.large_size').text  
        print(timestamp() + product + " added to shopping cart.") 
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()  
    print(timestamp() + '{:d} items are all added to shopping cart successfully.'.format(count))

def remove_item_in_cart(driver, count):
    print (timestamp() +'Remove items from cart')
    for i in range(count):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_secondary.btn_inventory").click()
        product = driver.find_element(By.CSS_SELECTOR, '.inventory_details_name.large_size').text
        print(timestamp() + product + " removed from shopping cart.") 
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
    print(timestamp() + '{:d} items removed from shopping cart successfully.'.format(count))

def add_to_cart_and_checkout(driver, count):
    print (timestamp() +'Add items to cart for check out')
    for i in range(count):
        element = "a[id='item_" + str(i) + "_title_link']"  
        driver.find_element(By.CSS_SELECTOR, element).click()  
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click() 
        product = driver.find_element(By.CSS_SELECTOR, '.inventory_details_name.large_size').text  
        print(timestamp() + product + " added to shopping cart.")  
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()  
    print(timestamp() + '{:d} items added to shopping cart.'.format(count))

def check_out(driver):
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge').click()  
    driver.find_element(By.ID, 'checkout').click() 
    driver.find_element(By.ID, "first-name").send_keys('John')
    driver.find_element(By.ID, "last-name").send_keys('Doe')
    driver.find_element(By.ID, "postal-code").send_keys('12345')
    driver.find_element(By.ID, 'continue').click() 
    driver.find_element(By.ID, 'finish').click() 
    status_check = driver.find_element(By.CSS_SELECTOR, '.complete-header').text
    print(timestamp() + status_check + " .Your order has been dispatched!")
    driver.find_element(By.ID, 'back-to-products').click()  

if __name__ == "__main__":
    COUNT = 5
    driver = login('standard_user', 'secret_sauce')
    add_to_cart(driver, COUNT)
    remove_item_in_cart(driver, COUNT)
    add_to_cart_and_checkout(driver, COUNT)
    check_out(driver)
    print(timestamp() + 'Selenium tests are completed!')