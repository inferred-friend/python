#Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_file = open('test2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
str_line = 0
for i, line in enumerate(content):
    str_line += 1
    word = len(line.split())
    print(f'Количество слов в {i + 1} строке {word}')
