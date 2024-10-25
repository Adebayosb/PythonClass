poundsinkilogram = 0.45359237
inchestometers = 0.0254

weightinpounds = float(input("Enter weight in pounds: "))
heightininches = float(input("Enter height in inches: "))

weightinkilogram = weightinpounds * poundsinkilogram
heightinmeters = heightininches * inchestometers

bmi = weightinkilogram / (heightininches ** 2)

print(f"Bmi is {bmi:}")