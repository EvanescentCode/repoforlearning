import requests
import json
import random


class SendRequest:
    """
    Klasa odpowiadająca za wysyłanie zapytania do API i uzyskiwania odpowiedzi.
    Funkcje get_applicationNumber oraz get_fieldInfos zwracają kolejno FKT number, oraz URL
    z Request.
    """
    def __init__(self, url=None, numer=None):
        self.url = url
        self.numer = numer
        self.send_request()

    def headers(self):
        headers = {
            "Ocp-Apim-Subscription-Key": "",
            "Content-Type": "application/json"
        }
        return headers

    def default_url(self):
        url = ''
        return url

    def post_request(self):
        data = self.data_to_request()
        json_data = json.dumps(data)
        response = requests.post(self.url, data=json_data, headers=self.headers(), verify=False)
        return response

    def data_to_request(self):
        data = {
            "contractId": "FKT176898743",
            "merchantId": "5423225335",
            "brokerId": "",
            "transactionId": "",
            "currency": "PLN",
            "amount": 6000,
            "buyerId": "",
            "urlNotify": "https://webhook.site/79b46fc2-f2cd-4c36-9640-e1fda62523e3",
            "toSendNotify": True,
            "urlCancel": "https://faktoria.pl",
            "urlReturn": "https://spingo.pl",
            "maxAppTime": 60,
            "ip": "255.255.255.255",
            "orderId": "12345123451234512345",
            "splitPayment": False,
            "vatAmount": 112.2,
            "vatAmountPln": 112.2
        }
        cyfry = random.randint(10000, 99999)
        self.numer = f"FV/{cyfry}/20"
        data["transactionId"] = self.numer
        return data

    def extract_data(self, data):
        applicationNumber = data['applicationNumber']
        fieldInfos = data['fieldInfos'][0].split(',')[0]
        return applicationNumber, fieldInfos

    def send_request(self):
        if self.url is None:
            self.url = self.default_url()
        response = self.post_request()
        response_data = response.json()
        if isinstance(response_data, dict):
            self.applicationNumber, self.fieldInfos = self.extract_data(response_data)

    def get_fieldinfos(self):
        return self.fieldInfos

    def get_applicationNumber(self):
        return self.applicationNumber
