# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
text = []
with open('file_2.txt', 'r') as file_en:
    # content = file_en.read().split('\n')
    for i in file_en:
        i = i.split(' ', 1)
        text.append(dict_num[i[0]] + '  ' + i[1])
    print(text)

with open('file_3.txt', 'w') as file_rus:
    file_rus.writelines(text)
