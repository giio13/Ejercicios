import time

import pytest

from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage


class Test_course_pack(WebDriverSetup):

    # Escenario 1
    def test_SearchGoogle(self):
        driver = self.driver
        self.driver.get(HomePage.get_homepage_url())
        home_page = HomePage(driver)
        home_page.search("Concredito")

    # Escenario 2
    def test_Lucky(self):
        driver = self.driver
        self.driver.get(HomePage.get_homepage_url())
        home_page = HomePage(driver)
        home_page.search_Lucky()

    # Escenario 3
    def test_double_Search(self):
        driver = self.driver
        self.driver.get(HomePage.get_homepage_url())
        home_page = HomePage(driver)
        home_page.double_Search("qa automation", "python")

    # Escenario 4
    def test_compare_Search(self):
        driver = self.driver
        self.driver.get(HomePage.get_homepage_url())
        home_page = HomePage(driver)
        home_page.compare_Search("carros")

    # Escenario 5
    def test_search_Images(self):
        driver = self.driver
        self.driver.get(HomePage.get_homepage_url())
        home_page = HomePage(driver)
        home_page.search_Images("dinosaurios")

        # Excel
    def test_Excel(self):
        driver = self.driver
        self.driver.get(HomePage.get_url_pruebas())
        home_page = HomePage(driver)
        home_page.Ejemplo_excel()