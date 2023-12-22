class Date:
    """
    Eine Klasse, welche Daten nach der Deutschen Usanz zur Verfügung stellt.

    Attribute:
        day (int): Die Nummer des Tages im Monat.
        month (int): Die Nummer des Monats im Jahr.
        year (int): Die Jahreszahl.

    Methoden:
        date_in_days(self): Rechnet das Datum nach der Deutschen Usanz
        in Tage seit dem 1. Januar im Jahr 0 um.
        day_count_date2date(self, other_day): Rechnet die Differenz
        zwischen zwei Daten in Tagen nach der Deutschen Usanz aus.
    """

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.leapyear = self._is_leap_year()
        self._day_normaliser(day)

    def _is_leap_year(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            return True
        else:
            return False

    def _day_normaliser(self, day):
        if self.leapyear and self.month == 2 and self.day == 29:
            self.day = 30
        elif self.month == 2 and self.day == 28:
            self.day = 30
        elif self.day == 31:
            self.day = 30
        else:
            self.day = day

    def date_in_days(self):
        return self.day + (self.month - 1) * 30 + self.year * 360

    def day_count_date2date(self, other_day):
        start = self.date_in_days()
        end = other_day.date_in_days()
        return abs(end - start)

        