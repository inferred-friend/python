#Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
number_1 = int(input('Введите размер выручки в рублях: '))
number_2 = int(input('Введите размер издержек в рублях: '))

if number_2 > number_1:
    print('Ваша фирма работает в убыток')
if number_2 < number_1:
    print('Ваша фирма работает с прибылью')
    r = (number_1 - number_2) / number_1
    print(f'Рентабельность: r')
    p = int(input('Сколько человек работает в Вашей фирме: '))
    s = (number_1 - number_2) / p
    print('Прибыль на одного человека составляет: ', s, 'рублей')

