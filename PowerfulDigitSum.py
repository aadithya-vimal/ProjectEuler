# For maximum digital sum of a^b for a, b < 100, we subsitute values for a and b iteratively till we find maximum sum
maxSum = 0
for a in range(1, 100):
    for b in range(1, 100):
        digitSum = sum(int(digit) for digit in str(a**b))
        if digitSum > maxSum:
            maxSum = digitSum
print(f"The maximum digital sum of a^b for a, b < 100 is: {maxSum}")
