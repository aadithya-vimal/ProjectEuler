from fractions import Fraction
ansNum = []
ansDen = []

for num in range(10, 100):
    for den in range(num + 1, 100):
        # Exclude trivial cases (e.g., 30/60 = 3/6)
        if num % 10 == 0 and den % 10 == 0:
            continue
            
        n_str, d_str = str(num), str(den)
        
        # Check for a shared digit
        common_digits = set(n_str) & set(d_str)
        if len(common_digits) == 1:
            common = list(common_digits)[0]
            
            # Remove the common digit to simulate "incorrect" cancellation
            new_num = int(n_str.replace(common, '', 1))
            new_den = int(d_str.replace(common, '', 1))
            
            # Verify if the canceled fraction matches the original mathematical value
            if new_den != 0 and num / den == new_num / new_den:
                ansNum.append(num)
                ansDen.append(den)

print(f"Answers are (numerators): {ansNum}")
print(f"Answers are (denominators): {ansDen}")

product = Fraction(1, 1)
for num, den in zip(ansNum, ansDen):
    product *= Fraction(num, den)

print(f"Product in lowest terms: {product}")