# Taking number value in variable
num = 2**1000
# Taking individual digits and finding sum
answer = 0;
while num>0:
    digit = num % 10
    answer += digit
    num //= 10
print(f"The sum of digits of 2^1000:{answer}")