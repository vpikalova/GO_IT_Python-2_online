from collections import UserDict
import datetime
import re

pattern_phone = '\d{3,}'


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):

    def __init__(self, value):
        self.__value = 0
        self.value = value


class Phone(Field):

    def __init__(self, value):
        self.__value = 0
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):

        if re.fullmatch(pattern_phone, new_value):
            self.__value = new_value

        else:
            print('Phone number is wrong')
            self.__value = None


class Birthday(Field):

    def __init__(self, value):
        self.__value = 0
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):

        try:
            date_birthday = datetime.datetime.strptime(
                new_value, "%Y-%m-%d").date()

            
            if date_birthday >= datetime.datetime.today().date():
                print('Date from future')
                self.__value = None
                return
          
            self.__value = date_birthday

        except:
            print('Date is not correct')
            self.__value = None


class AddressBook(UserDict):

    def add_record(self, record):
        self[record.name.value] = record

    def iterator(self, n):
        lst_tpl_data = list(self.data.items())

        while lst_tpl_data:
            result = '\n'.join(
                [f'{k} - {v.phones}' for k, v in lst_tpl_data[:n]])
            yield result
            lst_tpl_data = lst_tpl_data[n:]
            print(lst_tpl_data )


class Record():

    def __init__(self, name, phone=[], birthday=None):
        self.name = name
        self.phones = [phone]
        self.birthday = birthday

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, phone):
        pass

    def days_to_birthday(self):
        now = datetime.datetime.today().date()

        bd = self.birthday.value


        bd_that_year = bd.replace(year=now.year)

        delta = bd_that_year - now

        if delta.days <= 0:

            bd_that_year = bd_that_year.replace(year=now.year+1)
   
            delta = bd_that_year - now

        return delta.days


