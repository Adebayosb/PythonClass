firstinput = float(input("Enter firstNumber: "))
secondinput = float(input("Enter secondNumber: "))
thirdinput = float(input("Enter thirdNumber: "))

if firstinput < secondinput < thirdinput:
	print(firstinput , secondinput , thirdinput) 

elif firstinput < thirdinput < secondnput:
	print(firstinput , thirddinput , secondinput)

elif secondinput < firstinput  < thirdinput:
	print(secondinput , firstinput , thirdinput) 

elif secondinput < thirdinput  < firstinput:
	print(secondinput , thirdinput , firstinput) 

elif thirdinput < firstinput < secondinput:  
	print(thirdinput , firstinput , secondinput) 
else:
	print(firstinput, thirdinput, secondinput)