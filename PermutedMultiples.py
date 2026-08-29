# To find the smallest possible integer for which x,2x,3x,4x,5x and 6x contain the same digits
# Defining function to take digits and place them in sorted array
def takeAndSortDigits(num):
    arr = []
    while num>0:
        digit = num % 10
        arr.append(digit)
        num //= 10
    arr.sort()
    return arr
# Iterating through all positive integer numbers to find the required number
number = 1
found = False
while not found:
    if(takeAndSortDigits(number) == takeAndSortDigits(2*number) and takeAndSortDigits(2*number) == takeAndSortDigits(3*number) and takeAndSortDigits(3*number) == takeAndSortDigits(4*number) and takeAndSortDigits(4*number) == takeAndSortDigits(5*number) and takeAndSortDigits(5*number) == takeAndSortDigits(6*number)):
        found = True
        break
    number += 1

print(f"The required number is: {number}")