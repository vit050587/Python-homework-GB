# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

n_str = input("введите строку: ")
word = []
number = 1
el = 0
for el in range(n_str.count(' ') + 1):
    word = n_str.split()
    if len(str(word)) <= 10:
        print(f" {number} {word[el]}")
        number += 1
    else:
        print(f" {number} {word[el][:10]}")
        number += 1

#--------------------------Решение GB----------------------------

string = input('Enter the number with space - ').split()

for n, i in enumerate(string, 1):
    print(n, i) if len(i) <= 10 else print(n, i[:10])

#--------------------------------------------------------------

my_string = input('Введите строку из нескольких слов, разделенных пробелами: ').split()

for i, word in enumerate(my_string, 1):
    print(f'{i}. {word[:10]}')


