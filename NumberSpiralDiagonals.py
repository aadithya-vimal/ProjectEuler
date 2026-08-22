# The summing factor increases by +2 after every four digits
# Top value of 1001x1001 matrix will be 1001x1001
top = 1001*1001
num = 1
sum = 1
fourCounter = 0
summingFactor = 2
while num<top:
    num += summingFactor
    sum += num
    fourCounter += 1
    if fourCounter == 4:
        summingFactor += 2
        fourCounter = 0
print(f"The sum of all diagonal elements of 1001x1001 matrix is: {sum}")