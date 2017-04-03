from JokerTheHMI import JokerHMI
from TransactionManagger import AccountTypes, TransactionManagger, TransactionTypes

'''
acc_init_dict = {}
acc_init_dict[AccountTypes.CASH.name] = " CASH account"
acc_init_dict[AccountTypes.CARD.name] = "this is the CARD's account"

HMI = JokerHMI(acc_init_dict)
HMI.reqTransaction(AccountTypes.CASH.name, +10000, 'test', TransactionTypes.culture,datetime.now(), 'init other note')

HMI.reqTransaction(AccountTypes.CARD.name, +5000, 'deposit 5000 HUF', TransactionTypes.deposit, datetime.now(), 'note for deposit' )
HMI.reqTransaction(AccountTypes.CARD.name, 3000, 'get 3000 HUF from the card', TransactionTypes.withdrawal, datetime.now(), 'note for withdrawal')
'''

filenames = ['2016_12.csv','2017_01.csv','2017_02.csv','2017_03.csv']
'''
csv_tr_list = []

for file_name in filenames:
    parseOTPcsv(file_name, csv_transactions=csv_tr_list)

'''
acc_init_dict = {}
acc_init_dict[AccountTypes.CASH.name] = " CASH account"
acc_init_dict[AccountTypes.CARD.name] = " CARD account"

HMI = JokerHMI(acc_init_dict)
#HMI.reqTransaction(AccountTypes.CASH.name, +10000, 'test', TransactionTypes.culture,datetime.now(), 'init other note')
HMI.loadTransactionsFromCsv(filenames)


print "muhaha"

