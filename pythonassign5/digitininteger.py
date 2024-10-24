number = int(input("Enter integer between 0 and 1000: "))

if number < 0 or number > 1000:
	print("Error: Enter a number 0 and 1000")
else:
	sumDigit = (number %10) + (number // 10 % 10) + (number // 100)

print("Sum of the dights is:", sumDigit)