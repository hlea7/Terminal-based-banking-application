from FileManager import FileManager
from HistoryMessages import HistoryMessages

class Account:
    def __init__(self, balance = 0):
        self.balance = balance
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        # the dictionary from hist_dict is added to hist.json    
        return self.file_manager.add_to_json(hist_dict, self.hist_file_path) 

    def deposit(self, amount):
        try:
            amount = int(amount)
            # amount must be a integer greater than 0
            if amount > 0:
                self.balance += amount
                # in case of a positive outcome, write it to a JSON file
                history_message = HistoryMessages.deposit("success", amount, self.balance)                
            else:
                # in case of a negative outcome, write to the JSON file
                history_message = HistoryMessages.deposit("failure", amount, self.balance)
                print('Invalid amount for deposit!')
        except ValueError:            
            history_message = HistoryMessages.deposit("failure", amount, self.balance)
            print("Invalid amount for deposit!")   
        self.write_to_history(history_message) 
        

    def debit(self, amount):
        try:
            amount = int(amount)
            # amount must be a integer greater than 0
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                # in case of positive outcome write to JSON file                
                history_message = HistoryMessages.debit("success", amount, self.balance)
            else:
                # in case of a negative outcome, write to a JSON file
                # if amount is greater than the amount in the account (insufficient funds) the operation should not work
                history_message = HistoryMessages.debit("failure", amount, self.balance)
                print("Invalid amount for debit!") 
        except ValueError:
            history_message = HistoryMessages.debit("failure", amount, self.balance)
            print('Invalid amount for debit!')
        self.write_to_history(history_message)
    

    def get_balance(self):
        return self.balance

    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
        else:
            return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'
        

    def get_history(self):
        # returns transaction history line by line using the dict_to_string method to create a string from a dictionary
        transaction_history_data = self.file_manager.read_json(self.hist_file_path)
        transaction_history_lines = ""
        for dict_data in transaction_history_data:
            if dict_data == transaction_history_data[0]:
                transaction_history_lines += f"-- {self.dict_to_string(dict_data)} --"
            else:
                transaction_history_lines += f"\n-- {self.dict_to_string(dict_data)} --"
        return transaction_history_lines