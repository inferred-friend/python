#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_func_division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'You cannot divide by zero. Enter another number'

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
result = my_func_division(num1, num2)
print(result)
