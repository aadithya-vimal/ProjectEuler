# Iterative approach to find the first 1000-digit Fibonacci number
a = 1
b = 1
index = 1

while len(str(a)) < 1000:
    a, b = b, a + b  # Update values simultaneously
    index += 1

print(f"The {index} Fibonacci number is the first to have 1000 digits.")