from Automatyzacja.base.base_driver import BaseDriver
from Automatyzacja.utilities.util import Utils
from selenium.webdriver.common.by import By
import logging

class Ekran4(BaseDriver):

    """
    Klasa ta odpowiada za określenie lokatorów strony 4 w procesie Spingo Standard.
    Następnie wykonuje select na każdym z wyżej wymienionych elementów i je zwraca.
    Następnie są wykonywane na tych elementach różne akcje i funkcję te są następnie
    wywoływane w testcase.
    """

    log = Utils().custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    WZOR_POROZUMIENIA = 'a#ctl00_CPH_Content_linFile_V_FKT_FPAY_POROZUMIENIE__Q__POROZUMIENIE'
    ZAPLAC_SPINGO_BTN = 'input#ctl00_CPH_nav_POROZUMIENIE_Button1_PP020_NOWY_WNIOSEK_A070_AKCEPTUJ_PORZUMIENIE'
    
    def wzor_porozumienia_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.WZOR_POROZUMIENIA)
    
    def zaplac_spingo_btn_field(self):
        return self.long_wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.ZAPLAC_SPINGO_BTN)
    
    # Funkcje docelowe
    def wzor_porozumienia(self):
        self.wzor_porozumienia_field().click()
    
    def zaplac_spingo_btn(self):
        self.zaplac_spingo_btn_field().click()
        self.log.info('Kliknięto przycisk zaplać spingo')

    def ekran4(self):
        self.zaplac_spingo_btn()