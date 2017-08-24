#------------------------------------------------------
# This function shows the cryptocurrency statistics 
# through the CLI. It uses the BeautifulSoup module
# to parse the HTML, it also uses the requests module 
# to get the document behind the URL.
# Author: Erv
#------------------------------------------------------

import requests
from bs4 import BeautifulSoup

# All tests
def cli_print(coin):
	URL =  'https://worldcoinindex.com/coin/' 
	URL = URL + coin
	req = requests.get(URL)
	soup = BeautifulSoup(req.text, 'html.parser')
	
	price = " "

	for link in soup.find_all('td', {'class': 'coinprice'}):
		price = (link.text.lstrip())

	message = "The price of " + coin.upper() + " is $"  + price
	
	return message
# LOL it works

