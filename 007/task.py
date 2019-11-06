"""
    Задача 7
10001-ое простое число
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?

Будем использовать теорему о распределении простых чисел

Также эта теорема может быть эквивалентным образом переформулирована для описания поведения
k-го простого числа  p_{k}: она утверждает, что

p_{k} ~ k ln k, k -> infty
"""

import math
from typing import List


def eratosfen(n: int, p_list: list):
    """
    Алгоритм решета Эратосфена
        Вход: натуральное число n
        Пусть A — булевый массив, индексируемый числами от 2 до n,
        изначально заполненный значениями true.

         для i := 2, 3, 4, ..., пока i2 ≤ n:
          если A[i] = true:
            для j := i2, i2 + i, i2 + 2i, ..., пока j ≤ n:
              A[j] := false

        Выход: числа i, для которых A[i] = true.
    :type n: int
    :type p_list: list[bool]
    """
    for i in range(2, n):
        if i * i > n:
            break
        else:
            if p_list[i]:
                for j in range(i * i, n, i):
                    p_list[j] = False
            else:
                pass


def main() -> None:

    k = 10001
    num = 0
    max_n: int = int(k * math.log(k)) * 2
    prime_list: List[bool] = []

    for i in range(0, max_n):  # Заполняем массив
        prime_list.append(True)
    eratosfen(max_n, prime_list)

    for i in range(0, max_n):
        if prime_list[i]:
           if num == 10001:
               break
           num += 1
           print(num, ": ->", i)
        else:
            pass


main()

