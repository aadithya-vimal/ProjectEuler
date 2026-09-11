# Defining function to find factorial of a number
def factorial(n):
    fact = 1
    while n>0:
        fact *= n
        n -= 1
    return fact
# The formula for no. of paths is (2n)!/(n!)^2
def paths(n):
    return (factorial(2*n))/(factorial(n)**2)
# Printing final answer
print(f"Number of paths for 20x20 grid is: {paths(20)}")