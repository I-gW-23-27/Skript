from date import Date

class Entry:
    """
    Eine Klasse, welche einen Betrag und ein Datum in einem Objekt zusammenfasst.

    Attribute:
        amount (double): Der Betrag eines Konteneintrags. Der Betrag kann auch negativ sein.
        date (Date): Das Datum des Konteneintrags.

    Methoden:
        Ausser dem Konstruktor werden keine Methoden zur Verfügung gestellt.
    """

    def __init__(self, amount, date: Date):
        self.amount = amount
        self.date = date