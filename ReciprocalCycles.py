import math
# To find Find the value of 𝑑 <1000 for which 1/𝑑 contains the longest recurring cycle in its decimal fraction part.
"""
1/2	=0.5
1/3	=0.⁢(3)
1/4	=0.25
1/5	=0.2
1/6	=0.1⁢(6)
1/7	=0.⁢(142857)
1/8	=0.125
1/9	=0.⁢(1)
1/10=0.1
"""
# Defining function to get the 1/d value, and find the repetition
d_value = 0
maxLength = 0
def repetitionCompute(d):
    pattern = set()
    patternFound = False
    num = 1
    while not patternFound:
        num *= 10
        num %= d  # Use integer modulo instead of math.modf to get the true remainder
        
        if num == 0:  # Handle terminating decimals (like 1/2 or 1/5)
            break
        if num in pattern:
            patternFound = True
        else:
            pattern.add(num)
    return len(pattern)
for num in range(1,1001):
    length = repetitionCompute(num)
    if length > maxLength:
        maxLength = length
        d_value = num
print(f"The maximum length value is {maxLength} of number: {d_value}")