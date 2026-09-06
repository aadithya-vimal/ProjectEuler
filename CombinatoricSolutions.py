# To find not necessarily distinct, values of nCr for 1 <= n <= 100, are greater than one-million
bound = 1000000
# Defining function to find factorial of given number
def factorial(num):
    fact = 1
    while num>0:
        fact *= num
        num -= 1
    return fact
# Defining function to find the combination of two numbers
def combination(n,r):
    combi = factorial(n)/(factorial(r)*factorial(n-r))
    return combi
# Iterating through all possible combinations
# Already given 23C10 is the least possible combination for >1000000 value
answer = 0
for n in range(23,101):
    for r in range(1,n):
        combiValue = combination(n,r)
        if combiValue>bound:
            answer += 1

print(f"The count of all such numbers is: {answer}")