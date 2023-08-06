import random
import calendar
import re
import time 

class PeselGen:

    """
    Pesel generator został zbudowany, tak żeby generowany pesel przechodził wszystkie walidacje.
    Generator ten na początku roku 2024 powinien zostać zaaktualizowany w funkcjach generate_pesel
    user_question.
    """

    def __init__(self):
        self.gender = self.user_question1()
        self.b_date = self.user_question2()

    def generate_pesel(self, birth_date, gender):
        year = birth_date[0:2]
        month = birth_date[2:4]
        day = birth_date[4:6]
        year = int(year)
        month = int(month)
        # Pesel generator will be up-to-date up to 2024 year.
        if year <= 23:
            month += 20
        year = str(year).zfill(2)
        month = str(month).zfill(2)
        # serial number
        serial = str(random.randint(0, 999)).zfill(3)
        # gender number
        gender_number = self.get_gender_number(gender)
        # control digit last number
        control_digit = self.calculate_control_digit(day, month, year, serial, gender_number)
        # Adding all pesel stuff
        pesel = year + month + day + serial + str(gender_number) + str(control_digit)
        return pesel

    def get_gender_number(self, gender):
        if gender == "M":
            return random.choice([1, 3, 5, 7, 9])
        if gender == "K":
            return random.choice([0, 2, 4, 6, 8])

    def calculate_control_digit(self, day, month, year, serial, gender_number):
        weight_factors = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        pesel_without_control_digit = day + month + year + serial + str(gender_number)
        pesel_without_control_digit = [char for char in pesel_without_control_digit if char.isdigit()]
        control_sum = 0
        for i in range(0, 10):
            control_sum += int(pesel_without_control_digit[i]) * weight_factors[i]
        control_digit = (10 - (control_sum % 10)) % 10
        return control_digit

    def user_question1(self):
        randomize = random.randint(1, 2)
        if randomize == 1:
            answer = 'K'
        else:
             answer = 'M'
        return answer

    def user_question2(self):
        roll_the_dice = random.randint(1, 2)
        if roll_the_dice == 1:
            year = random.randint(0, 5)
        else:
            year = random.randint(58, 99)
        month = random.randint(1, 12)
        if year <= 23:
            days_in_month = calendar.monthrange(2000 + year, month)[1]
        else:
            days_in_month = calendar.monthrange(1900 + year, month)[1]
        day = random.randint(1, days_in_month)
        birth_date = f"{year:02d}{month:02d}{day:02d}"
        return birth_date

    def pesel(self):
        pesel = self.generate_pesel(self.b_date, self.gender)
        return pesel

