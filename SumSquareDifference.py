# Finding the individual sum of squares and square of sums
sum_of_squares = 0
square_of_sums = 0
for i in range(1,101):
    sum_of_squares += i**2
    square_of_sums += i
square_of_sums = square_of_sums**2
# Difference between the sum of the squares and square of the sums
print(f"Difference between the sum of the squares and square of the sums: {square_of_sums - sum_of_squares}")