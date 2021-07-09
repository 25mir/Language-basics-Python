src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

my_dict = {}
for i in src:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print([el for el in src if my_dict[el] == 1])
