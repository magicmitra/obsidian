#----------------------------------------------
# If else to select cryptocurrency,
# simply appends the coin name to be passed on 
# as a URL. This file was created to to prevent 
# the developer from hardcoding the function more
# than once.
# Author: Erv
#------------------------------------------------

def select_coin(num):
	
	returned_str = " "
	
	if num == '1':
		returned_str = 'bitcoin'
	elif num == '2':
		returned_str = 'ethereum'
	elif num == '3':
		returned_str = 'litecoin'
	elif num == '4':
		returned_str = 'ripple'
	elif num == '5':
		returned_str = 'eos'
	else:
		returned_str = 'dash'
		
	return returned_str