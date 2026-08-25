# Initializing answer number from smallest multiple of largest number
# Using nested for loop inside while loop to check divisibility
def findSmallestMultiple():
    answer = 20
    found = False
    while(not found):
        for num in range(1,21):
            if(answer%num != 0):
                # Increment by largest multiple each time its not found
                answer += 20
                break
            if(num == 20):
                found = True
                return answer
print(findSmallestMultiple())