import numpy as np


class Calc:

  ## INIT
  def __init__(self, TM):
    self.TM = TM
    # it's maybe nasty solution a bit, but with this way this module can access the TM module at every time without the calling of it
    return

  ## STATIC METHODS

  @staticmethod
  def getChangesOfTrs(tr_list):
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
  def getBalancesOfTrs(tr_list):
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
  def getReasonsOfTrs(tr_list):
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
  def getTimeStampsOfTrs(tr_list):
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
  def getModTypesOfTrs(tr_list):
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
  def getNotesOfTrs(tr_list):
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

  def selTrsInInterval(self, account_name, start_date, end_date):
    """
    Method for getting all transactions between the specified time interval
    :param account_name: which account is examined
    :param start_date: the first transaction's date in the result collection must be greater than this
    :param end_date: the last transaction's date in the result collection must be less or equal with this
    :return: an array of collected transactions
    """
    transactions = []
    # get the account
    acc = None # account
    first_tr_id = None
    last_tr_id = None

    for id in range(len(self.TM.accounts)):
      if self.TM.accounts[id].name == account_name:
        acc = self.TM.accounts[id]

    # get the first transaction ID in the specified time interval
    for tr_id in range(1, len(acc.modification_list)):
      if acc.modification_list[tr_id].time_stamp > start_date:
        first_tr_id = tr_id
        break

    # get the last transaction ID in the specified time interval
    if not first_tr_id == None:
      for tr_id in range(first_tr_id, len(acc.modification_list)):
        if (tr_id > 1) and (acc.modification_list[tr_id].time_stamp.date() > end_date.date()):
          last_tr_id = tr_id-1
          break
    if (last_tr_id == None) and len(acc.modification_list) > 0:
      last_tr_id = len(acc.modification_list) -1

    # iterating over all transaction between the selected two ID
    if first_tr_id < last_tr_id:
      for tr_id in range(first_tr_id, last_tr_id):
        transactions.append(acc.modification_list[tr_id])
    return transactions







