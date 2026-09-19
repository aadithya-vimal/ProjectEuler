# Defining function to find the proper divisors, and hence the sum (d(num)) of a number
def properDivisorsSum(num):
    sumOfDivisors = 0
    for i in range(1,num):
        if(num % i == 0):
            sumOfDivisors += i
    return sumOfDivisors

# Finding all amicable numbers under 10000
bound = 10000
# Looping uptil our upper bound
totalSum = 0
for number in range(1,bound):
    sumOfNumbersDivisors = properDivisorsSum(number) #d(a) = b
    sumOfSumsDivisors = properDivisorsSum(sumOfNumbersDivisors) #d(b) 
    if sumOfSumsDivisors == number and sumOfNumbersDivisors != number:
        totalSum += number
print(f"The total sum of all amicable numbers below 10000 is: {totalSum}")