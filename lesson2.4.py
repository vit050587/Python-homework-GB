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
        print(f" {number} {word[el][0:9]}")
        number += 1
