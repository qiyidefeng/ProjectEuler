'''Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import math


d = {2: 1}
for i in range(3, 21):
    temp = i
    for k, v in d.items():
        index = 0
        while True:
            if temp % k == 0:
                index = index + 1
                temp = temp / k
            else:
                break
        if v < index:
            d[k] = index
    if temp != 1:
        d[temp] = 1
sum = 1
for k, v in d.items():
    sum = sum * math.pow(k, v)
print d
print int(sum)
