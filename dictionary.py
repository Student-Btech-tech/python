students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    students[name] = marks

print("\nStudent Records:")
for name, marks in students.items():
    print(name, ":", marks)

# Search for a student
search = input("\nEnter name to search: ")

if search in students:
    print("Marks:", students[search])
else:
    print("Student not found")

# Find the topper
topper = max(students, key=students.get)

print("\nTopper:", topper)
print("Highest Marks:", students[topper])

# Calculate average marks
average = sum(students.values()) / len(students)

print("Average Marks:", average)