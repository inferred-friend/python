#Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list1 = input('Ввведите несколько переменных: ').split()
my_list1[:-1:2], my_list1[1::2] = my_list1[1::2], my_list1[:-1:2]
print(my_list1)