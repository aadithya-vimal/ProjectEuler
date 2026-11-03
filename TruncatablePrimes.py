# Function to check if a number is prime
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i ==0:
            return False
    return True

# Function to separate the digits of a number, remove only the first element iteratively and store all the nums in an array
def truncateDigits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits.reverse()
    truncated_nums = [] 
    truncated_nums.append(int(''.join(map(str, digits))))  # Add the original number
    for i in range(1, len(digits)):
        truncated_num = int(''.join(map(str, digits[i:])))
        truncated_nums.append(truncated_num)
    return truncated_nums

#Function to check if a number is a truncatable prime
def isTruncatablePrime(num):
    if(num < 10):  # Single-digit primes are not considered truncatable primes
        return False
    truncated_nums = truncateDigits(num)
    # Left to right truncation
    for truncated_num in truncated_nums:
        if not isPrime(truncated_num):
            return False
    # Right to left truncation
    for i in range(len(truncated_nums)):
        truncated_num = int(''.join(map(str, str(num)[:len(str(num)) - i])))
        if not isPrime(truncated_num):
            return False
    return True

foundCount = 0
sumOfTruncatablePrimes = 0

# Loop through numbers to find truncatable primes
num = 11  # Start checking from the first two-digit prime
while foundCount < 11:  # There are only 11 truncatable primes
    if isTruncatablePrime(num):
        foundCount += 1
        sumOfTruncatablePrimes += num
    num += 2  # Increment by 2 to check only odd numbers (even numbers > 2 are not prime)

print("Sum of truncatable primes:", sumOfTruncatablePrimes)