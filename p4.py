# coding=utf-8
'''Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
 is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import sys


def is_palindromic(n):
    s = 0
    m = n
    while m != 0:
        mod = m % 10
        s = s * 10 + mod
        m = m / 10
    return s == n

if __name__ == '__main__':
    res = 0
    for i in range(999, 99, -1):
        if i * 999 <= res:
            break
        for j in range(999, 99, -1):
            if i * j <= res:
                break
            if is_palindromic(i * j) and i * j > res:
                res = i * j
                break
    print res
