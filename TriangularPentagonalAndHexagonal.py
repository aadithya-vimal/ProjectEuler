# We need to find the next triangle number that is also pentagonal and hexagonal after 40755
number = 40755
t_index = 285
p_index = 165
h_index = 143
# Priming all values to find next required number
number += 1
t_index += 1
p_index += 1
h_index += 1
result = 0
# Defining three functions to find required numbers
def triangulate(num):
    result = (num*(num + 1))/2
    return result
def pentagulate(num):
    result = (num*(3*num - 1))/2
    return result
def hexagulate(num):
    result = num*(2*num - 1)
    return result
# We observe that any such number will have values of T(n1), P(n2), H(n3) as n1 > n2 > n3
# Hence, triangular check should loop most no. of times, followed by pentagonal and finally hexagonal
found = False
while not found:
    t_val = triangulate(t_index)
    p_val = pentagulate(p_index)
    h_val = hexagulate(h_index)
    if(t_val == p_val == h_val):
        result = t_val
        found = True
        break
    else:
        smallest = min(t_val,p_val,h_val)
        if(t_val == smallest):
            t_index += 1
        elif(p_val == smallest):
            p_index += 1
        else:
            h_index += 1

print(f"The required number is: {result}")
print(f"Indices found: T_{t_index}, P_{p_index}, H_{h_index}")