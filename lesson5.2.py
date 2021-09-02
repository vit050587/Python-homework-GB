# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.



def words_func():
    try:
        with open('file.txt', 'r', encoding="utf-8") as file:
            list = file.readlines()
            print(f'Количество строк в файле {len(list)}')
            for i in range(len(list)):
                str_num = list[i].split()
                print(f'Количество слов в {i + 1}-ой строке: {len(str_num)}')
    except FileNotFoundError:
        return 'Файл не найден.'


words_func()
