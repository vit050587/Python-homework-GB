# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def subjects_func():
    try:
        my_dict = {}
        with open("file_6.txt", encoding='utf-8') as file_subject:
            for line in file_subject:
                subject, lessons = line.split(':')
                lessons_sum = sum(map(int, ''.join(
                    [i for i in lessons if i == ' ' or ('0' <= i <= '9')]).split()))
                my_dict[subject] = lessons_sum
            print(f"{my_dict}")
    except FileNotFoundError:
        return 'Err!!!'


subjects_func()

#-------------------------решение GB------------------------------------

mydict = {}
with open("text_6.txt", encoding="utf-8") as fobj:
    for line in fobj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        mydict[name] = name_sum
print(f"{mydict}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


with open('text_6.txt', 'r', encoding='utf8') as text_file:
    a = text_file.readlines()
    for s in a:
        new_str = ''.join((i if i in '1234567890' else ' ') for i in s)
        new_2 = [int(i) for i in new_str.split()]
        print(f'{s.split()[0]} {sum(new_2)}')

#  ------------------------------------------- вариант решения ---------------------------------------------------------


dic = {}
numbers = "1234567890 "

with open("text_6.txt", "r", encoding="utf-8") as file:
    for line in file:
        head, hours = line.split(":")
        dic[head] = sum(map(int, "".join([num for num in hours if num in numbers]).split()))
print(dic)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


subj = {}
with open('text_6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.replace('-', '0').replace(':', '').replace('(л)', '') \
            .replace('(пр)', '').replace('(лаб)', '').split()
        subj[line[0]] = sum(map(int, line[1:]))
    print(f'Общее количество часов по предмету: \n{subj}')

#  ------------------------------------------- вариант решения ---------------------------------------------------------


result = {}
with open("text_6.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        lesson_timing = []
        lessons = ([el for el in line.split(" ")])
        for el in lessons:
            lesson_timing.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(':')[0]] = sum([int(i) for i in lesson_timing if i.isdigit()])

print(result)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


with open('text_6.txt', 'r', encoding='utf-8') as file:
    print({string.split(':')[0]: sum([int(s[:s.index('(')]) for s in string.split() if '(' in s]) for string in file})


#  ------------------------------------------- вариант решения ---------------------------------------------------------

import re

subs_total_hours = {}

with open("text_6.txt") as f:
    for line in f.readlines():
        subs_total_hours[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(subs_total_hours)