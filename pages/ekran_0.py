from Automatyzacja.base.base_driver import BaseDriver
from Automatyzacja.utilities.util import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging


class LaunchPage(BaseDriver):

    """
    Klasa ta odpowiada za określenie lokatorów strony 0 w procesie Spingo Standard.
    Następnie wykonuje select na każdym z wyżej wymienionych elementów i je zwraca.
    Następnie są wykonywane na tych elementach różne akcje i funkcję te są następnie
    wywoływane w testcase.
    """

    log = Utils().custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    ACCEPT_COOKIES = 'a#hs-eu-confirmation-button'
    DECLINCE_COOKIES = 'a#hs-eu-decline-button'
    WYSZUKAJ_BUTTON_0 = 'input[name="ctl00$CPH$nav_DANE_FIRMY_WPROWADZ_NIP_Button1_PP020_NOWY_WNIOSEK_A040_AP_POBIERZ_DANE_FIRMY_NEW"]'
    INPUT_NIP_0 = 'input#ctl00_CPH_Content__V_FKT_FPAY_FIRMA_DANE__Q__NIP'

    # Extraction
    def input_nip_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.INPUT_NIP_0)

    def accept_cookies_button(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.ACCEPT_COOKIES)

    def get_wyszukaj_button_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.WYSZUKAJ_BUTTON_0)

    # Functions
    def input_nip_0(self, nip):
        self.log.info('NIP:' + nip)
        self.input_nip_field().send_keys(nip)

    def click_cookies_button(self):
        self.accept_cookies_button().click()

    def get_wyszukaj_button_0(self):
        self.get_wyszukaj_button_field().click()

    def ekran0(self, nip):
        self.input_nip_0(nip)
        self.click_cookies_button()
        self.get_wyszukaj_button_0()
