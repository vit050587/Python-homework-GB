#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

def func_1():
    num = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(num), 10):
        print(i)
func_1()

#-------------------------------------------------------------

def func_2():
    spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(spisok), 10):
        print(el)
func_2()

#-----------------------решения GB----------------------------


from itertools import count, cycle

print('Программа генерирует целые числа, начиная с указанного. Для генерации следующего числа необходимо нажать Enter,'
      ' для выхода из программы - "q"')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print(
    'Программа повторяет элементы списка. Для генерации следующего повторения необходимо нажать Enter, для выхода'
    ' из программы - "q"')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import count, cycle

my_count = count(7)
my_cycle = cycle("ABC")

for _ in range(5):
    print("(my_count, my_cycle) = ({},{})".format(next(my_count), next(my_cycle)))


#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import islice, cycle, count


def unexpected(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        my_list = [el for el in islice(count(), start_el, stop_el + 1)]
        #  repeat_list = [el for el in islice(cycle(my_list), num_str)]
        r_list = iter(el for el in cycle(my_list))
        repeat_list = [next(r_list) for _ in range(num_str)]
        print(my_list)
        return repeat_list
    except ValueError:
        return "Value Error"
    except TypeError:
        return "TypeError"


print(unexpected(input("List starting at - "), input("from to - "), input("Number of repetition - ")))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import count, cycle

# а)
iterator = count(int(input('Введите целое число, начиная с которого будут генерироваться числа: ')))
print('Первые десять чисел начиная с введенного вами числа:')
for i in range(10):
    print(next(iterator), end=' ')

# б)
print('\n- cycle -')
lst = ['string', 101, 3.1415, 15.457]
iterator = cycle(lst)
# Перебираем элементы списка два раза.
for i in range(len(lst) * 2):
    print(next(iterator), end=' ')
