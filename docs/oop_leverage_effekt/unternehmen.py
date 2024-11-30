# unternehmen.py

from bilanz import Bilanz
from erfolgsrechnung import Erfolgsrechnung

class Unternehmen:
    def __init__(self, bilanz, erfolgsrechnung) -> None:
        self.bilanz = bilanz
        self.erfolgsrechnung = erfolgsrechnung
        
        
    def berechne_fk_zinssatz(self):
        verzinsliches_fk = self.bilanz.get_verzinsliches_fk()
        zinsaufwand = self.erfolgsrechnung.get_zinsaufwand()
        return (zinsaufwand/verzinsliches_fk) * 100