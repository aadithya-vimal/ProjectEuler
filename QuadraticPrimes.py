# Euler discovered the remarkable quadratic formula:
#  class="center">$n^2 + n + 41$
# It turns out that the formula will produce $40$ primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by $41$, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by $41$.
# The incredible formula $n^2 - 79n + 1601$ was discovered, which produces $80$ primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, $-79$ and $1601$, is $-126479$.
# Considering quadratics of the form:
# $n^2 + an + b$, where $|a| &lt; 1000$ and $|b| \le 1000$<br><br><div>where $|n|$ is the modulus/absolute value of $n$<br>e.g. $|11| = 11$ and $|-4| = 4$</div>
# Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.
# Defining function to find if given number is prime or not
def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
# Defining function to find result of Euclid's formula for given a and b
def euclidsFormula(a,b,n):  
    return n**2 + a*n + b
# Starting the main function 
def main():
    maxCount = 0
    product = 0
    for a in range(-999,1000):
        for b in range(-1000,1001):
            n = 0
            while True:
                result = euclidsFormula(a,b,n)
                if isPrime(result):
                    n += 1
                else:
                    break
            if n > maxCount:
                maxCount = n
                product = a*b
    print(f"The product of coefficients a and b for the quadratic expression that produces the maximum number of primes is: {product}")
main()