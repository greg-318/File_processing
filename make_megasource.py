"""
При вызове передаються названия файлов.txt скрипт создает два новых файла в репозитории:
big_file.txt --> в него записываются все строки из всех переданных фалов
big_file_fin.txt --> исходный файл, в него будут записаны строки исходя из условия задания.
Если файлы большие, то я думаю можно также собрать все файлы в один большой файл,
брать первый элемент файла и читать по строчно файл сверяя с первым элементом файла,
если найдуться одинаковые элементы то сохранять их в памяти, потом записать наденные обработанные элементы в
новый фал, при этом удалить первый элемент из большоего файла. И так повторить пока не закончаться
элементы в большом файле, но нужно будет еще делать одну проверку, существует ли элемент
в новом созданном файле каждый рес. 
"""

import sys


def read_file(name_file):
    """
    :param name_file: название файла
    :return: список строк из файла
    """
    with open(name_file, 'r') as out_file:
        out_file = out_file.readlines()
    return out_file


def write_file(name_file, list_str):
    """
    :param name_file: название файла
    :param list_str: списов строк
    :return: NONE
    """
    with open(name_file, 'w') as out_file:
        for string in list_str:
            out_file.write(string)


def read_files(name_file_list):
    """
    принимает список с именами файлов читает их построчно и записывает данные с фалов в один файл.
    :param name_file_list: список с именами файлов
    :return: None
    """
    with open('big_file.txt', 'w') as out_file:
        for f_name in name_file_list:
            with open(f_name) as infile:
                for line in infile:
                    out_file.write(line)


def size_check(d):
    """
    принимает словарь с одинаковыми словами с файле и проверяет веса.
    :param d:  словарь {индекс строки в файле : строка из файла } повторяющиеся строки в файле
    :return: формированная новая строка.
    """
    size = set([sys.getsizeof(i) for i in d.values()])
    if len(size) == 1: #если у всех веса одинаковые.
        numbers = ",".join(set(",".join([i[:-1].split('\\t')[1] for i in d.values()]).split(','))) # если веса одинковые то отбираються уникальные числа из всех строк
        word = d[0].split('\\t')[0]
        return f"{word}\\t{numbers}\n"
    else: #выбираються числа с самым большим весом если веса разные
        sizes = 0
        element = ''
        for j in d.values():
            if sys.getsizeof(j) > sizes:
                sizes = sys.getsizeof(j)
                element = j
        return f"{element}"


if __name__ == "__main__":

    read_files(sys.argv[1:])
    list_string = read_file('big_file.txt')
    f = {}
    fin_list = []
    while len(list_string) != 0:
        for j, i in enumerate(list_string):
            if list_string[0].split('\\t')[0] == i.split('\\t')[0]:
                f[j] = i
        if len(f) != 1:
            fin_list.append(size_check(f))
        else:
            fin_list.append(f[0])
        for i in f.keys().__reversed__():
            del list_string[i]
        f = {}

    write_file('big_file_fin.txt', fin_list)
