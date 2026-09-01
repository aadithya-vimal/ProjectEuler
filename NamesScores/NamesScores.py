# Defining function to extract numerical value of the alphabet
def numify(alphabet):
    numValue = ord(alphabet) - 64
    return numValue
# Extracting each name from the txt file
with open(r"C:\Users\aadit\OneDrive\Desktop\ProjectEuler\NamesScores\names.txt" , "r") as file:
    content = file.read()

names = content.split(',')
names = [name.replace('"', '') for name in names]
names.sort()
# Index variable to track the position of the name
index = 0
totalSum = 0
# Iterating through each name
for name in names:
    index += 1
    nameSum = 0
    for letter in name:
        nameSum += numify(letter)
    totalSum += nameSum * index

print(f"The required total sum of all names: {totalSum}")