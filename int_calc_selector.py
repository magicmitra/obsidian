#-----------------------------------------------------------------
# This program selects the mode type of interest:
# Continuous vs Discrete.
# It includes a check to make sure that the user only 
# inputs either a 'D' or a 'C'.
# It then returns the valid entered kry.
# Auhtor: Erv
#------------------------------------------------------------------

def select_calculator():
	
	print("Select between the mode of interest rates.")
	print("Press 'D' to use compound interest (discrete).")
	print("Press 'C' to use continuous interest.\n")
	print("--------------------------------------------------------------")
	
	choice = input(str("D or C:"))
	choice = choice.upper()
	while choice  !="D" and choice != "C":
		print("Invalid input, try again.")
		print("Press 'D' to use compound interest (discrete).")
		print("Press 'C' to use continuous interest.\n")
		print("--------------------------------------------------------------")
		
		choice = input(str("D or C: "))
		choice = choice.upper()
		
	return choice