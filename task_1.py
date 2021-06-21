duration = int(input('Укажите время в секундах: '))
minute = 60
hour = 3600

if duration <= hour:
    print(f'{duration} сек = {duration // minute} мин {duration % minute} сек')
else:
    print('Максимальный промежуток времени до часа')
