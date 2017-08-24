#-----------------------------------------------------------------------------------
# This is a function that computes the balance in a continuous compound interest
# manner. The user will provide the principal amount and the interest rate.
# The balance will be returned afterwards.
# Author: Erv
#------------------------------------------------------------------------------------

from decimal import *

# Some numbers
euler_constant = 2.718

# Formula for continuous is B(t) = Pe ** rt
# B = balance
# P = Principal
# e = euler's constant
# r = rate
# t = time in years
def continuous_calculate():
	
	# Prompt the user for values
	principal = float(input("Enter the Principal amount: $"))
	time  = int(input("Enter the time in years: "))
	rate = float(input("Enter the interest rate in percentage form (Ex. 5.2): "))
	
	# calculate the Balance after user entered ptompted values
	rate = rate * 0.01
	exponent = rate * time
	new_euler = euler_constant ** exponent
	balance = principal* new_euler
	balance = round(balance, 2)
	
	return "Balance will be $" + str(balance)
	

	