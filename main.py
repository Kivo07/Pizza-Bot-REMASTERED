import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys


dv = webdriver.Chrome(executable_path=r"C:/Users/Kivanc's Account/Desktop/Selenium Drivers/chromedriver.exe")
dv.get("https://www.dominos.ca/en/")
dv.maximize_window()

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


Nathan = PizzaBuyer("731 Sundew Drive", "Waterloo", "ON", "N2K 0B4")

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

# This function opens up the pizza menu


def makepizza():
    pizza = ui.WebDriverWait(dv, 10).until(ec.element_to_be_clickable((By.ID, "csn-Pizza"))).click()


makepizza()

# This function scrolls down to my preferred pizza

# XPATH was used, make sure it is updated regularly


def scroll():
    pepperoni = dv.find_element(By.XPATH, '//*[@id="categoryPage2"]/section/div/div[12]/div/a[1]')
    pepperoni.send_keys(Keys.PAGE_DOWN)
    pepperoni.send_keys(Keys.HOME)
    pepperoni.send_keys(Keys.PAGE_DOWN)
    pepperoni.click()


dv.implicitly_wait(10)

scroll()

