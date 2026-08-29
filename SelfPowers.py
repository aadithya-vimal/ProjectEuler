# We need to find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000
totalSum = 0
# Using simple brute force method
for num in range(1,1001):
    totalSum += num**num
# Getting the last ten digits of the total sum
lastTenDigits = totalSum % 10000000000
print(f"The last ten digits of the series are: {lastTenDigits}")