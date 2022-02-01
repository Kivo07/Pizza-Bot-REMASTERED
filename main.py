import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import ui


dv = webdriver.Chrome(executable_path=r"C:/Users/Kivanc's Account/Desktop/Selenium Drivers/chromedriver.exe")
dv.get("https://www.dominos.ca/en/")

# Clicking the delivery button


def deliver():
    delivery_button = ui.WebDriverWait(dv, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "smart-order__cta-container")))
    delivery_button.click()


deliver()

# A class made to show the attributes of someone who wants pizza


class PizzaBuyer:
    def __init__(self, address, city, province, postal):
        self.address = address
        self.city = city
        self.province = province
        self.postal = postal

# A person who wants pizza


Nathan = PizzaBuyer("123 Somewhere street", "Toronto", "ON", "Postal Code")

# A function made to fill out the order information


def info():
    add = ui.WebDriverWait(dv, 10).until(ec.element_to_be_clickable((By.ID, "Street"))).send_keys(Nathan.address)
    city = ui.WebDriverWait(dv, 10).until(ec.element_to_be_clickable((By.ID, "City"))).send_keys(Nathan.city)
    prov = ui.WebDriverWait(dv, 10).until(ec.element_to_be_clickable((By.ID, "Region"))).send_keys(Nathan.province)
    postal_code = dv.find_element(By.ID, "Postal_Code")
    postal_code.click()
    postal_code.send_keys(Nathan.postal)
    deliv_button = dv.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    deliv_button.click()


info()
