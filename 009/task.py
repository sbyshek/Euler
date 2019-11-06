"""
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.

"""


def b_(m, n) -> int:
    if (m - n) % 2 != 0:
        return m ** 2 - n ** 2
    else:
        return 0


def a_(m, n) -> int:
    if (m - n) % 2 != 0:
        return 2 * m * n
    else:
        return 0


def c_(m, n) -> int:
    if (m - n) % 2 != 0:
        return m ** 2 + n ** 2
    else:
        return 0


k: bool = True
for i in range(1, 25): # Границу в 25 подобрал экспериментальным путем, после вывода i, j
    if k:
        for j in range(1, 25):
            if j > i and k:
                a = a_(j, i)
                b = b_(j, i)
                c = c_(j, i)
                if a + b + c <= 1000:
                    if (a * b * c != 0) and (a ** 2 + b ** 2 == c ** 2):
                        if a + b + c == 1000:
                            print("!" * 3, a, "+", b, "+", c, "= 1000")
                            print("Answer is", a * b * c)
                            k = False
                            break
                        else:
                            print(a, b, c, i, j)
                else:
                    break
    else:
        break


