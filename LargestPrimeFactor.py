# Defining function to find the max prime factor of a number

def maxPrimeFactor(num):
    d = 2
    factors = []
    while d*d <= num:
        while num%d == 0:
            factors.append(d)
            num //= d
        d += 1
    if num>1:
        factors.append(num)
    return max(factors)

print(maxPrimeFactor(600851475143))