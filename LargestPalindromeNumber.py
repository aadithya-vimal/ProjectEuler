# Creating function to check if number is palindrome
def isPalindrome(num):
    originalNum = num
    arr = []
    while num>0:
        digit = num%10
        arr.append(digit)
        num //=10
    power = len(arr)-1
    result = 0
    index = 0
    while power>=0:
        result += arr[index]*(10**power)
        index += 1
        power -= 1
    if result==originalNum:
        return True
    return False 

# We decide the range of testing that is 100 to 999
# We move down from 999 for the sake of efficiency
maxReqNum = 0
for i in range(999,100,-1):
    for j in range(i,100,-1):
        num = i*j
        if(isPalindrome(num)):
            if(num>maxReqNum):
                maxReqNum = num

print(f"The required number is: {maxReqNum}")