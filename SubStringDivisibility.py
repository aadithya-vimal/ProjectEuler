# Function to generate and store all 0 to 9 pandigital numbers
def panDigitalNumbers():
    from itertools import permutations
    # Generate all permutations of the digits 0-9
    digits = '0123456789'
    pandigital_numbers = [''.join(p) for p in permutations(digits)]
    return pandigital_numbers

#Function to check if a number satisfies the substring divisibility property
def hasSubstringDivisibilityProperty(num_str):
    # List of primes corresponding to the divisibility checks
    primes = [2, 3, 5, 7, 11, 13, 17]
    
    # Check the substring divisibility property
    for i in range(1, 8):
        substring = int(num_str[i:i+3])  # Get the substring of length 3
        if substring % primes[i-1] != 0:
            return False
    return True
# Function to find the sum of all pandigital numbers with the substring divisibility property
def sumOfPandigitalNumbersWithProperty():  
    pandigital_numbers = panDigitalNumbers()
    total_sum = 0
    
    for num_str in pandigital_numbers:
        if hasSubstringDivisibilityProperty(num_str):
            total_sum += int(num_str)
    
    return total_sum
print(f"The sum of all 0 to 9 pandigital numbers with the substring divisibility property is: {sumOfPandigitalNumbersWithProperty()}")