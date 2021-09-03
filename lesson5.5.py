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

#--------------------------решение GB------------------------------

from random import randint

with open("text.txt", "w", encoding="utf-8") as my_file:
    my_list = [randint(1, 100) for _ in range(100)]
    my_file.write(" ".join(map(str, my_list)))

print(f"Sum of elements - {sum(my_list)}")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


from random import randint


with open('task_5_file.txt',  mode='w+', encoding='utf-8') as the_file:
    the_file.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
    the_file.seek(0)
    print(sum(map(int, the_file.readline().split())))
