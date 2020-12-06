import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from TransactionManagers.account_otp_csv_interface import InterfaceOtpCsvToAccount
import matplotlib.dates as mdates
import numpy as np


years = mdates.YearLocator()
months = mdates.MonthLocator()
days = mdates.DayLocator()
years_fmt = mdates.DateFormatter('%b')

filenames = [r'c:\__DATA__\otp_account_history_2018_10.csv',
             r'c:\__DATA__\otp_account_history_2018_11.csv',
             r'c:\__DATA__\otp_account_history_2018_12.csv',
             r'c:\__DATA__\otp_account_history_2019_01.csv',
             r'c:\__DATA__\otp_account_history_2019_02.csv',
             r'c:\__DATA__\otp_account_history_2019_03.csv',
             r'c:\__DATA__\otp_account_history_2019_04.csv',
             r'c:\__DATA__\otp_account_history_2019_05.csv',
             r'c:\__DATA__\otp_account_history_2019_06.csv',
             r'c:\__DATA__\otp_account_history_2019_07.csv',
             r'c:\__DATA__\otp_account_history_2019_08.csv',
             r'c:\__DATA__\otp_account_history_2019_09.csv' ]

otp_csv_interface = InterfaceOtpCsvToAccount(filenames)
account = otp_csv_interface.account

balances = []
timestamps = []

income_transactions = []
income_balances = []
income_timestamps = []

bigger_expense_transactions = []
expense_balances = []
expense_timestamps = []

for transaction in account.transaction_list:
	balances.append(transaction.new_balance)
	timestamps.append(transaction.time_stamp)
	
	if transaction.change < -20000:
		bigger_expense_transactions.append(transaction)
		expense_balances.append(transaction.new_balance)
		expense_timestamps.append(transaction.time_stamp)
		
	if transaction.change > 0:
		income_transactions.append(transaction)
		income_balances.append(transaction.new_balance)
		income_timestamps.append(transaction.time_stamp)
	
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(timestamps, balances)
sc_all = ax.scatter(timestamps, balances, 10, c='black')
sc_income = ax.scatter(income_timestamps, income_balances, c='green')
ax.plot(expense_timestamps, expense_balances, 'X', markeredgecolor='red')
ax.grid(axis='x', which='major')
ax.grid(axis='y')

annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
names = balances
norm = plt.Normalize(1,4)
cmap = plt.cm.RdYlGn


def update_annot(ind):

    pos = sc_all.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    indices = ind['ind']
    text = ''
    for index in indices:
		    
	    text = text + " date: " + account.transaction_list[index].time_stamp.strftime("%d. %b")
	    text = text + " | change: " + "{:,d} Ft".format(int(account.transaction_list[index].change)).replace(","," ")
	    text = text + " | balance: " + "{:,d} Ft".format(int(account.transaction_list[index].new_balance)).replace(",", " ")
	    text = text + "\n   | " + account.transaction_list[index].reason
	    text = text + "   | " + account.transaction_list[index].note
	    if len(indices) > 1 and index != indices[-1]:
		    text = text + "\n"
    
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor('green')
    annot.get_bbox_patch().set_alpha(0.8)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc_all.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()
			    
fig.canvas.mpl_connect("motion_notify_event", hover)
    

ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(days)


labels = []

for item in ax.get_yticks():
	label = "{:,d} Ft".format(int(item)).replace(",", " ")
	labels.append(label)
ax.set_yticklabels(labels)
print(labels)
plt.show()
