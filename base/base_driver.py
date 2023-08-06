import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class BaseDriver:
    """
    BaseDriver jest klasą która dostarcza wszystkie funckje obsługi automatyzacji, która zawiera driver.
    Zawiera ona takie funkcje jak:
    scroll: scrolluje do końca strony.
    page_back: powraca do poprzedniej strony.
    Funkcje wait: które odpowiedzialne są za obsługę szukania elementów, tak aby miały na to odpowiedni czas i warunek.
    Funkcje bez wait: które odpowiedzialne są za obsługę szukania elementów, bez określenia czasu.
    """
    def __init__(self, driver):
        self.driver = driver

    def scroll(self):
        page_length = self.driver.execute.script(
            "window.scrollTo(0, document.body.scrollHeight); var pageLength=document.body.scrollHeight; return page_lenght"
        )
        match = False
        while (match == False):
            last_count = page_length
            time.sleep(2)
            lenght_of_page = self.driver.execute.script(
                "window.scrollTo(0, document.body.scrollHeight); var pageLength=document.body.scrollHeight; return page_lenght"
            )

        time.sleep(3)

    def page_back(self, amount=None):
        amount = amount if amount else 1
        for am in range(amount):
            self.driver.back()

    def wait_for_appearance(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return element

    def wait_for_item_to_be_selected(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_selected((locator_type, locator)))
        return element

    def wait_for_item_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_for_presence_of_all_elements_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def long_wait_for_item_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def select_item(self, locator_type, locator):
        element = self.driver.find_element((locator_type, locator))
        return element

    def visibility_of_item(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element
