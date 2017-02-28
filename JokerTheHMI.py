from TransactionManagger import AccountTypes
from AccountPrimitives import Account

class JokerHMI:
  accounts = []

  def __init__(self, account_init_dict):
    for dict_element in acc_init_dict:
      acc = Account(dict_element,acc_init_dict[dict_element] )
      self.accounts.append(acc)

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
