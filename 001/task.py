s: int = 0
for i in range(1, 1001):
    if ((i%3 ==0) or (i%5==0)):
        s+=i
    else:
        continue
else:
    print(i)

print(s)
