#!/usr/bin/python3
def prostye(n):
    res = []
    delitel = 2
    while n > 1:
        if n % delitel == 0:
            n = n // delitel
            res.append(delitel)
        else:
            delitel += 1
    return res
k = int(input("Введите число для разложения: "))
print(prostye(k))

