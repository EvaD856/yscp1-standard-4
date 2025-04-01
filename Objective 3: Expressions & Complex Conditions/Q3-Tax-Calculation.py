'''
Question 3: Tax Calculation
Description: Write a program that calculates the tax on a purchase based on the price. The tax rate should be 8% if the price is under $100 and 10% if it’s $100 or more.
'''

# This program calculates the tax based on price

price = float(input("Enter the price of the item: "))

# Use complex conditions to calculate the tax rate
if price < 100:
    print("Tax rate is 8%")
elif price >= 100:
    print("Tax rate is 10%")
else:
    print("Error invalid input.")