from Automatyzacja.base.base_driver import BaseDriver
from Automatyzacja.utilities.util import Utils
from selenium.webdriver.common.by import By
import logging


class Ekran5(BaseDriver):

    """
    Klasa ta odpowiada za określenie lokatorów strony 5 w procesie Spingo Standard.
    Następnie wykonuje select na każdym z wyżej wymienionych elementów i je zwraca.
    Następnie są wykonywane na tych elementach różne akcje i funkcję te są następnie
    wywoływane w testcase.
    """

    log = Utils().custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    TWOJE_ZAMOWIENIE_ZOSTALO_OPLACONE ='div[class="col-xs-offset-0 col-xs-12 col-sm-offset-0 col-sm-12 col-md-offset-0 col-md-12 fepColPad fepDefFont fepDefFontTab fepDefFontMob"] p'
    NA_PODANY_ADRES_EMAIL = '//div[@id="ctl00_CPH_Content_FKT_FPAY_KOMUNIKAT_1__lab"]//div//span[contains(text(), "Na")]'
    DOWIEDZ_SIE_WIECEJ = 'div[class=" col-xs-offset-0 col-xs-12 col-sm-offset-0 col-sm-7 col-md-offset-0 col-md-7 fepColPad fepDefFont fepDefFontTab fepDefFontMob"] p a'
    DZIEKUJEMY_ZE_WYBRALES_SPINGO ='//div[@regioncontrolfield="PF|FKT_FPAY_KOMUNIKAT_GRATULACJE_STANDARD_2"]//div//div//p//p'

    def twoje_zamowienie_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.TWOJE_ZAMOWIENIE_ZOSTALO_OPLACONE)

    def na_podany_field(self):
        return self.wait_for_item_to_be_clickable(By.XPATH, self.NA_PODANY_ADRES_EMAIL)

    def dowiedz_field(self):
        return self.wait_for_item_to_be_clickable(By.XPATH, self.DOWIEDZ_SIE_WIECEJ)

    def dziekujemy_field(self):
        return self.wait_for_item_to_be_clickable(By.XPATH, self.DZIEKUJEMY_ZE_WYBRALES_SPINGO)

    # Funkcje docelowe
    def tresc(self):
        try:
            self.log.info(self.twoje_zamowienie_field())
            self.log.info(self.na_podany_field())
            self.log.info(self.dowiedz_field())
            self.log.info(self.dziekujemy_field())
        except Exception as e:
            self.log.warning('Nie znaleziono tresci')

    def ekran5(self):
        check = Utils().assert_list_item(self.dziekujemy_field, "nie ma za co")
