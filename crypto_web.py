#-----------------------------------------------------------------
# This script is the logic for the cryptocurrency of interest to 
# be viewed as a webpage. 
# Current lineup of  Cryptocurrencies (retreived from the world coin
# index website):
# Bitcoin, Ethereum, Litecoin, Ripple, Eos, Dash.
# Returns a message regarding the selected cryptocurrency.
# Author: Erv
#------------------------------------------------------------------

import webbrowser



# this function is the logic behind the cryptocurrency.py script
# range of 1 - 6. Any number outside this range is checked by the 
# cryptocurrency.py script. 
def crypt_receive(num):

	message = "You viewed "
	
	returned_str = " "
	if num == '1':
		# Bitcoin (BTC)
		webbrowser.open('https://www.worldcoinindex.com/coin/bitcoin')
		message = message + "Bitcoin(BTC)."
	elif num == '2':
		# Ethereum (ETH)
		webbrowser.open('https://www.worldcoinindex.com/coin/ethereum')
		message = message + "Ethereum(ETH)."
	elif num == '3':
		# Litecoin (LTC)
		webbrowser.open('https://www.worldcoinindex.com/coin/litecoin')
		message = message + "Litecoin(LTC)."
	elif num == '4':
		# Ripple (XRP?)
		webbrowser.open('https://www.worldcoinindex.com/coin/ripple')
		message = message + "Ripple(XRP)."
	elif num == '5':
		# Eos (EOS)
		webbrowser.open('https://www.worldcoinindex.com/coin/eos')
		message = message + "Eos(EOS)."
	else:
		# Dash (DASH)
		webbrowser.open('https://www.worldcoinindex.com/coin/dash')
		message = message + "Dash(DASH)."
		
	return message
		
	
