from entry import Entry

class Account:
    def __init__(self):
        self.entries = []
        self.saldo = 0.0

    def add_entry(self, entry):
        self.entries.append(entry)

    def calculate_saldo(self):
        saldo = 0
        for entry in self.entries:
            saldo = saldo + entry.amount

        self.saldo = saldo