import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

homepage_url = "https://www.google.com/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.google_search = "q"
        self.select_link = "//h3[contains(text(),'ConCrédito | Gana prestando')]"
        self.button_lucky = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]"
        self.click_Lucky = "/html/body/div[2]/div/div[1]/div[1]/ul/li[1]/div/div/a/img"
        self.first_search = "#rso > div:nth-child(1) > div > div.NJo7tc.Z26q7c.jGGQ5e > div > a > h3"
        self.second_search = "//h3[contains(text(),'Welcome to Python.org')]"
        self.element = "//body/div[@id='searchform']/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]"
        self.elements_page = "//div[@class='yuRUbf']//h3"
        self.second_page = "#botstuff > div > div:nth-child(2) > table > tbody > tr > td:nth-child(3) > a"
        self.images = "//body/div[@id='main']/div[@id='cnt']/div[@id='top_nav']/div[@id='hdtb']/div[@id='pTwnEc']/div[@id='hdtb-msb']/div[1]/div[1]/div[2]/a[1]"
        self.image_dinosaur = "#islrg > div.islrc > div:nth-child(6) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img"
        self.image_displayed = "#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div > a > img"
        self.close_image = "body.tQj5Y.ghyPEc.IqBfM.ecJEib.EWZcud.eejsDc.uirfo.notranslate.EIlDfe.cjGgHb.d8Etdd.Wq3Ysf.LcUz9d:nth-child(2) div.T1diZc.KWE8qe:nth-child(6) c-wiz.FA7L0b.P3Xfjc.SSPGKf.BIdYQ:nth-child(1) div.mJxzWe:nth-child(4) div.l39u4d:nth-child(2) div.WaWKOe.RfPPs:nth-child(3) div.A8mJGd div.dFMRD div:nth-child(2) a.hm60ue.CqeZic > svg:nth-child(1)"
        self.display = "//div[@id='Sva75c']"

    def search(self, Texto):
        self.get_google_search().send_keys(Texto + Keys.ENTER)
        time.sleep(5)
        self.get_select().click()
        current_Url = self.driver.current_url
        assert ("https://www.concredito.com.mx/" in current_Url)
        print(current_Url)
        time.sleep(5)

    def search_Lucky(self):
        self.get_button_Lucky().click()
        time.sleep(5)
        self.get_search_lucky().click()
        time.sleep(5)

    def double_Search(self, first_Text, second_Text):
        self.get_google_search().send_keys(first_Text + Keys.ENTER)
        time.sleep(5)
        self.get_first_search().click()
        time.sleep(5)
        current_Url = self.driver.current_url
        assert ("https://es.wikipedia.org/wiki/Hola_mundo" in current_Url)
        print(current_Url)
        self.driver.back()
        time.sleep(5)
        self.get_element().clear()
        self.get_element().send_keys(second_Text + Keys.ENTER)
        self.get_second_search().click()
        time.sleep(5)
        second_Url = self.driver.current_url
        assert ("https://www.python.org/" in second_Url)
        print(second_Url)

    def compare_Search(self, Texto):
        self.get_google_search().send_keys(Texto + Keys.ENTER)
        time.sleep(5)
        elements = self.get_elements_page()

        print("Primera Busqueda")
        for element in elements:
            print(element.text)

        self.get_second_page().click()
        time.sleep(5)
        elements2 = self.get_elements_page()

        print("\n Segunda Busqueda \n")
        for element2 in elements2:
            print(element2.text)

        assert element != element2
        print("los Elementos De La Busqueda Son Diferentes\n")

    def search_Images(self, Texto):
        self.get_google_search().send_keys(Texto + Keys.ENTER)
        time.sleep(5)
        self.get_images().click()
        time.sleep(5)
        self.get_select_image().click()
        image = self.get_image_displayed()
        width = int(image.get_attribute("naturalWidth"))
        height = int(image.get_attribute("naturalHeight"))
        time.sleep(5)

        # Verificamos que se abrio el cuadro de visualización Opcion 1
        if self.get_display().is_displayed():
            self.get_display().is_displayed()
            print("\nImagen Visualizada Correctamente")
            self.get_close_image().click()
            if self.get_display().is_enabled():
                print("La Imagen Se cerro Correctamente\n")
        else:
            print("La Imagen No Se Visualizo")

        # Opcion 2
        """if width == 300 and height == 168:
            print("Imagen desplegada")
            self.get_close_image().click()
            time.sleep(3)
        else:
            print("Imagen no desplegada")
        """
        time.sleep(5)

    def get_display(self):
        return self.driver.find_element(By.XPATH, self.display)

    def get_close_image(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.close_image)

    def get_image_displayed(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.image_displayed)

    def get_select_image(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.image_dinosaur)

    def get_images(self):
        return self.driver.find_element(By.XPATH, self.images)

    def get_second_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.second_page)

    def get_elements_page(self):
        return self.driver.find_elements(By.XPATH, self.elements_page)

    def get_google_search(self):
        return self.driver.find_element(By.NAME, self.google_search)

    def get_select(self):
        return self.driver.find_element(By.XPATH, self.select_link)

    def get_button_Lucky(self):
        return self.driver.find_element(By.XPATH, self.button_lucky)

    def get_search_lucky(self):
        return self.driver.find_element(By.XPATH, self.click_Lucky)

    def get_first_search(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.first_search)

    def get_second_search(self):
        return self.driver.find_element(By.XPATH, self.second_search)

    def get_element(self):
        return self.driver.find_element(By.XPATH, self.element)

    @staticmethod
    def get_homepage_url():
        return homepage_url
