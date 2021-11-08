#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def sum_max_num (num1, num2, num3):
    return f'Сумма двух максимальных чисел равна: {num1 + num2 + num3 - min([num1, num2, num3])}'

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
result = sum_max_num(num1, num2, num3)
print(result)
