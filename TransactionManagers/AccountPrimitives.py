from datetime import datetime
from aenum import Enum ## TODO: check this import. in windows it is working with enum name, in linux it is working with aenum name



## ENUMS
class TransactionTypes(Enum):
  """
  Enum like Class for store some specified classes of transactions for sorting.
  """
  incoming= 0
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

class AccountTypes(Enum):
  """
  Enum like Class for storing which account types are specified in this program
  """
  MAIN = 0
  CARD = 1
  CASH = 2
  init = 99

## STRUCTS
class Modification:
  """
  Structure like Class that is encapsulate the modifications
  """
  change = 0.0
  ''' value of the changing
  :type: float'''
  new_balance = 0.0
  ''' the new value of account
  :type: float'''
  reason = ''
  ''' reason of the modification
  :type: string'''
  time_stamp = None
  ''' time point of modification
  :type: datetime.datetime'''
  modification_type = None
  ''' class of modification. This field sorts the transaction into a larger group of modifications. For example this money was spend for food, clothes etc.
  :type: TransactionTypes enum'''
  note = ''
  ''' some important information about the modification
  :type: string'''

## CLASSES

class Account:
  """
  Primitive class of all accounts and its main managing methods
  """
  name = None
  ''' name of the account; :type: string'''
  __note = None
  ''' some important information about the account; :type: string'''
  modification_list = None
  ''' store of all modification that is associated to this account; :type: list of Modification objects'''
  balance = None
  ''' balance of this account inf HUF; :type: float'''

  def __init__(self, acc_name, init_value):
    # create the first modification
    first_mod = Modification()
    first_mod.change = float(init_value)
    first_mod.reason = 'init'
    first_mod.time_stamp = datetime.now()
    first_mod.modification_type = TransactionTypes.init
    first_mod.note = acc_name + " account"

    # init the account
    self.name = acc_name
    self.note = acc_name + " account"
    self.modification_list = []
    self.balance = 0.0
    self.doModification(first_mod)
    return

  def doModification(self, mod):
    # check the field types
    assert (type(mod.change) == float) or (type(mod.change) == int), "[%s account] The content of modification's name field is not float or int"%self.name
    assert type(mod.reason) == str, "[%s account] The content of reason field in the modification is not string"%self.name
    assert type(mod.time_stamp) == datetime, "[%s account] The value in the time_stamp field of the modification is not a datetime format"%self.name
    assert type(mod.modification_type) == TransactionTypes, "[%s account] The value in the modification_type field of the modification is not in valid format"%self.name
    assert type(mod.note) == str, "[%s account] The value in the note field is not a string"%self.name
    # update balance
    self.balance += mod.change
    mod.new_balance = self.balance
    # append the modification
    self.modification_list.append(mod)
    return

  def createModification(self, _value, _reason, _time_stamp, _transaction_type, _note):
    # create a mod object
    mod = Modification()
    mod.change = _value
    mod.reason = _reason
    mod.time_stamp = _time_stamp
    mod.modification_type = _transaction_type
    mod.note = _note

    # execute the modification
    self.doModification(mod)
    return



