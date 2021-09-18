# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        for row in self.list:
            for i in row:
                print(f"{i:10}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.list)):
            for i_2 in range(len(other.list[i])):
                self.list[i][i_2] = self.list[i][i_2] + other.list[i][i_2]
        return Matrix.__str__(self)


result = Matrix([[3, 5, 32],
                 [2, 4, 6],
                 [-1, 64, -8]])
result_2 = Matrix([[-3, -5, -32],
                   [-2, -4, -6],
                   [1, -64, 8]])
print(result.__add__(result_2))

#-----------------------решение GB----------------------------------

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([f"{itm:03}" for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Ошибка размерностей матриц'


m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [['5', '7', '23'], ['9', '23', '-54'], ['12', '3', '16']]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2

# stroki = int(input("Введите количество строк и столбцов матрицы: "))
# stolbci = stroki
#
# matrix1 = Matrix([[i * j for j in range(stroki)] for i in range(stolbci)])
# matrix2 = Matrix([[i + j for j in range(stroki)] for i in range(stolbci)])
#
# print('First matrix:\n', matrix1, end='\n\n')
# print('Second matrix:\n', matrix2, end='\n\n')
# print('Summ of first and second matrix:\n', matrix1 + matrix2)


#  ------------------------------------------- вариант решения ---------------------------------------------------------

a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
print(f"matrix 1 + matrix 2\n{matrix_1 + matrix_2}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import zip_longest


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n '.join(['\t '.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                       for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])


m = [[1, 2, 3], [3, 4, 5], [1, 2]]
n = [[9, 8, 7], [7, 6, 5]]

matr_1 = Matrix(m)
matr_2 = Matrix(n)

print(matr_1)
print(matr_1 + matr_2)


#  ------------------------------------------- вариант решения ---------------------------------------------------------


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: '   '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


my_m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_m1)
print(my_m2)
s = my_m1 + my_m2
print(s)
