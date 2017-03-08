from TransactionManagger import AccountTypes, TransactionManagger
from AccountPrimitives import Account

"""
NOTE for my code:
I used to create a class' main variables before the initialization, because the code will be clearer with this way.
But I cannot declare its types and values, therefore they are not static members of the class
"""

class JokerHMI:
  '''
  Class for interfacing to the core functions, which are:
    - (TM) Transaction Managger
    - .... in future: (IO_parser) DataParser
    - .... in future: (Calc) Evaluation module for calculation trends and future expectations
    - .... in future: (Graph) Visualise the results of Calc module and the current balances
    - .... in future: (WM) Window Manager for creating fancy windowed application from this stuff
  '''
  accounts = []
  """ list of managed accounts"""
  ## Modules
  TM = None # Transaction Managger
  IO_Parser = None # Handle import and export tasks
  Calc = None # Evaluation module
  Graph = None # Plot generator module
  WM = None # Window Manager


  def __init__(self, account_init_dict):
    for dict_element in account_init_dict:
      acc = Account(dict_element,account_init_dict[dict_element])
      self.accounts.append(acc)
      acc = None
    self.TM = TransactionManagger(self.accounts)
    return

  def reqTransaction(self, account_name, change_value, reason_note, trans_type, time, other_note):
    self.TM.doTransaction(account_name=account_name,
                          value=change_value,
                          reason=reason_note,
                          transaction_type=trans_type,
                          time_stamp=time,
                          note=other_note)
    return


