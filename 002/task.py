summ: int = 0

def fibonacci(f, s, limit):
    global summ
    n = f + s
    if n % 2 == 0:
        summ += n
    if n >= limit:
        return n
    return fibonacci(s, n, limit)


print(fibonacci(0, 1, 4000000))
print(summ)