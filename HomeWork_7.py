#Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json

firms = {}
prof = 0
prof_sum = 0

with open('test7.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        name = line.split()
        profit = int(name[2]) - int(name[3])
        firms.update({name[0]: profit})
        if profit > 0:
            prof += 1
            prof_sum += profit
prof_aver = prof_sum / prof
result = [firms, {'Средняя прибыль': prof_aver}]

with open("result.json", 'w', encoding="utf-8") as file:
    json.dump(result, file)
