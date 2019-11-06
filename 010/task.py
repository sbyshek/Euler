"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
"""

from typing import List
import time
start_time = time.time()

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
    for i in range(2, n + 1):
        if i * i > n:
            break
        else:
            if p_list[i]:
                for j in range(i * i, n + 1, i):
                    p_list[j] = False
            else:
                pass

prime_list: List[bool] = [] # Массив, который будет содержать индексы целых чисел

for i in range(0, 2000001): # Заполняем массив
    prime_list.append(True)


eratosfen(2000000, prime_list)

sum: int = 0

for j in range(1, prime_list.__len__() - 1):
    if prime_list[j]:
        sum += j
    else:
        pass

print(sum)
print("Elapsed %s seconds" % (time.time() - start_time))

