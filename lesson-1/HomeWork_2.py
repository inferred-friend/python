#Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
user_number = int(input('Введите секунды: '))
hour = ((user_number//3600))%24
minutes = (user_number//60)%60
second = user_number%60
result = f'На часах {hour:01}:{minutes:01}:{second:01}'
print(result)