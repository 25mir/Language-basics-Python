def type_logger(func):
    def wrapper(a):
        return f'{a}: {type(a)}'
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
