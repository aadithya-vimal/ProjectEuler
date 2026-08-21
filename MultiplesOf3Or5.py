# Problem is simple enough to directly find the sum
answer = 0
for i in range(3,1000):
    if i % 3 == 0:
        answer += i
    elif i % 5 == 0:
        answer += i
print(f"Sum of all multiples of 3 or 5 below 1000: {answer}")