# Defining function to find the factorial of a number
def factorial(num):
    fact = 1
    while num>0:
        fact = fact*num
        num -= 1
    return fact
# Defining answer variable
answer = 0
# Absolute ceiling of factorial of any digit => 9! = 362880
# Hence max sum of d-digits => d x 9!
# Lower bound of d-digits => 10^(d-1)
# Hence we get d=8, thus we search for max sum for 8-digit number => 8 x 9!
top = 8*factorial(9)
# Starting the loop from 3 to ommit 1! and 2!
for number in range(3,top+1):
    temp = number
    factorialSum = 0
    while temp>0:
        digit = temp % 10
        factorialSum += factorial(digit)
        temp //= 10
    if factorialSum == number:
        answer += number
print(f"The final sum of all such numbers is: {answer}")