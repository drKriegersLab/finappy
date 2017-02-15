import accountPrimitives as am

account = am.Account()
account.doTransaction(12,am.en_TransactionTypes.deposit,'note')

print "actual balance:"
print account.getActualBalance()

print "last transaction:"
print account.getLastTransaction()

account.printLastTransaction()

account.doTransaction(10,am.en_TransactionTypes.other,'this is an other transaction')
account.doTransaction(-5,am.en_TransactionTypes.IT,'I bought a new analpiszkator')

account.printLastTransaction()
for i in range(account.getNumberOfTransactions()):
  account.printNthTransaction(i)

