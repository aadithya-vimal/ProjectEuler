# Defining function to check if triangle is right angle
def isRightAngled(a,b,c):
    if (a**2 + b**2) == c**2:
        return True
    return False
# Upper bound is p <= 1000, starting from p = 12, as the smallest perimeter of a right-angled triangle is 12 (3,4,5)
def findRightAngledTriangles():
    max_count = 0
    count = 0
    for p in range(12, 1001):
        for a in range(1, p//3):
            for b in range(a, (p-a)//2):
                c = p - a - b
                if isRightAngled(a, b, c):
                    count += 1
        if count > max_count:
            max_count = count
            perimeter_with_max_count = p
        count = 0
    return perimeter_with_max_count
print(f"The perimeter with the maximum number of right-angled triangles is: {findRightAngledTriangles()}")