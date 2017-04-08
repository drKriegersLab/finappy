from HMI.JokerTheHMI import JokerHMI
from TransactionManagers.TransactionManagger import AccountTypes
from datetime import datetime

'''
acc_init_dict = {}
acc_init_dict[AccountTypes.CASH.name] = " CASH account"
acc_init_dict[AccountTypes.CARD.name] = "this is the CARD's account"

HMI = JokerHMI(acc_init_dict)
HMI.reqTransaction(AccountTypes.CASH.name, +10000, 'test', TransactionTypes.culture,datetime.now(), 'init other note')

HMI.reqTransaction(AccountTypes.CARD.name, +5000, 'deposit 5000 HUF', TransactionTypes.deposit, datetime.now(), 'note for deposit' )
HMI.reqTransaction(AccountTypes.CARD.name, 3000, 'get 3000 HUF from the card', TransactionTypes.withdrawal, datetime.now(), 'note for withdrawal')
'''

filenames = ['BankAccountSources/2016_12.csv','BankAccountSources/2017_01.csv','BankAccountSources/2017_02.csv','BankAccountSources/2017_03.csv']
'''
csv_tr_list = []

for file_name in filenames:
    parseOTPcsv(file_name, csv_transactions=csv_tr_list)

'''
acc_init_values = {AccountTypes.CASH.name: 0,
                   AccountTypes.CARD.name: 403527}

HMI = JokerHMI(acc_init_values)
#HMI.reqTransaction(AccountTypes.CASH.name, +10000, 'test', TransactionTypes.culture,datetime.now(), 'init other note')
HMI.loadTransactionsFromCsv(filenames)

trs = HMI.Calc.selTrsInInterval(AccountTypes.CARD.name, datetime(2017,03,9), datetime(2017,03,12))
bals = HMI.Calc.getChangesOfTrs(trs)

print "muhaha"

