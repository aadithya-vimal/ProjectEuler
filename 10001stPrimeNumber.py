import math
# Initializing counter variable 
counter = 1
# Initializing loop to find the req prime number
num = 3
while(counter != 10001):
    square_root = int(math.sqrt(num))
    for i in range(2,square_root+1):
        if num%i==0:
            break
    else:
        counter += 1
        if counter == 10001:
            break
    num += 2
print(f"The 10001st prime number is: {num}")