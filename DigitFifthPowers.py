# First we need to establish a concrete upper bound
# Maximum fifth power sum for a 1-digit number
maxPower = 9**5
totalSum = 0
# Finding number of digits (k) where smallest k-digit number exceeds maximum sum (k*(9**5))
foundKValue = False
k = 1
while not foundKValue:
    if(k*(9**5)<(10**(k-1))):
        foundKValue = True
        break
    else:
        k += 1
# We have found the upper bound of problem as k-digits
# Starting from number 2 as 1 is not included
for num in range(2,((k*(9**5))+1)):
    originalNum = num
    sum = 0
    arr = []
    while num>0:
        digit = num % 10
        arr.append(digit)
        num //= 10
    for elem in arr:
        digit_sum += elem**5
    if digit_sum == originalNum:
        totalSum += originalNum
print(f"The total sum of all required numbers is: {totalSum}")