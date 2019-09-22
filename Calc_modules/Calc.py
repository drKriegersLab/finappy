class Calc:
	
	@staticmethod
	def get_all_changes_from_transactions(tr_list):
		"""
		collect all balance data from the given transaction list into an array
		:param tr_list: list of transactions
		:return: array of balances
		"""
		changes = []
		for tr_id in range(len(tr_list)):
			changes.append(tr_list[tr_id].change)
		return changes
	
	@staticmethod
	def get_all_balances_from_transactions(tr_list):
		"""
		collect all balance data from the given transaction list into an array
		:param tr_list: list of transactions
		:return: array of balances
		"""
		balances = []
		for tr_id in range(len(tr_list)):
			balances.append(tr_list[tr_id].new_balance)
		return balances
	
	@staticmethod
	def get_all_reasons_from_transactions(tr_list):
		"""
		collect all reason information from the given transaction list into an array
		:param tr_list: list of transactions
		:return: array of reason information
		"""
		reasons = []
		for tr_id in range(len(tr_list)):
			reasons.append(tr_list[tr_id].reason)
		return reasons
	
	@staticmethod
	def get_all_time_stamps_from_trs(tr_list):
		"""
		collect all time stamp data from the given transaction list into an array
		:param tr_list: list of transactions
		:return: array of time stamps
		"""
		time_stamps = []
		for tr_id in range(len(tr_list)):
			time_stamps.append(tr_list[tr_id].time_stamp)
		return time_stamps
	
	@staticmethod
	def get_all_mod_types_from_transactions(tr_list):
		"""
		collect all modification type information from the given transaction list into an array
		:param tr_list: list of transactions
		:return: array of modification types
		"""
		mod_types = []
		for tr_id in range(len(tr_list)):
			mod_types.append(tr_list[tr_id].modification_type)
		return mod_types
	
	@staticmethod
	def get_all_notest_from_transactions(tr_list):
		"""
		collect all note from the given transaction list into an array
		:param tr_list: list of transactions
		:return: array of notes
		"""
		notes = []
		for tr_id in range(len(tr_list)):
			notes.append(tr_list[tr_id].note)
		return notes
	
	## METHODS
	
	def select_transactions_from_interval(self, account, start_date, end_date):
		"""
		Method for getting all transactions between the specified time interval
		:param transaction_manager: give the transaction manager, which encapsulates all used accounts
		:param account_name: which account is examined
		:param start_date: the first transaction's date in the result collection must be greater than this
		:param end_date: the last transaction's date in the result collection must be less or equal with this
		:return: an array of collected transactions
		"""
		transactions = []
		
		account = None
		first_tr_id = None
		last_tr_id = None
		
		# get the first transaction ID in the specified time interval
		for tr_id in range(1, len(account.modification_list)):
			if account.modification_list[tr_id].time_stamp > start_date:
				first_tr_id = tr_id
				break
		
		# get the last transaction ID in the specified time interval
		if first_tr_id is not None:
			for tr_id in range(first_tr_id, len(account.modification_list)):
				if (tr_id > 1) and (account.modification_list[tr_id].time_stamp.date() > end_date.date()):
					last_tr_id = tr_id - 1
					break
		if (last_tr_id is None) and len(account.modification_list) > 0:
			last_tr_id = len(account.modification_list) - 1
		
		# iterating over all transaction between the selected two ID
		if first_tr_id < last_tr_id:
			for tr_id in range(first_tr_id, last_tr_id):
				transactions.append(account.modification_list[tr_id])
		return transactions
