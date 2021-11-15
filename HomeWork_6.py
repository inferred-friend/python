#Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.


def sum_hour():
    try:
        my_dict = {}
        with open("test6.txt", encoding='utf-8') as file:
            for line in file:
                name, hours = line.split(':')
                summ = sum(map(int, ''.join([i for i in hours if i == ' ' or ('0' <= i <= '9')]).split()))
                my_dict[name] = summ
            print(f"{my_dict}")
    except FileNotFoundError:
        return 'Файл не найден.'


sum_hour()
