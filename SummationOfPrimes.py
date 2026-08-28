import math
# Defining function to check if number is prime
def isPrime(num):
    if(num == 2):
        return True
    if(num%2 == 0 and num != 2):
        return False
    topBound = int(math.sqrt(num))
    for i in range(2,topBound+1):
        if(num % i == 0):
            return False
    return True
# Now, to find of all primes below 2000000
upperBound = 2000000
totalSum = 0
for number in range(2,upperBound):
    if(isPrime(number)):
        totalSum += number
print(f"The sum of all primes below 2 million is: {totalSum}")