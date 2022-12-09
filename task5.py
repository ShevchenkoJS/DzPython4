# 5'. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

import sympy

def get_polynom(file_num: int) -> str:
    """Взять многочлен из файла"""
    with open(f'file{file_num}.txt', 'r') as f:
        polynom = f.readline()
    return polynom


"""Сумма двух многочленов"""
polynom1 = sympy.simplify(get_polynom(1))
polynom2 = sympy.simplify(get_polynom(2))
print('\t\t' + str(polynom1) + '\n\t\t' + str(polynom2))
x = sympy.Symbol('x')
polynom = str(sympy.simplify(polynom1 + polynom2))
print('Сумма = ' + polynom)
with open('file3.txt', 'w') as f:
    f.write(polynom)
