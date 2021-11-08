#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def my_info (word1, word2, word3, word4, num1):
    return f"I'am {word1} {word2}, live in {word3}, my email is {word4}, my telephon number is {num1}"

str1 = input('Enter your name: ')
str2 = input('Enter your surname: ')
str3 = input('Enter your town of living: ')
str4 = input('Enter your email: ')
tel_num = input('Enter your telephon number: ')
result = my_info(word1=str1, word2=str2, word3=str3, word4=str4, num1=tel_num)
print(result)
