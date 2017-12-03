#!env/bin/python3
# Price Ticker
# Gets current cryptocurrency prices from GDAX

import json
import requests
import os

class priceTicker():

	def __init__(self):
		pass

	def validateCurrency(self, currency):

		if (currency.lower() == 'ltc'):
			# print('Litecoin')
			return True
		elif (currency.lower() == 'btc'):
			# print('Bitcoin')
			return True
		elif (currency.lower() == 'eth'):
			# print('Ethereum')
			return True
		else:
			# print('Unknown currency')
			return False

	def getCurrentPrice(self, currency):

		url = 'https://api.gdax.com/products/{}-USD/ticker'.format(currency.upper())

		if self.validateCurrency(currency) != True:
			return None

		response = requests.get(url)
		if response.status_code == 200:
			#print(response.json())
			currentPrice = response.json()['price'][:-6]
			# print('Price: {}'.format(currentPrice))
			return currentPrice

		else: 
			print(reponse.status_code)
			return None

	def convertCurrency(self, fromCurrency, toCurrency):

		if fromCurrency != 'USD' || fromCurrency != 'CAD':
			print('Unsupported currency you are converting FROM.')
			return None

		if toCurrency != 'USD' || toCurrency != 'CAD':
			print('Unsupported currency you are converting TO.')
			return None

		