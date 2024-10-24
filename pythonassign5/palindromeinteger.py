digit = int(input("Enter a three digit number: "))

digit1 = digit // 100
digit2 = digit % 10

if digit == digit2:
	print(f"{digit} is palindrome")
else:
	print(f"{digit} is not palindrome")