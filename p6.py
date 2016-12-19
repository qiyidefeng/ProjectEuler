# coding=utf-8
'''Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


def f(n):
    res = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                res = res + i * j
    return res

if __name__ == '__main__':
    print f(10)
    print f(100)


''' more easier solution
(1 + 2 + ... + n)^2 = n^2 * (n+1)^2 * 1/4

1^2 + 2^2 + ... + n^2 = n * (n+1) * (2n+1) * 1/6
'''