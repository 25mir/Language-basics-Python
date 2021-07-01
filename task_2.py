def thesaurus(*args):
    staff = dict()
    for name in args:
        key = name[0]
        if key not in staff:
            staff[key] = []
        staff[key].append(name)
    return staff


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
