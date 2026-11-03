word = input("Word likho: ")

reverse= word[::-1]

if word == reverse:
    print("is Palindrome")
else:
    print("is not Palindrome")