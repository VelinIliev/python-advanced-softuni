from math import log

number = int(input())
log_base = input()

if log_base == 'natural':
    print(f'{log(number):.2f}')
else:
    print(f'{log(number, int(log_base)):.2f}')