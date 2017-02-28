from AccountPrimitives import TransactionTypes, AccountTypes

class TransactionManagger():
  ## vars
  accounts = []
  ''' list of accounts; :type: list'''
  balances = {}
  ''' collection of all current balances; :type: dict'''

  def __init__(self, accounts):
    self.accounts = accounts
    self.updateBalances()
    return

  ## meths
  def doTransaction(self, value, reason, account_name, transaction_type, time_stamp, note):
    # get the affected accounts (which ususally will be only one account, except the withdrawal or deposit like transations)
    # and realize the transactions on the accounts

    # withdrawal
    if transaction_type == TransactionTypes.withdrawal:
      # get the money out of the specified account
      for acc in self.accounts:
        if acc.name == account_name:
          acc.doModification(-value, reason, time_stamp, transaction_type, note)

      # put the money into the CASH account
      for acc in self.accounts:
        if acc.name == AccountTypes.CASH.name:
          acc.doModification(value, reason, time_stamp, transaction_type, note)

    # deposit
    if transaction_type == TransactionTypes.deposit:
      # put the balance into the selected account
      for acc in self.accounts:
        if acc.name == account_name:
          acc.doModification(value,reason, time_stamp, transaction_type, note)
      # remove the balance from the CASH account
      for acc in self.accounts:
        if acc.name == AccountTypes.CASH.name:
          acc.doModification(-value,reason,time_stamp,transaction_type,note)
    # if the required transaction is not a deposit or withdrawal, just modify the specified account
    if not ((transaction_type == TransactionTypes.deposit) or (transaction_type == TransactionTypes.withdrawal)):
      for acc in self.accounts:
        if acc.name == account_name:
          acc.doModification(value,reason,time_stamp,transaction_type, note)

    # update balances
    self.updateBalances()
    return

  def updateBalances(self):
    self.balances = {}
    for acc_id in range(len(self.accounts)):
      self.balances[self.accounts[acc_id].name] = self.accounts[acc_id].balance
    return

  def getBalances(self):
    return self.balances

