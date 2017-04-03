from aenum import Enum
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

class InputInterfacePrimitive:
  """
  this class encapsulate all classes and functions that are assigned to reading a specific file type and getting transaction
  information out of it.

  It contains two parts:
    1. static like class for handling input parser tasks for each transactions
    2. function that uses this class for create object instances of parsed transactions
  """
  InputParser = None

  def inputParserFcn(self, fileName, transaction_list=[]):
    return


## INPUT PARSER ABSTRACT CLASS
class InputParserPrimitive:
  card_number = None  # the number of mentioned card
  sign = None  # -1 or +1, which represents that this transaction is a deposit or a withdrawal
  change_value = None  # the value of changing
  currency = None  # represents the currency of the change (for example HUF)
  date_of_realization = None  # when was the transaction
  date_of_transaction = None  # when appeared the transaction on the account
  balance = None  # the new balance after the transaction
  note = None  # the important notes for the transaction
  transaction_name = None  # the type of the transaction

  def __init__(self, **kwargs):

    self.card_number = 0
    self.sign = 0
    self.change_value = 0
    self.date_of_transaction = datetime(1,1,1)
    self.date_of_realization = datetime(1,1,1)
    self.balance = 0
    self.note = ''
    self.transaction_name = ''

    return

  ''' abstract classes '''

  def parseCardNumber(self, card_num):
    return

  def parseSign(self, sign):
    return

  def parseChangeValue(self, value_string):
    return

  def parseCurrency(self, curr):
    return

  def parseDateOfRealisation(self, dateString):
    return

  def parseDateOfTransaction(self, dateString):
    return

  def parseNewBalance(self, balanceString):
    return

  def parseNote(self, string):
    return

  def parseTransactionName(self, string):
    return
