class DivisionByZero:
    @staticmethod
    def divide(a, b):
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Вы не можете делить на ноль!")


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
DivisionByZero.divide(num1, num2)
