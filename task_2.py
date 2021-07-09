tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

result = ((tutors[item], klasses[item]) if len(klasses) > item else (tutors[item], None) for item in range(len(tutors)))
print(type(result), *result)
