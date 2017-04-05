import numpy as np


class Calc:
  def __init__(self, TM):
    self.TM = TM
    # it's maybe nasty solution a bit, but with this way this module can access the TM module at every time without the calling of it
    return

  def selTrsInInterval(self, account_name, start_date, end_date):
    '''
    Method for getting all transactions between the specified time interval
    :param account_name: which account is examined
    :param start_date: the first transaction's date in the result collection must be greater than this
    :param end_date: the last transaction's date in the result collection must be less or equal with this
    :return: an array of collected transactions
    '''
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

  def calcBalances(self, account_name, start_date, end_date):
    mod_ids = []
    balances = []
    # get all changes from desired interval
    # sum them
    return mod_ids, balances




