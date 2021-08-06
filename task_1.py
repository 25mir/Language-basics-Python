import re


class Date:
    def __init__(self, time):
        self.time = time

    def __str__(self):
        return f'Hellow'

    @classmethod
    def method_int(cls, time):
        result = list()
        for el in re.split(r'\.', time):
            result.append(int(el))
        Date.valid(time, result[0], result[1], result[2])

    @staticmethod
    def valid(time, day, month, year):
        if day > 31 or day <= 0:
            print('Некорректно указан день')
        elif month > 12 or month <= 0:
            print('Некорректно указан месяц')
        elif year > 2021 or year <= 0:
            print('Некорректно указан год')
        else:
            print(time)


date = Date('10.08.2021')
date.method_int(date.time)
