from TransactionManagers.account_otp_csv_interface import InterfaceOtpCsvToAccount

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


otp_interface = InterfaceOtpCsvToAccount(filenames)
account = otp_interface.account

print('muhaha')
