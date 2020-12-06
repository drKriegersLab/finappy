from datetime import datetime
from enum import Enum
from TransactionManagers.transaction import Transaction, TransactionTypes

msg_color_warning = '\x1b[1;33;0m'
msg_color_ok = '\x1b[1;30;0m'
msg_color_end = '\x1b[0m'

class AccountTypes(Enum):
	"""
	Enum like Class for storing which account types are specified in this program
	"""
	MAIN = 0
	CARD = 1
	CASH = 2
	init = 99


class Account:
	def __init__(self, acc_name='no name', init_value=0, verbose=False):
		self.name = acc_name
		self.verbose = False
		
		
		self.msg_start("initialize account")
		
		# init the account
		
		self.note = acc_name + " account"
		''' some important information about the account; :type: string'''
		
		self.transaction_list = []
		''' store of all modification that is associated to this account; :type: list of Modification objects'''
		
		self.balance = 0.0
		''' balance of this account inf HUF; :type: float'''
		
		
		self.msg_success()
		self.verbose = verbose
		print("\taccount name: %s" % self.name)
		print("\tnote: %s" % self.note)
		print("\tbalance: {:,.0f}".format(self.balance).replace(',',' '))
	
	def new_transaction(self, transaction):
		if self.verbose: self.msg_start("add new transaction")
		# update balance
		# self.balance += transaction.change
		# transaction.new_balance = self.balance
		transaction.account_name = self.name
		
		# append the modification
		self.transaction_list.append(transaction)
		
		if self.verbose:
			self.msg_success()
			self.msg_common("reason: {:s} | change: {:,d} | type: {:s} | new balance: {:,.0f}".format(transaction.reason,
			                                                                                        transaction.change,
			                                                                                        str(transaction.transaction_type),
			                                                                                        self.balance).replace(',',' '))
		
	
	def add_transaction(self, value, reason, time_stamp, transaction_type, note):
		# create a mod object
		mod = Transaction()
		mod.change = value
		mod.reason = reason
		mod.time_stamp = time_stamp
		mod.modification_type = transaction_type
		mod.note = note
		
		# execute the modification
		self.new_transaction(mod)
		return
		
	def msg_common(self, msg):
		print("[%s account] %s" % (self.name, msg))
		
	def msg_start(self, msg):
		print("[%s account] %s ... " %(self.name, msg), end="")
	
	@staticmethod
	def msg_success():
		print(msg_color_ok + '  [ok]' + msg_color_end)
	
	@staticmethod
	def msg_fail(msg):
		print(msg_color_warning + " [fail]\n\t" + msg)
	
	
	
		
	


if __name__ == '__main__':
	acc0 = Account()
	acc1 = Account('muhaha', 100000)
	acc1.add_transaction(value=-10000,
	                     reason='no reason',
	                     time_stamp=datetime.now(),
	                     transaction_type=TransactionTypes.clothes,
	                     note='')
	tr0 = Transaction()
	tr0.transaction_type = TransactionTypes.entertainment
	tr0.time_stamp = datetime.now()
	tr0.change = 150000
	tr0.reason = 'test'

