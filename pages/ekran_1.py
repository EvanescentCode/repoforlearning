from Automatyzacja.base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
import logging
from Automatyzacja.utilities.util import Utils
import time


class Ekran1(BaseDriver):

    """
    Klasa ta odpowiada za określenie lokatorów strony 1 w procesie Spingo Standard.
    Następnie wykonuje select na każdym z wyżej wymienionych elementów i je zwraca.
    Następnie są wykonywane na tych elementach różne akcje i funkcję te są następnie
    wywoływane w testcase.
    """

    log = Utils().custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    NR_LOKALU = 'input#ctl00_CPH_Content__V_FKT_FPAY_FIRMA_DANE__Q__ADRES_SIEDZIBY__Q__NR_MIESZKANIA'
    NUMER_TELEFONU = 'input#ctl00_CPH_Content__V_FKT_FPAY_FIRMA_DANE__Q__TELEFON_KOMORKOWY'
    E_MAIL = 'input#ctl00_CPH_Content__V_FKT_FPAY_FIRMA_DANE__Q__EMAIL'
    OSWIADCZENIA_ALL_BUTTON = '//input[@id="ctl00_CPH_UI__V_FKT_FPAY_ZGODA_FIRMY_1__Q__CheckBox"]/..'
    OSWIADCZENIA_REGULAMIN_SPINGO = 'input#ctl00_CPH_UI__V_FKT_FPAY_ZGODA_FIRMY_2__Q__CheckBox'
    OSWIADCZENIA_ZGOD_MARKET_TEL = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__1__ABR____Q__WYBOR__Q__CheckBox'
    OSWIADCZENIA_ZGOD_MARKET_SMS = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__2__ABR____Q__WYBOR__Q__CheckBox'
    OSWIADCZENIA_ZGOD_MARKET_E_MAIL = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__3__ABR____Q__WYBOR__Q__CheckBox'
    OSWIADCZENIA_ZGOD_MARKET_INTERNET = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__4__ABR____Q__WYBOR__Q__CheckBox'
    OSWIADCZENIA_ZGOD_MARKET_ODMOWA = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__5__ABR____Q__WYBOR__Q__CheckBox'
    OSWIADCZENIA_DANE_OSOBOWE_MARKET = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__6__ABR____Q__WYBOR__Q__CheckBox'
    OSWIADCZENIA_DANE_OSOBOWE_TEL = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__7__ABR____Q__WYBOR__Q__CheckBox'
    OSWIADCZENIA_DANE_OSOBOWE_SMS = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__8__ABR____Q__WYBOR__Q__CheckBox'
    OSWIADCZENIA_DANE_OSOBOWE_E_MAIL = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__9__ABR____Q__WYBOR__Q__CheckBox'
    OSWIADCZENIA_DANE_OSOBOWE_INTERNET = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__10__ABR____Q__WYBOR__Q__CheckBox'
    OSWIADCZENIE_UPOWAZNIENIE_NEST = 'input#ctl00_CPH_UI__V_ZGODY_FIRMY_NEW__Q____ABL__12__ABR____Q__WYBOR__Q__CheckBox'
    DALEJ_BUTTON = 'input#ctl00_CPH_nav_DANE_FIRMY_Button2_PP020_NOWY_WNIOSEK_A040_DALEJ'
    INFORMACJA_SMS_OK_BUTTON = 'a#ctl00_CPH_MessageDialog_lbB1'
    KOD_WERYFIKACJI_SMS_INPT = 'input#ctl00_CPH_Content_FKT_FPAY_WPROWADZ_PIN'
    KOD_WERYFIKACJI_SMS_POTWIERDZ = 'input#ctl00_CPH_nav_DANE_FIRMY_Button4_PP020_NOWY_WNIOSEK_A040_POTWIERDZ_PIN'
    APPNUM = 'input#ctl00_CPH_appnum'

    # Wywołanie locatora
    def numer_lokalu_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.NR_LOKALU)
    
    def numer_telefonu_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.NUMER_TELEFONU)
    
    def e_mail_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.E_MAIL)
    
    def oswiadczenia_all_button_field(self):
        return self.wait_for_item_to_be_clickable(By.XPATH, self.OSWIADCZENIA_ALL_BUTTON)
    
    def oswiadczenia_regulamin_spingo_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_REGULAMIN_SPINGO)
    
    def oswiadczenia_zgod_market_tel_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_ZGOD_MARKET_TEL)
    
    def oswiadczenia_zgod_market_sms_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_ZGOD_MARKET_SMS)
    
    def oswiadczenia_zgod_market_e_mail_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_ZGOD_MARKET_E_MAIL)
    
    def oswiadczenia_zgod_market_internet_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_ZGOD_MARKET_INTERNET)
    
    def oswiadczenia_zgod_market_odmowa_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_ZGOD_MARKET_ODMOWA)
    
    def oswiadczenia_dane_osobowe_market_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_DANE_OSOBOWE_MARKET)
    
    def oswiadczenia_dane_osobowe_tel_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_DANE_OSOBOWE_TEL)
    
    def oswiadczenia_dane_osobowe_sms_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_DANE_OSOBOWE_SMS)
    
    def oswiadczenia_dane_osobowe_e_mail_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_DANE_OSOBOWE_E_MAIL)
    
    def oswiadczenia_dane_osobowe_internet_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIA_DANE_OSOBOWE_INTERNET)
    
    def oswiadczenia_upowaznienie_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.OSWIADCZENIE_UPOWAZNIENIE_NEST)

    def dalej_button_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.DALEJ_BUTTON)

    def informacja_sms_ok_button_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.INFORMACJA_SMS_OK_BUTTON)
    
    def kod_weryfikacji_sms_inpt_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.KOD_WERYFIKACJI_SMS_INPT)
    
    def kod_weryfikacji_sms_potwierdz_field(self):
        return self.wait_for_item_to_be_clickable(By.CSS_SELECTOR, self.KOD_WERYFIKACJI_SMS_POTWIERDZ)

    def appnum_field(self):
        list_appnum_field = self.wait_for_appearance(By.CSS_SELECTOR, self.APPNUM)
        return list_appnum_field

    # Funkcje docelowe
    def numer_lokalu(self, numer_lokalu):
        self.log.info("Numer lokalu: " + numer_lokalu)
        self.numer_lokalu_field().send_keys(numer_lokalu)
    
    def numer_telefonu(self, numer_telefonu):
        self.log.info("Numer telefonu: " + numer_telefonu)
        self.numer_telefonu_field().send_keys(numer_telefonu)
    
    def e_mail(self, e_mail):
        self.e_mail_field().clear()
        self.log.info("E-mail: " + e_mail)
        self.e_mail_field().send_keys(e_mail)
    
    def oswiadczenia_all_button(self):
        self.oswiadczenia_all_button_field().click()
    
    def oswiadczenia_regulamin_spingo(self):
        self.oswiadczenia_regulamin_spingo_field().click()
    
    def oswiadczenia_zgod_market_tel(self):
        self.oswiadczenia_zgod_market_tel_field().click()
    
    def oswiadczenia_zgod_market_sms(self):
        self.oswiadczenia_zgod_market_sms_field().click()
    
    def oswiadczenia_zgod_market_e_mail(self):
        self.oswiadczenia_zgod_market_e_mail_field().click()
    
    def oswiadczenia_zgod_market_internet(self):
        self.oswiadczenia_zgod_market_internet_field().click()
    
    def oswiadczenia_zgod_market_odmowa(self):
        self.oswiadczenia_zgod_market_odmowa_field().click()
    
    def oswiadczenia_dane_osobowe_market(self):
        self.oswiadczenia_dane_osobowe_market_field().click()
    
    def oswiadczenia_dane_osobowe_tel(self):
        self.oswiadczenia_dane_osobowe_tel_field().click()
    
    def oswiadczenia_dane_osobowe_sms(self):
        self.oswiadczenia_dane_osobowe_sms_field().click()
    
    def oswiadczenia_dane_osobowe_e_mail(self):
        self.oswiadczenia_dane_osobowe_e_mail_field().click()
    
    def oswiadczenia_dane_osobowe_internet(self):
        self.oswiadczenia_dane_osobowe_internet_field().click()
    
    def oswiadczenia_upowaznienie(self):
        self.oswiadczenia_upowaznienie_field().click()

    def click_dalej_button(self):
        self.dalej_button_field().click()

    def informacja_sms_ok_button(self):
        self.informacja_sms_ok_button_field().click()

    def kod_weryfikacji_sms_inpt(self, sms_inpt):
        self.log.info('Kod weryfikacji SMS inpt: ' + sms_inpt)
        self.kod_weryfikacji_sms_inpt_field().send_keys(sms_inpt)
    
    def kod_weryfikacji_sms_potwierdz(self):
        self.kod_weryfikacji_sms_potwierdz_field().click()

    def appnum(self):
        for item in self.appnum_field():
            items_value = item.get_attribute('value')
            self.log.info('FKT NUMBER: ' + items_value)

    def ekran1(self, numer_lokalu, numer_telefonu, e_mail, sms_inpt):
        self.numer_lokalu(numer_lokalu)
        self.numer_telefonu(numer_telefonu)
        self.e_mail(e_mail)
        self.oswiadczenia_all_button()
        self.appnum()
        time.sleep(5)
        self.click_dalej_button()
        self.informacja_sms_ok_button()
        self.kod_weryfikacji_sms_inpt(sms_inpt)
        self.kod_weryfikacji_sms_potwierdz()