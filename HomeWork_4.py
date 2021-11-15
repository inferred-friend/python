#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('test4.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

with open('test4.1.txt', 'w', encoding="utf-8") as file_2:
    for line in lines:
        i = line.split()
        i[0] = translation[i[0]]
        print(' '.join(i), file=file_2)
