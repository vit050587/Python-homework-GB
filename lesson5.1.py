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


# Не сохраняется форматирование ввода.

#----------------решение GB--------------------------


with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Input new string or empty string to done: ')
        if not line:
            break
        # f.write(f"{line}\n")
        print(line, file=f)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


print('Введите данные для записи в файл \nДля окончания ввода введите пустую строку')
with open('task_1.txt', 'w', encoding='utf-8') as my_file:
    while (line := input()) != '':
        my_file.write(f"{line}\n")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_file = open("text_1.txt", 'w', encoding='utf-8')

line = " "
while line:
    line = input("пишите или не пишите!: ")
    my_file.write(f"{line}\n") if line != '' else my_file.close()
