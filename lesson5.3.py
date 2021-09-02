# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

def salary_func():
    peoples = [['Иванов ', '12000 \n'], ['Петров ', '19000 \n'], ['Сидоров ', '85000 \n'],
               ['Косинов ', '180000 \n']]
    try:
        with open('file_1.txt', 'r+', encoding="utf-8") as file:
            for i in range(len(peoples)):
                file.writelines(peoples[i])
            str_peoples = file.readlines()
            spisok_sotrudnikov = []
            sum = 0
            for i in range(len(str_peoples)):
                salary = int((str_peoples[i].split())[1])
                if salary < 20000:
                    spisok_sotrudnikov.append((str_peoples[i].split())[0])
                sum += salary
            print(f'Средняя величина дохода сотрудников: {sum / len(peoples) / 4:.2f}')
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(spisok_sotrudnikov)}')
    except FileNotFoundError:
        return 'Err!!!'


salary_func()
