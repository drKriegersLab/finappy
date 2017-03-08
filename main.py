from JokerTheHMI import JokerHMI
from TransactionManagger import AccountTypes, TransactionManagger, TransactionTypes
from datetime import datetime
acc_init_dict = {}
acc_init_dict[AccountTypes.CASH.name] = " CASH account"
acc_init_dict[AccountTypes.CARD.name] = "this is the CARD's account"

HMI = JokerHMI(acc_init_dict)
HMI.reqTransaction(AccountTypes.CASH.name, +10000, 'test', TransactionTypes.culture,datetime.now(), 'init other note')

HMI.reqTransaction(AccountTypes.CARD.name, +5000, 'deposit 5000 HUF', TransactionTypes.deposit, datetime.now(), 'note for deposit' )
HMI.reqTransaction(AccountTypes.CARD.name, 3000, 'get 3000 HUF from the card', TransactionTypes.withdrawal, datetime.now(), 'note for withdrawal')

print "muhaha"

