import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pages
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_S6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is("Samsung galaxy s6")

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(3)
    homepage.check_monitor_count(2)

