#!/usr/bin/python3
def onlyletters(s):
    res = []
    for i in s:
        if i.isalpha():
            res.append(i)
        if i == ' ':
            res.append(i)
        if i.isnumeric():
            res.append(i)
    return ''.join(res)
stroka = list(input('Введите строку: '))
print(onlyletters(stroka))

