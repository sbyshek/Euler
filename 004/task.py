def is_polindrom(n: int) -> bool:
    """
    Функция проверяет. является ли число n полиндромом
    :param n: int
    :return: bool
    """
    res: bool = False
    number: str = str(n)
    length: int = number.__len__() - 1
    for i in range(0, (length // 2 + 1)):
        if number[i] == number[length - i]:
            res = True
        else:
            res = False
            break
    return res


def store_res(a: int, b: int, maxim: int) -> int:
    """
    Функция определяет, является ли произведение чисел a и b максимальным числом
    в случае нахождения максимума в глобальые переменные x и y сохраняются значения множителей

    :param a:
    :param b:
    :param maxim:
    :return: int:
    """

    if a * b > maxim:
        global x
        global y
        x = a
        y = b
        return a * b
    else:
        return maxim


def main() -> None:
    """
    Основное тело программы. В цикле проверяется произведение возможных трехзначных чисел на максимальное значение
    и на то, является ли оно полиндромом. Переменная maximum = 0, будет накапливать максимальное значение
    из всех подобранных полиндромов. Переменные max_num=1000 и min_num=100 содержат границы возможных трехзначных чисел.
    :return: None
    """
    maximum: int = 0
    max_num: int = 1000
    min_num: int = 100

    for i in range(1, max_num - min_num):
        x1: int = max_num - i
        for j in range(1, max_num - min_num):
            x2: int = max_num - j
            add: int = x1 * x2
            if is_polindrom(add):
                maximum = store_res(x1, x2, maximum)
                break
            else:
                pass

    print("Maximum polindrom is", maximum, "equal is ", x, "*", y)


main()
