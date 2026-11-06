filename = "notes.txt"

# Write to the file
with open(filename, "w", encoding="utf-8") as file:
    file.write("My first note\n")

# Read the file
with open(filename, "r", encoding="utf-8") as file:
    print("File contents:")
    print(file.read())

# Add more text
with open(filename, "a", encoding="utf-8") as file:
    file.write("Another note\n")