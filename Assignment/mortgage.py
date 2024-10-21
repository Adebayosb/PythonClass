borrowedamount = float(input("the amount the client wishes to borrow $"))
interestrate = float(input("yearly interest rate "))
duration = float(input("duration of the mortgage in years "))

monthlyrate = (interestrate /100) / 12
totalmonth = duration * 12

monthlymortgage = (borrowedamount * monthlyrate * (1 + monthlyrate) ** totalmonth / ((1+monthlyrate) ** totalmonth -1))

print(F"monthly mortgage payment: ${monthlymortgage}")