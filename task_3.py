number = 0
while number != 20:
    number += 1
    if number == 1:
        print(f'{number} процент')
    elif number > 1 and number < 5:
        print(f'{number} процент' + 'а')
    else:
        print(f'{number} процент' + 'ов')

print('================================================')


number = int(input('Введите число до 20: '))
if number == 1:
    print(f'{number} процент')
elif number > 1 and number < 5:
    print(f'{number} процент' + 'а')
elif number <= 20:
    print(f'{number} процент' + 'ов')
else:
    print('Введите число до 20.')
