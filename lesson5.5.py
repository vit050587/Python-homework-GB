# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def sum_func():
    try:
        with open('file_5.txt', 'w+') as file_num:
            str_num = input('Введите цифры через пробел \n')
            file_num.writelines(str_num)
            numbers = str_num.split()

            print(sum(map(int, numbers)))
    except IOError:
        print('Err!!!')
    except ValueError:
        print('Программа работает с числами! Вы вишли')


sum_func()
