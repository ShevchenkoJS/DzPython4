# 1'. Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

from math import pi 

def format_by_mask(num: float, accurace: float) -> float:
    """форматирует число по заданной маске"""
    accurace = str(accurace)
    accurace = len(accurace[accurace.find('.')+1::])
    return float(f'{pi:0.{accurace}f}')     #f'a:0.3f'


d = input('Введите точность в формате "0.001": ')
print(format_by_mask(pi, d))