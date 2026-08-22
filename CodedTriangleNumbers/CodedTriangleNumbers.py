import math
with open(r"c:\Users\aadit\OneDrive\Desktop\ProjectEuler\CodedTriangleNumbers\words.txt", "r", encoding="utf-8") as file:
    words = file.read().replace('"', '').split(',') 
counter = 0
for word in words:
    sum = 0
    for alphabet in word:
        sum += ord(alphabet)-64
    if math.sqrt((8*sum)+1).is_integer():
        counter += 1
print(f"Number of words which are triangular: {counter}")