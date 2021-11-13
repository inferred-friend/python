#Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

my_list = [3, 18, 0, 44, 5, 5, 2, 8, 123, 1, 65, 33, 1567]
result = [number for i, number in enumerate(my_list) if i > 0 and my_list[i] > my_list[i - 1]]
print(result)
