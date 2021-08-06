class ListNumber:
    @staticmethod
    def check_list(num, nums):
        try:
            int(num)
        except ValueError:
            del nums[-1]
            print("Список должен содержать только числа!")


numbers = list()
while True:
    number = input('Введите число: ')
    if number != 'stop':
        numbers.append(number)
        ListNumber.check_list(number, numbers)
    if number == 'stop':
        break
print(numbers)

