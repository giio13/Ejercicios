import time

import pytest

from PageObject import HomePage
from TestBase.WebDriver import WebDriverSetup
from PageObject.HomePage import HomePage

#Autor: Jhiovany Moreno Gamez


class Test_course_pack(WebDriverSetup):

    #Escenario 1
    def test_SearchGoogle(self):
        driver = self.driver
        self.driver.get(HomePage.get_homepage_url())
        home_page = HomePage(driver)
        home_page.search("Concredito")
        time.sleep(3)

    #Escenario 2
    def test_Lucky(self):
        driver = self.driver
        self.driver.get(HomePage.get_homepage_url())
        home_page = HomePage(driver)
        home_page.search_Lucky()
        time.sleep(3)

    #Escenario 3
    def test_double_Search(self):
        driver = self.driver
        self.driver.get(HomePage.get_homepage_url())
        home_page = HomePage(driver)
        home_page.double_Search("hola mundo", "python")
        time.sleep(3)

    #Escenario 4
    def test_compare_Search(self):
        driver = self.driver
        self.driver.get(HomePage.get_homepage_url())
        home_page = HomePage(driver)
        home_page.compare_Search("carros")
        time.sleep(3)

    #Escenario 5
    def test_search_Images(self):
        driver = self.driver
        self.driver.get(HomePage.get_homepage_url())
        home_page = HomePage(driver)
        home_page.search_Images("dinosaurios")
        time.sleep(3)
