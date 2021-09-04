# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

quant = int(input("Введите количество элементов списка: "))
spisok = []
i = 0
el = 0
while i < quant:
    spisok.append(input("Введите значение списка: "))
    i += 1

for element in range(int(len(spisok) / 2)):
    spisok[el], spisok[el + 1] = spisok[el + 1], spisok[el]
    el += 2
print(spisok)

# ----------------------------------------------------------------------

my_list = list(input("Enter the number without space - "))
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)

# ----------------------------------------------------------------------

my_list = input('Ведите числа списка через пробел - ').split()
print('Введенный список: ', my_list)

idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1

my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
print('Измененный список: ', my_list)

#-----------------------------------------------------------------------

user_list = input("Enter the number without space - ").split()
for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))

print(user_list)