from account import Account
from entry import Entry

class BalanceSheetAccount(Account):
    def __init__(self, initial_amount, initial_date):
        self.entries = [Entry(initial_amount, initial_date)]
