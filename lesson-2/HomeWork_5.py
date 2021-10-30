#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
my_list = [9, 6, 3, 3, 1]
number = int(input("Введите число: "))
a = my_list.count(number)
for element in my_list:
    if a > 0:
        i = my_list.index(number)
        my_list.insert(i+a, number)
        break
    else:
        if number > element:
            y = my_list.index(element)
            my_list.insert(y, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)