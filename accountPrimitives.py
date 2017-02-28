from datetime import datetime
from enum import Enum

## ENUMS
class TransactionTypes(Enum):
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
  MAIN = 0
  CARD = 1
  CASH = 2
  init = 99

## CLASSES
class Modification:
  change = 0.0
  ''' value of the changing :type: float'''
  reason = ''
  ''' reason of the modification; :type: string'''
  time_stamp = None
  ''' time point of modification; :type: datetime.datetime'''
  modification_type = None
  ''' class of modification. This field sorts the transaction into a larger group of modifications. For example this money was spend for food, clothes etc.
  :type: TransactionTypes enum'''
  note = ''
  ''' some important information about the modification; :type: string'''


class Account:
  name = ''
  ''' name of the account; :type: string'''
  note = ''
  ''' some important information about the account; :type: string'''
  modification_list = []
  ''' store of all modification that is associated to this account; :type: list of Modification objects'''
  balance = 0.0
  ''' balance of this account inf HUF; :type: float'''

  def doModification(self, mod):
    # check the field types

    # append the modification

    # update balance
    return

  def getBalance(self):
    return self.balance

  def getNthTransaction(self, id_of_transaction):
    return

  def getLastTransaction(self):
    return



