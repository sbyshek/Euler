"""
Домашнее задание: парсинг римских чисел
Написать функцию, которая принимает на вход строку - римское число,
а возвращает это число в арабском виде.
Например, если передаём "XV" - должна вернуть 15, если передаём "IV" - должна вернуть 4.
Вот список римских символов и их отображение на арабские числа:
I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000
"""

rome_base = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
rome_excluded = dict(IV=4, IX=9, XL=40, XC=90, CD=400, CM=900)


def simply_check(value: str) -> bool:
    res = True
    for v in value:
        if v not in rome_base:
            res = False
            break
    return res



def simply_parse_rome_digit(value: str) -> int:
    res = 0
    for i, c in enumerate(value):
        if i + 1 < len(value) and rome_base[value[i]] < rome_base[value[i + 1]]:
            res -= rome_base[value[i]]
        else:
            res += rome_base[value[i]]
    return res


