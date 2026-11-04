a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) # Union: {1,2,3,4,5,6}
print(a & b) # Intersection: {3,4}
print(a - b) # Difference: {1,2}
print(a ^ b) # Symmetric Difference: {1,2,5,6}