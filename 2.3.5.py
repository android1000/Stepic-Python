import itertools


def primes():
    x = 2
    while True:
        count = 0
        for i in range(2, x+1):
            if x % i == 0:
                count+=1
        if count == 1:
            yield x
        x += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# primes()
