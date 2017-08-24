#-----------------------------------------------
# This is a function at the beginning of the program 
# to prompt the user how he/she wants to use the
# program. It includes a check for key validity
# only 'Q' or 'w' keys are valid.
# It then returns the entered valid key.
# Author: Erv
#------------------------------------------------

def welcome_func():
	
	print("Welcome to Obsidian, a tool for cryptocurrency information.")
	print("Press 'Q' to use the cryptocurrency infomation tool.")
	print("Press 'W' to view a cryptocurrency from the CLI.")
	print("Press 'E' to use the interest calculator.")
	print("--------------------------------------------------------------")
	
	choice = input(str("Q, W or E:"))
	choice = choice.upper()
	while choice  !="W" and choice != "Q":
		print("Invalid input, try again.")
		print("Press 'Q' to view a webpage of a cryptocurrency.")
		print("Press 'W' to view a cryptocurrency from the CLI.")
		print("Press 'E' to use the interest calculator.")
		print("--------------------------------------------------------------")
		
		choice = input(str("Q, W or E: "))
		choice = choice.upper()
		
	return choice
	

