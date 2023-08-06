from Automatyzacja.base.base_driver import BaseDriver
from Automatyzacja.utilities.util import Utils
from selenium.webdriver.common.by import By
import logging


class Ekran2(BaseDriver):

    """
    Klasa ta odpowiada za określenie lokatorów strony 2 w procesie Spingo Standard.
    Następnie wykonuje select na każdym z wyżej wymienionych elementów i je zwraca.
    Następnie są wykonywane na tych elementach różne akcje i funkcję te są następnie
    wywoływane w testcase.
    """

    log = Utils().custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    PESEL = 'input#ctl00_CPH_Content__V_FKT_FPAY_KLIENT_DANE_UZUPELNIAJACE__Q__PESEL'
    RODZAJ_DOKUMENTU_TOZ_BTN = 'button[data-id=ctl00_CPH_Content__V_FKT_FPAY_KLIENT_DANE_UZUPELNIAJACE__Q__RODZAJ_DOKUMENTU_TOZSAMOSCI]'
    DROPDOWN_MENU = 'ul[class="dropdown-menu inner"] li[data-original-index="1"]'
    NUMER_DOKUMENTU_TOZ = 'input#ctl00_CPH_Content__V_FKT_FPAY_KLIENT_DANE_UZUPELNIAJACE__Q__NUMER_DOKUMENTU_TOZSAMOSCI'
    OSWIADCZENIA_ALL_BUTTON = '//input[@id="ctl00_CPH_UI__V_FKT_FPAY_KLIENT_DANE_UZUPELNIAJACE__Q__ZGODA_5__Q__CheckBox"]/..'
    OSWIADCZENIA_POTWIERDZENIE_DANYCH = 'input#ctl00_CPH_UI__V_FKT_FPAY_KLIENT_DANE_UZUPELNIAJACE__Q__ZGODA_1__Q__CheckBox'
    OSWIADCZENIA_UPOWAZNIENIE_FAKTORIA = 'input#ctl00_CPH_UI__V_FKT_FPAY_KLIENT_DANE_UZUPELNIAJACE__Q__ZGODA_2__Q__CheckBox'
    OSWIADCZENIA_POWIAZANIA_KAPIT = 'input#ctl00_CPH_UI__V_FKT_FPAY_KLIENT_DANE_UZUPELNIAJACE__Q__ZGODA_3__Q__CheckBox'
    OSWIADCZENIA_PEP = 'input#ctl00_CPH_UI__V_FKT_FPAY_KLIENT_DANE_UZUPELNIAJACE__Q__ZGODA_4__Q__CheckBox'
    DALEJ_BUTTON_FIELD = 'input#ctl00_CPH_nav_DANE_UZUPELNIAJACE_IDG_Button1_PP020_NOWY_WNIOSEK_A060_DALEJ'
    KOD_WERYFIKACJI_SMS_INPT = 'input#ctl00_CPH_Content_FKT_FPAY_WPROWADZ_PIN_UZUPELNIAJACE'
    KOD_WERYFIKACJI_SMS_POTWIERDZ_BTN = 'input#ctl00_CPH_nav_DANE_UZUPELNIAJACE_IDG_Button3_PP020_NOWY_WNIOSEK_A060_POTWIERDZ_PIN'
    INFORMACJA_OK = 'a[class="ToolButtonS fepDialogInfo"]'

    # Funkcje
    def pesel_inpt_field(self):
        return self.long_wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.PESEL)
    
    def rodzaj_dokumentu_toz_btn_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.RODZAJ_DOKUMENTU_TOZ_BTN)

    def dropdown_menu_field(self):
        return self.visibility_of_item(By.CSS_SELECTOR, self.DROPDOWN_MENU)

    def numer_dokumentu_toz_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.NUMER_DOKUMENTU_TOZ)

    def dalej_button_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.DALEJ_BUTTON_FIELD)

    def oswiadczenia_all_button_field(self):
        return self.wait_for_item_to_be_clickable(By.XPATH, self.OSWIADCZENIA_ALL_BUTTON)
    
    def oswiadczenia_potwierdzenie_danych_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_POTWIERDZENIE_DANYCH)
    
    def oswiadczenia_upowaznienie_faktoria_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_UPOWAZNIENIE_FAKTORIA)
    
    def oswiadczenia_powiazania_kapit_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_POWIAZANIA_KAPIT)
    
    def oswiadczenia_pep_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_PEP)
    
    def kod_weryfikacji_sms_inpt_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.KOD_WERYFIKACJI_SMS_INPT)
    
    def kod_weryfikacji_sms_potwierdz_btn_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.KOD_WERYFIKACJI_SMS_POTWIERDZ_BTN)

    def informacja_ok_button_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.INFORMACJA_OK)

    # Funkcje docelowe
    def pesel_inpt(self, pesel):
        self.log.info('Pesel: ' + pesel)
        self.pesel_inpt_field().send_keys(pesel)
    
    def rodzaj_dokumentu_toz_btn(self):
        self.rodzaj_dokumentu_toz_btn_field().click()

    def dropdown_menu(self):
        self.dropdown_menu_field().click()
        
    def numer_dokumentu_toz(self, numer_dokumentu):
        self.log.info('Numer Dokumentu: ' + numer_dokumentu)
        self.numer_dokumentu_toz_field().send_keys(numer_dokumentu)
    
    def oswiadczenia_all_button(self):
        self.oswiadczenia_all_button_field().click()
    
    def oswiadczenia_potwierdzenie_danych(self):
        self.oswiadczenia_potwierdzenie_danych_field().click()
    
    def oswiadczenia_upowaznienie_faktoria(self):
        self.oswiadczenia_upowaznienie_faktoria_field().click()
    
    def oswiadczenia_powiazania_kapit(self):
        self.oswiadczenia_powiazania_kapit_field().click()
    
    def oswiadczenia_pep(self):
        self.oswiadczenia_pep_field().click()
    
    def kod_weryfikacji_sms_inpt(self, sms_inpt):
        self.log.info('SMS INPUT: ' + sms_inpt)
        self.kod_weryfikacji_sms_inpt_field().send_keys(sms_inpt)
    
    def kod_weryfikacji_sms_potwierdz_btn(self):
        self.kod_weryfikacji_sms_potwierdz_btn_field().click()

    def click_dalej_button(self):
        self.dalej_button_field().click()

    def informacja_ok_button(self):
        self.informacja_ok_button_field().click()
        
    def ekran2(self, pesel, numer_dokumentu, sms_inpt):
        self.pesel_inpt(pesel)
        self.rodzaj_dokumentu_toz_btn()
        self.dropdown_menu()
        self.numer_dokumentu_toz(numer_dokumentu)
        self.oswiadczenia_all_button()
        self.click_dalej_button()
        self.informacja_ok_button()
        self.kod_weryfikacji_sms_inpt(sms_inpt)
        self.kod_weryfikacji_sms_potwierdz_btn()