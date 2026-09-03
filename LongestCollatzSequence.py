# To find the starting number, under one million, produces the longest chain
# Defining function which finds the next iterative element
def nextElement(num):
    if(num % 2 == 0):
        return num/2
    else:
        return 3*num + 1
# Defining function to find collatz sequence, assuming ending at 1 for all numbers
def collatzify(number):
    arr = []
    arr.append(number)
    while(number != 1):
        nextNumber = nextElement(number)
        arr.append(nextNumber)
        number = nextNumber
    return arr
# Now, finding longest sequence among all numbers below 1000000
number = 1
maxNumber = 0
maxLength = 0
while(number <= 1000000):
    sequence = collatzify(number)
    if(len(sequence) > maxLength):
        maxLength = len(sequence)
        maxNumber = number
    number += 1
print(f"The maximum length of sequence is {maxLength} of number: {maxNumber}")