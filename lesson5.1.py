# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

func = open('test.txt', 'w')
str_text = input('Введите текст: \n')
while str_text:
    func.writelines(str_text)
    str_text = input('Введите текст: \n')
    if not str_text:
        break

func.close()
func = open('test.txt', 'r')
content = func.readlines()
print(content)
func.close()
