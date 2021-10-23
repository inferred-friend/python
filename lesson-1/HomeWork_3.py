#Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
user_number = int(input('Введите любое число '))
number = str(user_number)
result = user_number + int(number*2) + int(number*3)
print(result)