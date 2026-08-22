# Defining the top value and finding(and simultaneously summing) the palindromic numbers
top = 1000000
totalSum = 0

for num in range(1,top+1):
    decimalTrue = False
    binaryTrue = False
    # First checking the decimal value
    initialNum = num
    newNum = 0
    decList = []
    while num>0:
        # 586
        digit = num % 10
        decList.append(digit)
        num //= 10
    #list = [6,8,5]
    power = len(decList)-1
    for i in decList:
        newNum += i*(10**power)
        power -= 1
    if newNum == initialNum:
        decimalTrue = True
    newNum = 0
    # Next, checking for decimal value
    # Taking the binary number and omitting '0b'
    binaryNum = int(bin(initialNum)[2:])
    initialBinaryNum = binaryNum
    binList = []
    while binaryNum>0:
        # 1001001010
        digit = binaryNum % 10
        binList.append(digit)
        binaryNum //= 10
    power = len(binList)-1
    for i in binList:
        newNum += i*(10**power)
        power -= 1
    if newNum == initialBinaryNum:
        binaryTrue = True
    if (binaryTrue and decimalTrue):
        totalSum += initialNum

print(f"Total sum of all required numbers: {totalSum}")