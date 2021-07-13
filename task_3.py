import csv


my_dict = dict()
with open('users.csv', 'r', encoding='utf-8') as f_1:
    reader_f1 = tuple(csv.reader(f_1))
    with open('hobby.csv', 'r', encoding='utf-8') as f_2:
        reader_f2 = tuple(csv.reader(f_2))
        for user, hobby in zip(reader_f1, reader_f2):
            my_dict.setdefault(" ".join(user), ",".join(hobby))

print(my_dict)
