#-----------------------------------------------------------------
# This script is for the user to select the cryptocurrency of 
# interest to view. It includes a check to make sure that the 
# only entered keys are 1 - 6. 
# It then returns the valid entered key.
# Author: Erv
#------------------------------------------------------------------

# import webbrowser and requests

def crypt_peep():
	
	print("Selct the cyprtocurrency.")
	print("Press '1' for Bitcoin(BTC)")
	print("Press '2' for Ethereum(ETH)")
	print("Press '3' for Litecoin(LTC)")
	print("Press '4' for Ripple(XRP)")
	print("Press '5' for Eos(EOS)")
	print("Press '6' for Dash(DASH)")
	print("--------------------------------------------------------------")
	
	choice = input(str("'1', '2', '3', '4', '5', '6': "))
	while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6':
		print("Invalid choice ")
		print("Press '1' for Bitcoin(BTC)")
		print("Press '2' for Ethereum(ETH)")
		print("Press '3' for Litecoin(LTC)")
		print("Press '4' for Ripple(XRP)")
		print("Press '5' for Eos(EOS)")
		print("Press '6' for Dash(DASH)")
		print("--------------------------------------------------------------")
	
		choice = input(str("'1', '2', '3', '4', '5', '6': "))
		
	return choice
	

	