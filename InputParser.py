import csv
from aenum import Enum
import datetime
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


class Fields_enum(Enum):
  card_number = 0
  sign = 1
  change = 2
  currency = 3
  date_of_realisation = 4
  date2 = 5
  num1 = 6
  field1 = 7
  field2 = 8
  note = 9
  field3 = 10
  date_of_transaction = 11
  transaction = 12
  field4 = 13



class CSV_Transaction:
  fields = None
  card_number = None # the number of mentioned card
  sign = None # -1 or +1, which represents that this transaction is a deposit or a withdrawal
  change_value = None # the value of changing
  currency = None # represents the currency of the change (for example HUF)
  date_of_realization = None # when was the transaction
  date_of_transaction = None # when appeared the transaction on the account
  note = None # the important notes for the transaction
  transaction_name = None # the type of the transaction

  def __init__(self, **kwargs):

    #assert len(kwargs) == len(Fields_enum), "not enough input fields!"
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
    if Fields_enum.note.name in kwargs:
      self.parseNote(kwargs[Fields_enum.note.name])
    if Fields_enum.transaction.name in kwargs:
      self.parseTransactionName(kwargs[Fields_enum.transaction.name])

    #for key, item in kwargs.iteritems():
      #print '%s : %s'%(key, item)

    return

  def parseCardNumber(self, card_num):


    self.card_number = int(card_num)
    return

  def parseSign(self, sign):
    if sign == "T": #terheles
      self.sign = -1
    if sign == "J":
      self.sign = -1

    return

  def parseChangeValue(self, value_string):
    self.change_value = float(value_string)
    return

  def parseCurrency(self, curr):
    self.currency = curr
    return

  def parseDateOfRealisation(self, dateString):
    self.date_of_realization = datetime.date(year=int(dateString[0:4]),
                                             month=int(dateString[4:6]),
                                             day=int(dateString[6:8]))
    return

  def parseDateOfTransaction(self, dateString):
    # Some reason the UNIVERSITAS'es deposit is different from other transactions :-)
    # thus if this is detected the DateOfTransaction will be equal to DateOfRealisation
    if (dateString[1:4] == "UNI") or (dateString == ''):
      self.date_of_transaction = self.date_of_realization
    else:
      self.date_of_transaction = datetime.date(year=int(dateString[1:5]),
                                               month=int(dateString[6:8]),
                                               day=int(dateString[9:11]))
    return

  def parseNote(self, string):
    self.note = string
    return

  def parseTransactionName(self, string):
    self.transaction_name = string
    return





def parseOTPcsv(fileName):
  fileObj = open(fileName)

  csvObj = csv.reader(fileObj)

  csvLines = []
  field = []
  fields = {}
  csv_transactions = []
  for row in csvObj:
    fieldNum = 0
    fields = {}
    field = []
    for character in row[0]: # the 0-th element of the row is the container of string array
      # fill each fields. The separator between they is semicolon
      if not character == ';':
        field.append(character)
      else:
        fields[Fields_enum(fieldNum).name] = ''.join(field)
        fieldNum += 1
        field = []

    tr = CSV_Transaction(**fields)
    csv_transactions.append(tr)

  return csv_transactions



###################################################
###################################################

filename = 'bank_cvs.csv'
parseOTPcsv(filename)
print 'muhaha'





