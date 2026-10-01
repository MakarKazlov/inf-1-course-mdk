#!/usr/bin/python3
import sys
a = [line for line in sys.stdin]
a.sort(reverse='True')
print('-'*30)
for i in a:
    print(f"{i:^30}")
print('-'*30)
