#Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)


def my_func(i_p, i):
    return i_p * i
print(reduce(my_func, my_list))
