from Input_Parser.InputParser_OTPcsvReader import InputInterfaceOTP
from TransactionManagers.AccountPrimitives import Account, TransactionTypes
from TransactionManagers.TransactionManagger import AccountTypes, TransactionManagger

"""
NOTE for my code:
I used to create a class' main variables before the initialization, because the code will be clearer with this way.
But I cannot declare its types and values, therefore they are not static members of the class
"""

class JokerHMI:
  '''
  Class for interfacing to the core functions, which are:
    - (TM) Transaction Manager
    - (InputInterface) Interface for different input files that will parse data from databases
    - .... in future: (IO_DataManager) Interface for load or save database and calculated data.
    - .... in future: (Calc) Evaluation module for calculation trends and future expectations
    - .... in future: (Graph) Visualise the results of Calc module and the current balances
    - .... in future: (WM) Window Manager for creating fancy windowed application from this stuff
  '''
  accounts = []
  """ list of managed accounts"""
  ## Modules
  TM = None # Transaction Manager
  InputInterface = None # Handler of import tasks
  Calc = None # Evaluation module
  Graph = None # Plot generator module
  WM = None # Window Manager


  def __init__(self, account_init_dict):
    # create accounts
    for dict_element in account_init_dict:
      acc = Account(dict_element,account_init_dict[dict_element])
      self.accounts.append(acc)
      acc = None

    # assign the case-specific classes
    self.TM = TransactionManagger(self.accounts)
    self.InputInterface = InputInterfaceOTP()
    return

  def reqTransaction(self, account_name, change_value, reason_note, trans_type, time, other_note):
    self.TM.doTransaction(account_name=account_name,
                          value=change_value,
                          reason=reason_note,
                          transaction_type=trans_type,
                          time_stamp=time,
                          note=other_note)
    return

  def loadTransactionsFromCsv(self, csv_filenames):
    csv_tr_list = []
    # parsing of input file
    for file_name in csv_filenames:
      self.InputInterface.inputParserFcn(file_name, transaction_list=csv_tr_list)

    for tr_num in range(len(csv_tr_list)):
      tr_record = csv_tr_list[tr_num]
      self.reqTransaction(account_name=AccountTypes.CARD.name,
                          change_value=tr_record.change_value,
                          reason_note=tr_record.note,
                          trans_type=TransactionTypes.other,
                          time=tr_record.date_of_transaction,
                          other_note='')

    return

