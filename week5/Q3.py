import numpy as np
import math

arr = np.arange(1, 101)

def printPrime(a):
    primes = []
    for i in a:
        i = int(i)   
        if i < 2:
            continue

        flag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            primes.append(i)
            
    return primes

print(printPrime(arr))
