# Initializing the first two fibonacci numbers
a = 1
b = 2
# Defining top value as 4,000,000
top = 4000000
# Simultaneously summing the even fibonacci numbers
answer = 0
while b <= top:
    if b%2 == 0:
        answer += b
    a, b = b, a+b
print(answer)