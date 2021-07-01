def num_translate_adv(key):
    for val in numbers.values():
        if key == val:
            return val
        else:
            return numbers.get(key)


numbers = {'one': 'один', 'two': 'два',
           'three': 'три', 'four': 'четыре',
           'five': 'пять', 'six': 'шесть',
           'seven': 'семь', 'eight': 'восемь',
           'nine': 'девять', 'ten': 'десять'}
print(num_translate_adv(input('Please enter a number between 0 and 10: ')))
