from TransactionManagers.account import Account
from Input_Parser.parser_otp_csv import OtpCsvParser
from TransactionManagers.transaction import Transaction, TransactionTypes

class InterfaceOtpCsvToAccount:
	
	def __init__(self, file_names):
		self.file_names = file_names
		self.account = None
		
		self.channel_file_data_to_account()
		
	def channel_file_data_to_account(self):
		parser = OtpCsvParser()
		for file in self.file_names:
			parser.parse_input_file(file)
			
		init_balance = parser.transaction_list[0].balance
		self.account = Account(acc_name='OTP bank YX',
		                       init_value=init_balance)
		for parsed_transaction in parser.transaction_list:
			transaction = Transaction(change=parsed_transaction.change_value,
			                          new_balance=parsed_transaction.balance,
			                          reason=parsed_transaction.transaction_name,
			                          time_stamp=parsed_transaction.date_of_realization,
			                          trans_type=TransactionTypes.other,
			                          note=parsed_transaction.note)
			self.account.new_transaction(transaction)
			
			

	
		
		
