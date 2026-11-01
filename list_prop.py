# List banana
list = [10, 20, 30, 40, 50]
print("List:", list)

# Index (0 se start, -1 = last)
print("First:", list[0])
print("Last:", list[-1])

# Change karna (mutable)
list[0] = 99
print("Change:", list)

# Adding
list.append(60) 
print(list)       # end me
list.insert(1, 15)     # index 1 par
print(list)

# Delete karna
list.remove(15) 
print(list)       # value se
list.pop()             # last wala
print("Delete:", list)

# Sort aur reverse
list.sort()
print("Sort:", list)
list.reverse()
print("Reverse:", list)

# Slicing
print("Slice:", list[1:3])

# Len, sum, max, min
print("Len:", len(list))
print("Sum:", sum(list))
print("Max:", max(list))
print("Min:", min(list))

# Loop
for i in list:
    print(i, end=" ")