#-----------------------------------------------------------------
# The main application. This is what needs to be run to run the 
# full application. Calls 6 function from 6 different script files.
# Author: Erv
#------------------------------------------------------------------

from welcome import welcome_func
from discrete import discrete_calculate
from continuous import continuous_calculate
from int_calc_selector import select_calculator
from cryptocurrency import crypt_peep
from crypto_web import crypt_receive
from crypto_cli import cli_print
from crypto_cliselect import  select_coin

 # call welcome.py 
selector_1 = welcome_func()
display = " "

if selector_1 == "Q":
	# User wants to view cyptocurrency website
	# call cryptocurrency.py
	q_select = crypt_peep()
	
	# pass logic from previous function to crypto_web.py
	display = crypt_receive(q_select)
elif selector_1 == 'W':
	# User wants to view cryptocurrency 
	# through the CLI.
	coin_str = " "
	w_select = crypt_peep()
	coin_str = select_coin(w_select)
	display = cli_print(coin_str)
	
else:
	# User wants to use interest calculators
	# call int_calc_selector.py
	selector_2 = select_calculator()
	if selector_2 == "D":
		# User wants to use discrete calculators
		# call discrete.py
		display = discrete_calculate()
	else:
		# User wants to use continuous calculators
		# call continuous.py
		display = continuous_calculate()

# display 
print(display)


