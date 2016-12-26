"""Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math


def prime():
    all = [2]
    yield 2
    p = 1
    while True:
        p = p + 2
        flag = True
        for i in all:
            if i>math.sqrt(p):
                break
            if p % i == 0:
                flag = False
                break
        if flag:
            all.append(p)
            yield p

if __name__ == '__main__':
    res = 0
    f = prime()
    while True:
        k = f.next()
        if k >= 2000000:
            break
        res = res + k

    print res
