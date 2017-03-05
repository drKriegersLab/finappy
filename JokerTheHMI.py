from TransactionManagger import AccountTypes, TransactionManagger
from AccountPrimitives import Account

class JokerHMI:
  accounts = []
  TM = None

  def __init__(self, account_init_dict):
    for dict_element in acc_init_dict:
      acc = Account(dict_element,acc_init_dict[dict_element] )
      self.accounts.append(acc)

    self.TM = TransactionManagger(self.accounts)
    return

  def reqTransaction(self):
    return


if __name__ == '__main__':
  # TODO: check the modifications
  acc_init_dict = {}
  acc_init_dict[AccountTypes.CASH.name] = " CASH account"
  acc_init_dict[AccountTypes.CARD.name] = "this is the CARD's account"

  hmi = JokerHMI(acc_init_dict)

  print "muhaha"
