number= int(input("enter fiveDigit: "))
digitone = number // 10000
digittwo = (number // 1000) % 10
digitthree = (number // 100) % 10
digitfour = (number // 10) %10
digitfive = number % 10

print(digitone, digittwo, digitthree, digitfour, digitfive,)