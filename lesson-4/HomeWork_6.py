#Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,

def generator1():
    a = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(a), 10):
        print(i)


generator1()

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.


def generator2():
    my_list = [5, 'Hello', 76, 3.49]

    from itertools import islice
    from itertools import cycle

    for x in islice(cycle(my_list), 10):
        print(x)


generator2()
