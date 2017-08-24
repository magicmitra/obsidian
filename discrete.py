#----------------------------------------------------------------------------------
# This is a function that will calculate the interest rate in a discrete manner.
# Wirh this, interest is compounded k times a year and the bank will only add 
# interest to the pricipal k times a year.
# The balance will then be returned.
# Author: Erv
#-----------------------------------------------------------------------------------

from decimal import *

constant_one = 1
# Formula : B(t) = P(1 + (r/k)) ** kt
# B = balance
# P = principal
# r = interest rate
# k = times compounded
# t = time in years

def discrete_calculate():
	
	# prompt the user for values
	principal = float(input("Enter the principal amount: $"))
	time = int(input("Enter the time in years: "))
	rate = float(input("Enter the interest rate in percentage form (Ex. 5.2): "))
	compound = int (input("How many times a year is the interest compounded? "))
	
	# calculate the balance
	rate = rate * 0.01
	exponent = compound * time
	fraction = rate / compound
	meta_balance = (fraction + constant_one) ** exponent
	balance = principal * meta_balance
	balance = round(balance, 2)
	
	return "balance will be $" + str(balance)


	
	