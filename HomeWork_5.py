#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('test5.txt', 'w+') as file:
            line = input('Введите цифры через пробел: \n')
            file.writelines(line)
            my_nums = line.split()
            print(sum(map(int, my_nums)))
    except ValueError:
        print('Введены неправильные данные')


summary()
