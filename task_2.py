sum_numbers = 0
number = 0
numbers = []
while number < 1000:
    if number % 2:
        numbers.append(number ** 3)
    number += 1
print(numbers)
print()

for num in numbers:
    sum_numeral = 0
    result_num = num
    while num != 0:
        sum_numeral += num % 10
        num = num // 10
    if sum_numeral % 7 == 0:
        sum_numbers += result_num

print(f'Сумма чисел из списка, сумма цифр которых делится нацело на 7 = {sum_numbers}')
print()

for num in numbers:
    num += 17
    sum_numeral = 0
    result_num = num
    while num != 0:
        sum_numeral += num % 10
        num = num // 10
    if sum_numeral % 7 == 0:
        sum_numbers += result_num
print(f'Сумма чисел из списка, сумма цифр которых делится нацело на 7, \nно теперь '
      f'каждое число было увеличено на 17 = {sum_numbers}')
