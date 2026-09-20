import math
# Using a triangle number variable to track current TN
triangleNumber = 1
sumFactor = 2
# Defining function to find all factors(divisors) of the number, and store in count var
def factorise(num):
    count = 0
    for n in range(1,math.isqrt(num)+1):
        if(num % n == 0):
            count += 1
            if n != num // n:
                count += 1
    return count
# Looping through all TN till factor count is more than 500
while((factorise(triangleNumber)) <= 500):
    triangleNumber += sumFactor
    sumFactor += 1

print(f"The first such triangle number is: {triangleNumber}")