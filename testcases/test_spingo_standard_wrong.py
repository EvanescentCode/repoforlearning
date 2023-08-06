import pytest
import logging
from Automatyzacja.pages.ekran_0 import LaunchPage
from Automatyzacja.pages.ekran_1 import Ekran1
from Automatyzacja.pages.ekran_2 import Ekran2
from Automatyzacja.pages.ekran_3 import Ekran3
from Automatyzacja.pages.ekran_4 import Ekran4
from Automatyzacja.pages.ekran_5 import Ekran5
from Automatyzacja.generators.psel_gen import PeselGen
from Automatyzacja.generators.dok_toz_gen import GeneratorDokToz
from Automatyzacja.generators.nr_tel_gen import NumerTelefonu
from Automatyzacja.test_data.data_driven_handler import DDT
from Automatyzacja.utilities.util import Utils
import time
import softest
from ddt import ddt, data, unpack


@ddt
@pytest.mark.usefixtures("setup")
class TestSpingo(softest.TestCase):
    """
    Tutaj biznesowa część testów, znajdują się tu odwołania do klas oraz funkcji w folderze Automatyzacja
    Funkcja test_spingo_smoke przyjmuje argumenty nip_data, col2, col3, col4
    col2, col3, col4 są traktowane jako placeholder z takiego powodu, że @unpack dopisuje wartości w liczbie
    równej do liczby argumentów, po czym jak dojdzie do końca to, zapętla.
    """

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.u = Utils()
        self.e0 = LaunchPage(self.driver)
        self.e1 = Ekran1(self.driver)
        self.e2 = Ekran2(self.driver)
        self.e3 = Ekran3(self.driver)
        self.e4 = Ekran4(self.driver)
        self.e5 = Ekran5(self.driver)
        self.log = Utils().custom_logger(log_level=logging.DEBUG)

    @data(*DDT(filename='../test_data/data_driven.xlsx', sheet_name='Sheet1', number_of_tests=1).process_handler())
    @unpack
    def test_spingo_smoke(self, nip_data, col2, col3, col4):  # (col2 = status, col3 = numer PKD col4 = Czy użyte)
        # Ekran 0
        self.e0.ekran0(nip=nip_data)
        # Ekran 1
        random_numer_telefonu = NumerTelefonu()
        self.e1.ekran1(numer_lokalu='3', numer_telefonu=random_numer_telefonu.numer_telefonu(),
                       e_mail='konrad.sledziewski@faktoria.pl', sms_inpt='64666')
        # Ekran 2
        gen_nr_toz = GeneratorDokToz()
        pesel_gen = PeselGen()
        self.e2.ekran2(pesel=str(pesel_gen.pesel()), numer_dokumentu=gen_nr_toz.generuj_numer_dowodu(),
                       sms_inpt='6666')
        # Ekran 3
        self.e3 = Ekran3(self.driver)
        self.e3.ekran3(sms_inpt='6666')
        # Ekran 4
        self.e4.ekran4()
        # Koniec
        time.sleep(5)
        # Ekran 5
