import csv
from datetime import datetime

from Input_Parser.parser_bases import Fields_enum, ParseTransaction, ParserBase

## It contains only derived classes of primitives of IO_parsers file

'''
This module is for parsing the csv files that are imported from OTP bank's internal web interface. The parseOTPcsv function
manages the parsing methods. It opens the csv file and gets all interpretable fields and create a list of CSV_Transaction
objects from it



## NOTE: if you want to include or remove a field, you only just follow the next steps:
##    1. modify the Fields_enum enum
##    2. modify the class-variables in the "head" of CSV transaction
##    3. write or delete a parsing method in the CSV_transaction class
##    4. include or remove the correct lines in the init method of the CSV_Transaction class
'''


class OtoCsvParser(ParserBase):
	def __init__(self, file_name=None):
		ParserBase.__init__(self, ParseOTPTransaction)
		
		if file_name is not None:
			self.parse_input_file(file_name)
	
	def parse_input_file(self, file_name):
			
		self.included_file_names.append(file_name)
		with open(file_name, 'r', encoding='utf-8') as file_obj:
			for line in file_obj:
				line_pieces = line.split(';')
				parsed_transaction = ParseOTPTransaction(line_pieces)
				self.transaction_list.append(parsed_transaction)


class ParseOTPTransaction(ParseTransaction):
	
	def __init__(self, csv_line_pieces):
		ParseTransaction.__init__(self)
		self.parse_card_number(csv_line_pieces[Fields_enum.card_number.value])
		self.parse_sign(csv_line_pieces[Fields_enum.sign.value])
		self.parse_change_value(csv_line_pieces[Fields_enum.change.value])
		self.parse_currency(csv_line_pieces[Fields_enum.currency.value])
		self.parse_date_of_realisation(csv_line_pieces[Fields_enum.date_of_realisation.value])
		self.parse_date_of_transaction(csv_line_pieces[Fields_enum.date_of_transaction.value])
		self.parse_new_balance(csv_line_pieces[Fields_enum.balance.value])
		self.parse_note(csv_line_pieces[Fields_enum.note.value])
		self.parse_transaction_name(csv_line_pieces[Fields_enum.transaction.value])
		return
	
	def parse_card_number(self, card_num):
		self.card_number = int(card_num.replace('"', ''))
		return
	
	def parse_sign(self, sign):
		if sign == "T":  # terhelés
			self.sign = -1
		if sign == "J":
			self.sign = 1
		return
	
	def parse_change_value(self, value_string):
		self.change_value = float(value_string)
		return
	
	def parse_currency(self, curr):
		self.currency = curr
		return
	
	def parse_date_of_realisation(self, dateString):
		self.date_of_realization = datetime(year=int(dateString[0:4]),
		                                    month=int(dateString[4:6]),
		                                    day=int(dateString[6:8]))
		return
	
	def parse_date_of_transaction(self, dateString):
		# Some reason the UNIVERSITAS's deposit is different from other transactions :-)
		# thus if this is detected the DateOfTransaction will be equal to DateOfRealisation
		# other exceptions:
		#   - empty field
		#   - hungarian student's loan organization's different fields
		#   - bank dependent "Kamatado" transaction
		if (dateString[1:4] == "UNI") or (dateString == '') or ("hitel" in dateString) or ('Kama' in dateString):
			self.date_of_transaction = self.date_of_realization
		else:
			self.date_of_transaction = datetime(year=int(dateString[1:5]),
			                                    month=int(dateString[6:8]),
			                                    day=int(dateString[9:11]))
		return
	
	def parse_new_balance(self, balanceString):
		self.balance = float(balanceString)
	
	def parse_note(self, string):
		# if exception occurred by hungarian student loan's transaction
		if '967' in string:
			self.note = 'DH'
		else:
			self.note = string
		return
	
	def parse_transaction_name(self, string):
		self.transaction_name = string
		return


###################################################
###################################################
if __name__ == '__main__':
	filename = r'c:\__DATA__\otp_account_history_2019_aug.csv'
	file_parser = OtoCsvParser(filename)
	
	print('muhaha')
