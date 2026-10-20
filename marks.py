name = input("Enter your name: ")

maths = int(input("Enter Maths marks: "))
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
percentage = (total / 300) * 100

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Maths:", maths)
print("Physics:", physics)
print("Chemistry:", chemistry)
print("Total Marks:", total, "/ 300")
print("Percentage:", percentage, "%")