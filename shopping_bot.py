from random import *
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys


import time


binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')


class amazon_product:
    def __init__(self,username,password,url,limit):
        self.username=username
        self.password=password
        self.url=url
        self.limit=limit
        self.driver= webdriver.Firefox(firefox_binary=binary)
    
    def SignIn(self):
        driver=self.driver
        
        username_elem=driver.find_element_by_xpath('//input[@name="email"]')
        username_elem.clear()
        username_elem.send_keys(self.username)
        
        time.sleep(1.5)
        
        username_elem.send_keys(Keys.RETURN)
        time.sleep(1.5)
        
        password_elem=driver.find_element_by_xpath('//input[@name="password"]')
        password_elem.clear()
        password_elem.send_keys(self.password)
        time.sleep(1.5)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def findProduct(self):
        
        driver=self.driver
        
        driver.get(self.url)
        time.sleep(3)
        self.isProductAvailable()
        
        if self.isProductAvailable()== 'Currently unavailable' or self.isProductAvailable()=='Actuellement indisponible.' or self.isProductAvailable() == 'Currently unavailable.' :
            time.sleep(8)
            self.findProduct()
        
        elif self.isProductAvailable() <= self.limit:
            buy_nom=driver.find_element_by_name('submit.buy-now')
            buy_nom.click()
            time.sleep(1)
            self.SignIn()
            
            place_order=driver.find_element_by_class_name('place-your-order-button')
            place_order.click()
            time.sleep(1)
        
        else:
            time.sleep(3)
            self.findProduct()
            
    def isProductAvailable(self):
        driver=self.driver
        a=driver.find_element_by_class_name('a-color-price').text
        available=a.replace(',','.')
        
        if available == 'Currently unavailable' or available=='Actuellement indisponible.' or available == 'Currently unavailable.' :
            return available
        
        else:
            return float(available[5:])
        
    def closeBrowser(self):
        self.driver.close()
        
if __name__ == '__main__':
    product_url='https://www.amazon.ca/PlayStation-5-Console/dp/B08GSC5D9G/ref=sr_1_5?dchild=1&keywords=ps5&qid=1608737126&sr=8-5'
    shopBot=amazon_product('your-email','your-password',product_url,640)
    shopBot.findProduct()
    shopBot.closeBrowser()



