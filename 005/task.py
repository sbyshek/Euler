"""
Условие задачи:
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""

from typing import List


def eratosfen(n: int, p_list: list):
    """
    Алгоритм решета Эратосфена
        Вход: натуральное число n
        Пусть A — булевый массив, индексируемый числами от 2 до n,
        изначально заполненный значениями true.

         для i := 2, 3, 4, ..., пока i^2 ≤ n:
          если A[i] = true:
            для j := i2, i2 + i, i2 + 2i, ..., пока j ≤ n:
              A[j] := false

        Выход: числа i, для которых A[i] = true.
    :type n: int
    :type p_list: list[bool]
    """
    for i in range(2, n + 1):
        if i * i > n:
            break
        else:
            if p_list[i]:
                for j in range(i * i, n + 1, i):
                    p_list[j] = False
            else:
                pass


def main() -> None:

    min10: int = 2520 # Берем известное число из условия задачи
    prime_list: List[bool] = [] # Массив, который будет содержать индексы целых чисел

    for i in range(0, 21): # Заполняем массив
        prime_list.append(True)
    eratosfen(20, prime_list)

    for i in range(10, 21): # Умножаем известное число на все простые числа от 10 до 20
        if prime_list[i]:
            min10 *= i

    print("First candidate is ", min10, "\r\nLet's try them!")

    for i in range(2, 21): # Циклом проверяем делимость на все числа от 2 до 20
        if min10 % i == 0:
            print(min10, "is divide to", i)
        else:
            print("But", min10, "is not divide to ", i, "\r\nFix it!")
            for j in range(1, prime_list.__len__() - 1):
                if prime_list[j]:
                    k = min10 * j
                    if k % i == 0:
                        min10 = k
                        break
                    else:
                        pass

    print("Seeking number is", min10)


main()
