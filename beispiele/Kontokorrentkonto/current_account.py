from balance_sheet_account import BalanceSheetAccount
from entry import Entry
from date import Date

class CurrentAccount(BalanceSheetAccount):
    def __init__(self, asset_interest, debt_interest, initial_amount, initial_date):
        super().__init__(initial_amount, initial_date)
        self.asset_interest = asset_interest
        self.debt_interest = debt_interest
        self.current_saldo = [initial_amount]
        self.interests = [0]

    def add_entry(self, entry):
        self.entries.append(entry)
        saldo = 0
        for i in range(len(self.entries)):
            saldo += self.entries[i].amount
        self.current_saldo.append(saldo)

        max_index = len(self.entries) - 1
        d1 = self.entries[max_index].date
        d2 = self.entries[max_index - 1].date
        days = d1.day_count_date2date(d2)

        money = self.entries[max_index-1].amount
        interest = 0
        if money >= 0:
            interest = ((money * self.asset_interest) / 360) * days
        else:
            interest = ((money * self.debt_interest) / 360) * days
        self.interests.append(interest)

    def inter_date_interest(self, start_date: Date, end_date: Date):
        start = start_date.date_in_days()
        end = end_date.date_in_days()
        entries_in_days = []
        for i in range(len(self.entries)):
            entries_in_days.append(self.entries[i].date.date_in_days())

        lower_bound = 0
        for index, wert in enumerate(entries_in_days):
            if start <= wert:
                lower_bound = index
            else:
                break

        upper_bound = 0
        for index, wert in enumerate(entries_in_days):
            if end > wert:
                upper_bound = index

        inner_interest = 0
        for i in range(lower_bound, upper_bound):
            inner_interest += self.interests[i]


        lower_saldo = self.current_saldo[lower_bound]

        lower_margin = 0
        if lower_saldo >= 0:
            lower_margin = lower_saldo * self.asset_interest / 360 * abs(start - entries_in_days[lower_bound])
        else:
            lower_margin = lower_saldo * self.debt_interest / 360 * abs(start - entries_in_days[lower_bound])

        upper_saldo = self.current_saldo[upper_bound]

        upper_margin = 0
        if upper_saldo >= 0:
            upper_margin = upper_saldo * self.asset_interest / 360 * abs(end - entries_in_days[upper_bound])
        else:
            upper_margin = upper_saldo * self.debt_interest / 360 * abs(end - entries_in_days[upper_bound])



        return inner_interest + lower_margin + upper_margin


