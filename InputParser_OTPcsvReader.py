import csv
from aenum import Enum
from datetime import datetime
from Input_Parser_Primitives import Fields_enum, InputParserPrimitive, InputInterfacePrimitive


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

## DERIVED CLASS OF IO_Parser_Primitive  FOR OTP SPECIFIC PARSING
class InputInterfaceOTP(InputInterfacePrimitive):
  def __init__(self):
    self.InputParser = InputParserOTP

  def inputParserFcn(self, fileName, transaction_list=[]):
    fileObj = open(fileName)

    csvObj = csv.reader(fileObj)

    csvLines = []
    field = []
    fields = {}
    # csv_transactions = []
    for row in csvObj:
      fieldNum = 0
      fields = {}
      field = []
      for character in row[0]:  # the 0-th element of the row is the container of string array
        # fill each fields. The separator between they is semicolon
        if not character == ';':
          field.append(character)
        else:
          fields[Fields_enum(fieldNum).name] = ''.join(field)
          fieldNum += 1
          field = []

      tr = self.InputParser(**fields)
      transaction_list.append(tr)

    return transaction_list


## DERIVED CLASS OF INPUT PARSER
class InputParserOTP(InputParserPrimitive):

  def __init__(self, **kwargs):
    InputParserPrimitive.__init__(self, **kwargs)

    if Fields_enum.card_number.name in kwargs:
      self.parseCardNumber(kwargs[Fields_enum.card_number.name])
    if Fields_enum.sign.name in kwargs:
      self.parseSign(kwargs[Fields_enum.sign.name])
    if Fields_enum.change.name in kwargs:
      self.parseChangeValue(kwargs[Fields_enum.change.name])
    if Fields_enum.currency.name in kwargs:
      self.parseCurrency(kwargs[Fields_enum.currency.name])
    if Fields_enum.date_of_realisation.name in kwargs:
      self.parseDateOfRealisation(kwargs[Fields_enum.date_of_realisation.name])
    if Fields_enum.date_of_transaction.name in kwargs:
      self.parseDateOfTransaction(kwargs[Fields_enum.date_of_transaction.name])
    if Fields_enum.balance.name in kwargs:
      self.parseNewBalance(kwargs[Fields_enum.balance.name])
    if Fields_enum.note.name in kwargs:
      self.parseNote(kwargs[Fields_enum.note.name])
    if Fields_enum.transaction.name in kwargs:
      self.parseTransactionName(kwargs[Fields_enum.transaction.name])

    return

  def parseCardNumber(self, card_num):
    self.card_number = int(card_num)
    return

  def parseSign(self, sign):
    if sign == "T": #terheles
      self.sign = -1
    if sign == "J":
      self.sign = 1

    return

  def parseChangeValue(self, value_string):
    self.change_value = float(value_string)
    return

  def parseCurrency(self, curr):
    self.currency = curr
    return

  def parseDateOfRealisation(self, dateString):
    self.date_of_realization = datetime(year=int(dateString[0:4]),
                                             month=int(dateString[4:6]),
                                             day=int(dateString[6:8]))
    return

  def parseDateOfTransaction(self, dateString):
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

  def parseNewBalance(self, balanceString):
    self.balance = float(balanceString)

  def parseNote(self, string):
    # if exception occurred by hungarian student loan's transaction
    if '967' in string:
      self.note = 'DH'
    else:
      self.note = string
    return

  def parseTransactionName(self, string):
    self.transaction_name = string
    return





###################################################
###################################################
if __name__ == '__main__':
  filename = 'bank_cvs.csv'
  parseOTPcsv(filename)
  print 'muhaha'





