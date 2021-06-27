forecast = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_forecast = []
for item in forecast:
    number = ''
    diff1 = ''
    diff2 = ''
    for s in item:
        if s in '1234567890':
            number += s
        else:
            if number:
                diff2 += s
            else:
                diff1 += s
    if not number:
        new_forecast.append(item)
        continue
    number = f'{diff1}{int(number):02d}{diff2}'
    new_forecast.append('"')
    new_forecast.append(number)
    new_forecast.append('"')
print(new_forecast)
result = ' '.join(new_forecast)
print(result)
