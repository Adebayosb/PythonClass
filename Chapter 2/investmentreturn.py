p = 1000
r = 7/100
after10Years = 10
after20Years = 20
after30Years = 30

amountAfter10Years = p * (1 + r)**after10Years
amountAfter20Years = p * (1 + r)**after20Years
amountAfter30Years = p * (1 + r)**after30Years

print(f" After 10 years, you will have: ${amountAfter10Years:.2f}")
print(f" After 20 years, you will have: ${amountAfter20Years:.2f}")
print(f" After 30 years, you will have: ${amountAfter30Years:.2f}")

