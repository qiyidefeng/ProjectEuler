'''Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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
    for i in range(10000):
        f.send(None)
    print f.next()