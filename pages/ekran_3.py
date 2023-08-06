from Automatyzacja.base.base_driver import BaseDriver
from Automatyzacja.utilities.util import Utils
from selenium.webdriver.common.by import By
import logging


class Ekran3(BaseDriver):

    """
    Klasa ta odpowiada za określenie lokatorów strony 3 w procesie Spingo Standard.
    Następnie wykonuje select na każdym z wyżej wymienionych elementów i je zwraca.
    Następnie są wykonywane na tych elementach różne akcje i funkcję te są następnie
    wywoływane w testcase.
    """

    log = Utils().custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver 

    # Locators
    KOD_WERYFIKACYJNY_SMS = 'input#ctl00_CPH_Content__V_FKT_FPAY_OFERTA__Q__KOD_PIN'
    KOD_WERYFIKACJI_SMS_POTWIERDZ_BTN = 'input#ctl00_CPH_nav_POROZUMIENIE_Button3_PP020_NOWY_WNIOSEK_A070_POTWIERDZ_PIN'
    
    def kod_weryfikacji_sms_inpt_field(self):
        return self.long_wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.KOD_WERYFIKACYJNY_SMS)
    
    def kod_weryfikacji_sms_potwierdz_btn_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.KOD_WERYFIKACJI_SMS_POTWIERDZ_BTN)
    
    # Funkcje docelowe
    def kod_weryfikacji_sms_inpt(self, sms_inpt):
        self.log.info(f'Kod weryfikacji SMS: ' + sms_inpt)
        self.kod_weryfikacji_sms_inpt_field().send_keys(sms_inpt)
    
    def kod_weryfikacji_sms_potwierdz_btn(self):
        self.kod_weryfikacji_sms_potwierdz_btn_field().click()

    def ekran3(self, sms_inpt):
        self.kod_weryfikacji_sms_inpt(sms_inpt)
        self.kod_weryfikacji_sms_potwierdz_btn()