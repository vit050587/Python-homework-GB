# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open('file.txt', 'r')
content = file.read()
print(f'Содержимое файла: \n {content}')
file = open('file.txt', 'r')
content = file.readlines()
print(f'Количество строк в файле - {len(content)}')
file = open('file.txt', 'r')
content = file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} строки {len(content[i])}')
file = open('file.txt', 'r')
content = file.read()
content = content.split()
print(f'Количество слов в строках - {len(content)}')
file.close()