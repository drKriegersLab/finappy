from enum import Enum
from datetime import datetime


## FIELDS ENUM
class Fields_enum(Enum):
	card_number = 0
	sign = 1
	change = 2
	currency = 3
	date_of_realisation = 4
	date2 = 5
	balance = 6
	field1 = 7
	field2 = 8
	note = 9
	field3 = 10
	date_of_transaction = 11
	transaction = 12
	field4 = 13


class ParserBase:
	"""
	this class encapsulates all classes and functions that are assigned to reading a specific file type and getting
	transaction	information out of it.
	It contains two parts:
		1. static like class for handling input parser tasks for each transactions
		2. function that uses this class for create object instances of parsed transactions
	"""
	
	def __init__(self, input_parser):
		self.InputParser = input_parser
		self.included_file_names = []
		self.transaction_list = []
	
	def parse_input_file(self, file_name, transaction_list):
		return


class ParseTransaction:
	"""
	Class for parsing transactions from CSV lines
	"""
	
	def __init__(self):
		self.card_number = 0  # the number of mentioned card
		self.sign = 0  # -1 or +1, which represents that this transaction is a deposit or a withdrawal
		self.change_value = 0  # the value of changing
		self.currency = ''  # represents the currency of the change (for example HUF)
		self.date_of_transaction = datetime(1, 1, 1)  # the date when the transaction has been done
		self.date_of_realization = datetime(1, 1, 1)  # when appeared the transaction on the account
		self.balance = 0  # the new balance after the transaction
		self.note = ''  # the important notes for the transaction
		self.transaction_name = ''  # the type of the transaction
		return
	
	def parse_card_number(self, card_num):
		raise NotImplementedError
	
	def parse_sign(self, sign):
		raise NotImplementedError
	
	def parse_change_value(self, value_string):
		raise NotImplementedError
	
	def parse_currency(self, curr):
		raise NotImplementedError
	
	def parse_date_of_realisation(self, dateString):
		raise NotImplementedError
	
	def parse_date_of_transaction(self, dateString):
		raise NotImplementedError
	
	def parse_new_balance(self, balanceString):
		raise NotImplementedError
	
	def parse_note(self, string):
		raise NotImplementedError
	
	def parse_transaction_name(self, string):
		raise NotImplementedError
