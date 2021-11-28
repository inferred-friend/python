#Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyError:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                value = int(input('Введите число и нажмите Enter (для завершения программы введите любой символ): '))
                self.my_list.append(value)
                print(f'Текущий список - {self.my_list} \n ')

            except:
                print(f"Недопустимое значение")
                a = input(f'Хотите попробовать еще раз? Y/N ')
                if a == 'Y' or a == 'y':
                    print(try_except.my_input())
                elif a == 'N' or a == 'n':
                    return f'Программа закончена'
                else:
                    break


try_except = MyError(1)
print(try_except.my_input())
