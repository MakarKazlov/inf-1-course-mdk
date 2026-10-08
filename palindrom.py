#!/usr/bin/python3
def palindrom(n):
    return n == n[::-1]
word = input('Введите слово: ')
print(palindrom(word))
