from enum import Enum
from datetime import datetime

class TransactionTypes(Enum):
	"""
	Enum like Class for store some specified classes of transactions for sorting.
	"""
	incoming = 0
	fees = 1
	food = 2
	clothes = 3
	IT = 4
	withdrawal = 5
	deposit = 6
	culture = 7
	entertainment = 8
	other = 9
	init = 99


class Transaction:
	def __init__(self, account_name='', change=0, new_balance=0, reason='', time_stamp=datetime.now(),
	             trans_type=TransactionTypes.init, note=''):
		
		# init properties
		self.__change = 0
		''' value of the changing :type: float'''
		
		self.__new_balance = 0.0
		''' the new value of an account :type: float'''
		
		self.__reason = ''
		''' reason of the modification :type: string'''
		
		self.__time_stamp = None
		''' time point of modification :type: datetime.datetime'''
		
		self.__transaction_type = None
		''' class of modification. This field sorts the transaction into a larger group of modifications.
			For example this money was spend for food, clothes etc.
			:type: TransactionTypes enum'''
		self.__note = ''
		''' some important information about the modification :type: string'''
		
		# use given parameters
		self.account_name = account_name
		self.change = change
		self.new_balance = new_balance
		self.reason = reason
		self.time_stamp = time_stamp
		self.transaction_type = trans_type
		self.note = note
		return
	
	def get_change(self):
		return self.__change
	
	def set_change(self, value):
		assert (type(value) == float) or (type(value) == int), \
			"[%s account] The content of transaction's change field is not a float or an int" % self.account_name
		self.__change = value
	
	def get_new_balance(self):
		return self.__new_balance
	
	def set_new_balance(self, value):
		assert (type(value) == float) or (type(value) == int), \
			"[%s account] The content of transaction's change field is not a float or an int" % self.account_name
		self.__new_balance = value
	
	def get_reason(self):
		return self.__reason
	
	def set_reason(self, value):
		assert (type(value) == str), \
			"[%s account] The content of transaction's reason field is not a string" % self.account_name
		self.__reason = value
	
	def get_time_stamp(self):
		return self.__time_stamp
	
	def set_time_stamp(self, value):
		assert (type(value) == datetime), \
			"[%s account] The content of transaction's time stamp field is not a datetime" % self.account_name
		self.__time_stamp = value
		
	def get_transaction_type(self):
		return self.__transaction_type
	
	def set_transaction_type(self, value):
		assert (type(value) == TransactionTypes), \
			"[% account] The content of transactio's transaction type is not correct" % self.account_name
		self.__transaction_type = value
	
	def get_note(self):
		return self.__note
	
	def set_note(self, value):
		assert (type(value) == str), \
			"[%s account] The content of transaction's note field is not a string" % self.account_name
		self.__note = value
	
	change = property(get_change, set_change)
	new_balance = property(get_new_balance, set_new_balance)
	reason = property(get_reason, set_reason)
	time_stamp = property(get_time_stamp, set_time_stamp)
	note = property(get_note, set_note)
	transaction_type = property(get_transaction_type, set_transaction_type)


if __name__ == '__main__':
	tr0 = Transaction()
	print("new balance: " + str(tr0.new_balance))
	print("change: " + str(tr0.change))
	print("reason: " + str(tr0.reason))
	print("time_stamp: " + str(tr0.time_stamp))
	print("transaction_type: " + str(tr0.transaction_type))
	print("note: " + str(tr0.note))
	tr0.new_balance = 100
	tr0.change = 10
	tr0.reason = 'test'
	tr0.time_stamp = datetime.now()
	tr0.transaction_type = TransactionTypes.deposit
	tr0.note = 'mehehe'
	print("new balance: " + str(tr0.new_balance))
	print("change: " + str(tr0.change))
	print("reason: " + str(tr0.reason))
	print("time_stamp: " + str(tr0.time_stamp))
	print("transaction_type: " + str(tr0.transaction_type))
	print("note: " + str(tr0.note))
	
	tr1 = Transaction(account_name='test account',
	                  new_balance=200,
	                  change=-1,
	                  reason='test reason',
	                  time_stamp=datetime.now(),
	                  trans_type=TransactionTypes.clothes,
	                  note='test note')
	
	print("new balance: " + str(tr1.new_balance))
	print("change: " + str(tr1.change))
	print("reason: " + str(tr1.reason))
	print("time_stamp: " + str(tr1.time_stamp))
	print("transaction_type: " + str(tr1.transaction_type))
	print("note: " + str(tr1.note))
	
	
