'''Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime():
    yield 2
    p = 1
    while True:
        p = p + 2
        if not is_prime(p):
            continue
        yield p

if __name__ == '__main__':
    f = prime()
    n = 600851475143
    while True:
        p = f.next()
        if p >= math.sqrt(600851475143) or p == n:
            print n
            break
        while n % p == 0:
            n = n / p
