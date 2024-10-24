weight = 0.0,
height = 0.0,
bmi = 0.0,

weight = float(input("Enter weight in pounds: "))

height = float(input("Enter height in inches: "))

bmi = (weight * 703) / (height * height)

print(f"your BMI is {bmi:.2f}")


print("BMI Values")
print("Underweight: under 18.5")
print("Normal: 18.5-24.9")
print("Overweight: 25-29.9")
print("Obese: 30 or over")