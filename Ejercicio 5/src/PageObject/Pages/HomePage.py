import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Funciones.FuncionesGenerales import Funciones_Generales
from Funciones import FuncionesExcel


homepage_url = "https://www.google.com/"
url_pruebas = "https://demoqa.com/text-box"
tiempo = .1

class HomePage:

    def __init__(self, driver):

        #Elementos de la pagina
        self.driver = driver
        self.google_search = "q"
        self.select_link = "//h3[contains(text(),'ConCrédito | Gana prestando')]"
        self.button_lucky = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]"
        self.click_Lucky = "/html/body/div[2]/div/div[1]/div[3]/ul/li[1]/div/div[1]/a/img"
        self.first_search = "//h3[contains(text(),'What is automated QA testing?')]"
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
        try:
            self.get_google_search().send_keys(Texto + Keys.ENTER)
            time.sleep(tiempo)
            self.get_select().click()
            current_Url = self.driver.current_url
            assert ("https://www.concredito.com.mx/" in current_Url)
            print("\n" + current_Url)
            time.sleep(tiempo)
        except TimeoutException as ex:
            print(ex.msg)

    def search_Lucky(self):
        try:
            self.get_button_Lucky().click()
            time.sleep(tiempo)
            self.get_search_lucky().click()
            time.sleep(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no esta disponible")

    def double_Search(self, first_Text, second_Text):
        try:
            self.get_google_search().send_keys(first_Text + Keys.ENTER)
            time.sleep(tiempo)
            self.get_first_search().click()
            time.sleep(tiempo)
            current_Url = self.driver.current_url
            assert ("https://www.globalapptesting.com/blog/automated-qa-testing" in current_Url)
            print("\n" + current_Url)
            self.driver.back()
            time.sleep(tiempo)
            self.get_element().clear()
            self.get_element().send_keys(second_Text + Keys.ENTER)
            self.get_second_search().click()
            time.sleep(tiempo)
            second_Url = self.driver.current_url
            assert ("https://www.python.org/" in second_Url)
            print(second_Url)
        except TimeoutException as ex:
            print(ex.msg)

    def compare_Search(self, Texto):
        try:
            self.get_google_search().send_keys(Texto + Keys.ENTER)
            time.sleep(tiempo)
            elements = self.get_elements_page()

            print("\nPrimera Busqueda")
            for element in elements:
                print(element.text)

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(tiempo)
            self.get_second_page().click()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(tiempo)
            elements2 = self.get_elements_page()

            print("\n Segunda Busqueda")
            for element2 in elements2:
                print(element2.text)

            assert element != element2
            print("Los Elementos De La Busqueda Son Diferentes\n")
        except TimeoutException as ex:
            print(ex.msg)

    def search_Images(self, Texto):
        try:
            self.get_google_search().send_keys(Texto + Keys.ENTER)
            self.get_images().click()
            self.get_select_image().click()
            time.sleep(tiempo)
            image = self.get_image_displayed()

            # Verificamos que se abrio el cuadro de visualización
            if self.get_display().is_displayed() == True:
                print("\nImagen Visualizada Correctamente")
                self.get_close_image().click()
                if self.get_display().is_enabled():
                    print("La Imagen Se cerro Correctamente\n")
                    time.sleep(tiempo)
            else:
                print("La Imagen No Se Visualizo")
        except TimeoutException as ex:
            print(ex.msg)
            print("Elemento no encontrado")

    def Ejemplo_excel(self):
        ruta = "C:\\Users\\jhiovany.moreno\\Downloads\\Curso_selenium\\Excel\\Datos_ok.xlsx"
        FuncionExcel = FuncionesExcel.Funexcel(self.driver)
        filas = FuncionExcel.getRowCount(ruta, "Hoja1")
        Fg = Funciones_Generales(self.driver)

        try:
            for fila in range(2, filas + 1):
                nombre = FuncionExcel.readData(ruta, "Hoja1", fila, 1)
                email = FuncionExcel.readData(ruta, "Hoja1", fila, 2)
                dir1 = FuncionExcel.readData(ruta, "Hoja1", fila, 3)
                dir2 = FuncionExcel.readData(ruta, "Hoja1", fila, 4)

                Fg.Texto_Mixto("id", "userName", nombre, tiempo)
                Fg.Texto_Mixto("id", "userEmail", email, tiempo)
                Fg.Texto_Mixto("id", "currentAddress", dir1, tiempo)
                Fg.Texto_Mixto("id", "permanentAddress", dir2, tiempo)
                Fg.Click_Mixto("id", "submit", tiempo)

                e = Fg.Existe("id", "name", tiempo)
                if (e == "Existe"):
                    print("El elemento se inserto correctamente")
                    FuncionExcel.writeData(ruta, "Hoja1", fila, 5, "Insertado")
                else:
                    print("No se inserto")
                    FuncionExcel.writeData(ruta, "Hoja1", fila, 5, "Error")

        except TimeoutException as ex:
            print(ex.msg)
            print("Fallo el Metodo Excel")

    def get_display(self):
        return self.driver.find_element(By.XPATH, self.display)

    def get_close_image(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.close_image)))

    def get_image_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.image_displayed)))

    def get_select_image(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.image_dinosaur)))

    def get_images(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.images)))

    def get_second_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.second_page)))

    def get_elements_page(self):
        return self.driver.find_elements(By.XPATH, self.elements_page)

    def get_google_search(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.google_search)))

    def get_select(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.select_link)))

    def get_button_Lucky(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.button_lucky)))

    def get_search_lucky(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.click_Lucky)))

    def get_first_search(self):
        return self.driver.find_element(By.XPATH, self.first_search)

    def get_second_search(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.second_search)))

    def get_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.element)))

    @staticmethod
    def get_homepage_url():
        return url_pruebas

    @staticmethod
    def get_url_pruebas():
        return url_pruebas