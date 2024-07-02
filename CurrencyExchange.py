from requests import get
from FileManager import FileManager
from HistoryMessages import HistoryMessages

class CurrencyExchange:
    def __init__(self, balance = 0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        # the dictionary from hist_dict is added to hist.json    
        return self.file_manager.add_to_json(hist_dict, self.hist_file_path)

    def get_exchange_rates(self):
        # sends a get request to the link and returns the resulting dictionary
        response = get("https://fake-api.apps.berlintech.ai/api/currency_exchange")
        return response.json()
    
    def exchange_currency(self, currency_from, currency_to, amount):
        # transfers the specified amount from currency `currency_from` 
        # to currency `currency_to` and, if positive, returns the amount in the new currency  
        try:
            amount = int(amount)
            if amount > 0:
                dict_exchange = self.get_exchange_rates()
                if currency_from in dict_exchange and currency_to in dict_exchange and (currency_from == "EUR" or currency_to == "EUR"):                    
                    converted_amount = amount / dict_exchange[currency_from]
                    # with a positive outcome, the record of history looks like this 
                    history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
                    self.write_to_history(history_message)
                    return converted_amount
                else:
                    # in case of a negative outcome, the history entry looks like this
                    # - if currency_from or currency_to is specified incorrectly
                    history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
                    self.write_to_history(history_message)
                    print("Currency exchange failed!")
                    return None
            else:
                history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
                self.write_to_history(history_message)
                print("Currency exchange failed!")
                return None
        except ValueError:
            # - if amount is not a number 
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            print("Currency exchange failed!")
            return None