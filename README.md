##This is Python Terminal-based banking application.

Its goal is to provide users with convenient and secure access to basic operations with their bank accounts through a terminal interface implemented with special attention to error handling and user-friendliness. 

Application implements an intuitive terminal interface with prompts for available commands where users are able to select Basic Account Operations:

#View Balance
#Deposit Funds
#Withdraw Funds
#View Transaction History
#Currency Exchange

by entering the corresponding command numbers.

When depositing funds and during withdrawal application validates the correctness of the provided amount and the attempt is added to history file. In case of incorrect input values, error message about Invalid amount is displayed. Additionally, check for sufficient funds in the account is implemented.

When viewing the transaction history, the history from a JSON file is read and displayed line by line in the terminal.

For currency exchange, application obtains data for conversion via HTTP request from API server. In case of an incorrectly specified value from the user, displays the message "Currency exchange failed!".

Logging is implemented for deposit, withdrawal, and currency exchange operations.

Class for the account with relevant properties (balance, transaction history) and methods (deposit, withdrawal, get balance) and currency exchange class with currency rates and methods for currency exchange and rate updates (using network requests) are implemented.