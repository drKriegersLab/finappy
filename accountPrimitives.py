import numpy as np
from enum import Enum

en_TransactionTypes = Enum('en_TracnsactionTypes','fees food clothes IT withdrawal deposit culture entertrainment other')

'''
 Primitive class off all types of accounts (for example bank account)
 This class for the managing of balance and transactions of an account.
 It means the keeping account the balances, all transactions, the types of transactions and store some notes from these
 There are the main methods:
    - doTransaction is realize a transaction in the account
    - "get" functions are for acquiring informations about the account
    - printLastTransaction and printNthTransaction for printing informations to the console
    - withdraval and deposit - handling function of withdrawals and depostis. These are abstract methods that are different in differen accounts
'''

class Account():
  """

  TODO:
  balance: type: np.ndarray
  change: list of values of changing
  type: type - list of en_TransactionType enums
  note: type - list of strings -
  """
  balance = np.array([])
  change = np.array([])
  type = []
  note = []

  def __init__(self):
    self.balance = np.append(self.balance, 0)
    self.change = np.append(self.change, 0)
    self.type.append(en_TransactionTypes.other)
    self.note.append('init')
    return


  def doTransaction(self, changeValue, transactionType, otherNote):
    """
    method for realize transactions
    :param changeValue: list of values of changing
    :param transactionType: type - list of en_TransactionType enums -- type of the transaction -
    :param otherNote: type - list of strings --
    :return:
    """
    self.balance = np.append(self.balance, self.balance[len(self.balance) - 1] + changeValue)
    self.change = np.append(self.change, changeValue)
    self.type.append(transactionType)
    self.note.append(otherNote)
    return

  def getActualBalance(self):
    return self.balance[len(self.balance) - 1]

  def getLastTransaction(self):
    return self.balance, self.change, self.type, self.note

  def getNumberOfTransactions(self):
    return len(self.balance)
  def printLastTransaction(self):
    lastID = len(self.balance) - 1
    assert lastID >= 0, "there is no valid transactions in this account"
    print "details of the last transaction:"
    print "\t balance: %d"%self.balance[lastID]
    print "\t change: %d " %self.change[lastID]
    print "\t type: " + self.type[lastID].name
    print "\t note: " + self.note[lastID]

  def printNthTransaction(self, transactionID):
    print "details of the %d. transaction:" %transactionID
    print "\t balance: %d"%self.balance[transactionID]
    print "\t change: %d " %self.change[transactionID]
    print "\t type: " + self.type[transactionID].name
    print "\t note: " + self.note[transactionID]


  def getNthTransaction(self, idOfTransaction):
    assert idOfTransaction < 0 or idOfTransaction > len(self.balance), 'the desired transaction id does not valid'
    return self.balance, self.change, self.type, self.note

  def getMoreTransaction(self, startTransactionID, endTransactionID):
    balances = np.array()
    changes = np.array()
    types = []
    notes = []
    for transaction_id in range(startTransactionID, endTransactionID):
      balance_, change_, type_, note_ = self.getNthTransaction(transaction_id)
      balances = np.append(balances, balance_)
      changes = np.append(changes, change_)
      types = np.append(types, type_)
      notes = np.append(notes, note_)
    return balances, changes, types, notes

  ''' abstract class for handling withdrawals that is depends on the cases '''
  def withdrawal(self):
    return

  ''' abstract class for handling deposit that is depends on the cases'''
  def deposit(self):
    return



if __name__ == '__main__':
  print en_TransactionTypes.fees

  print 'muhaha'