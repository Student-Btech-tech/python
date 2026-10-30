numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]
print("Even:", even)
print("Odd:", odd)