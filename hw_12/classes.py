from collections import UserDict
import datetime
import re
import copy

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
        self.value = value


class Phone(Field):
    def __init__(self, value):
        self.value = value
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, new_value):
        new_value = re.sub(r'[^\d]', '', new_value)
        if len(new_value) > 6:
            self.__value = new_value

        else:
            print('Phone number so short')
            self.__value = None


class Birthday(Field):
    def __init__(self, value):
        self.value = value
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, new_value):
        numbers_date = re.findall(r'\d+', str(new_value))
        if len(numbers_date) != 3:
            self.__value = None
        numbers_date = tuple(map(int, numbers_date))
        try:
            date_birthday = datetime.datetime(*numbers_date).date()
            if date_birthday >= datetime.datetime.today().date():
                print('Date from future')
                self.__value = None
                return
            self.__value = date_birthday
        except:
            print('Date is wrong')
            self.__value = None


class Record():
    def __init__(self, name, phone='', birthday=Birthday(None)):
        self.name = name
        self.phones = [phone]
        self.birthday = birthday
    def __str__(self):
        result = ''
        result += f"name - {self.name.value} "
        if self.birthday:
            result += f"birthday - {str(self.birthday.value)} "
        result += f"phones - {', '.join([phone.value for phone in self.phones])}"
        return result
    def add_phone(self, phone):
        self.phones.append(phone)
    def change_phone(self, phone, new_phone):
        for i, el in enumerate(self.phones):
            if phone.value == el.value:
                self.phones[i] = new_phone
                break
        else:
            raise Exception("Phone is not found")
    def change_birthday(self,  new_birthday):
        if new_birthday.value != None:
            self.birthday = new_birthday
        else:
            raise Exception("New birthday is not correct")
    def days_to_birthday(self):
        now = datetime.datetime.today().date()
        if (self.birthday.value.day, self.birthday.value.month) == (29, 2):
            bd = self.birthday.value + datetime.timedelta(days=1)
        else:
            bd = self.birthday.value
        bd_that_year = bd.replace(year=now.year)
        delta = bd_that_year - now
        if delta.days <= 0:
            bd_that_year = bd_that_year.replace(year=now.year+1)
            delta = bd_that_year - now
        if (self.birthday.value.day, self.birthday.value.month) == (29, 2):
            return delta.days - 1
        return delta.days


class AddressBook(UserDict):
    def __getstate__(self):
        atr = copy.deepcopy(self.__dict__)
        return atr
    def __setstate__(self, atr):
        self.__dict__ = atr
    def add_record(self, record):
        self[record.name.value] = record
    def full_search(self, user_or_phone):
        result = ''
        for rec in self.data.values():
            if user_or_phone in rec.name.value:
                result += '\n' + str(rec)
            dig_user_or_phone = re.sub(r'[\D]', '', user_or_phone)
            if len(dig_user_or_phone) > 3:
                for phone in rec.phones:
                    if dig_user_or_phone in phone.value:
                        result += '\n' + str(rec)
        return result
    def iterator(self, N):
        self.N = N
        self.i = 0
        new_iter = self
        while self.i < len(self.data):
            x = next(new_iter)
            lst = []
            for name, rec in x.items():
                lst.append(
                    f'{rec.name.value} : bd - {rec.birthday.value}, phone - {", ".join([phone.value for phone in rec.phones])}')
            yield '\n'.join(lst)
    def __next__(self):
        if self.i >= len(self):
            raise StopIteration
        lst_items = list(self.data.items())
        cuter_items = dict(lst_items[self.i: self.i + self.N])
        self.i += self.N
        return cuter_items
    def __iter__(self, N=1):
        self.i = 0
        return self

   
if __name__ == "__main__":
    pass
