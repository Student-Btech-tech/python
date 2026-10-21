weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))

bmi = weight / (height * height)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("BMI category: Underweight")
elif bmi < 25:
    print("BMI category: Normal range")
elif bmi < 30:
    print("BMI category: Overweight")
else:
    print("BMI category: Obesity range")