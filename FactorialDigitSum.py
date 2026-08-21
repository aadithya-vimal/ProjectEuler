# Finding numeric value of 100!
factorial = 1
for i in range(2, 101):
    factorial *= i
print(f"Factorial of 100:{factorial}")
# Extracting and summing each individual digit of the factorial
num = factorial
answer = 0
while num>0:
    digit = num % 10 
    answer += digit
    num //= 10
print(f"Final sum:{answer}")