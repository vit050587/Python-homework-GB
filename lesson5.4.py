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

#---------------------решение GB--------------------------------

rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_44.txt", "w", encoding='utf-8') as new_file:
    with open("text_4.txt", encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])


#  ------------------------------------------- вариант решения ---------------------------------------------------------
# pip install googletrans==3.1.0a0
# обновление до альфа-версии

from googletrans import Translator

with open("text_4_translate.txt", 'w', encoding='utf-8') as f:
    with open("text_4.txt", 'r', encoding='utf-8') as f1:
        text = f1.read()
    try:
        f.write(Translator().translate(text, dest='ru').text)
    except AttributeError:
        print("DDoS-атака на Google не прошла, продолжаем попытки!")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


import requests
import json

"""Переводит с английского на русский файл, результат записывается в новый файл.
Должен быть установлен модуль requests.
"""
token = "trnsl.1.1.20200416T132512Z.0bdb58c00f70557b.b1aec4ed1dc72e76cc6c08980f7ed0c2de92ae86"
url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

with open("task_4_text_yandex.txt", "w", encoding="utf-8") as f_result:
    with open("text_4.txt", encoding="utf-8") as f_4:
        for line in f_4:
            eng_text = line
            trans_option = {'key': token, 'lang': 'en-ru', 'text': eng_text}
            webRequest = requests.get(url_trans, params=trans_option)
            trans_dict = json.loads(webRequest.text)
            line_to_result = "".join(trans_dict["text"])
            f_result.write(line_to_result)

print(f"Text translate from {f_4.name} has been done in {f_result.name}")
