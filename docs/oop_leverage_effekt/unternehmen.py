# unternehmen.py

from bilanz import Bilanz
from erfolgsrechnung import Erfolgsrechnung

class Unternehmen:
    def __init__(self, bilanz, erfolgsrechnung) -> None:
        self.bilanz = bilanz
        self.erfolgsrechnung = erfolgsrechnung
        
        
    def berechne_fk_zinssatz(self):
        '''
        Methode zur Berechnung des durchscnittlichen Fremdkapitalzinssatzes.
        
        Rückgabewert:
            float: Durschnittlicher Zinssatz auf dem verzinslichen FK in Prozenten.
        '''
        verzinsliches_fk = self.bilanz.get_verzinsliches_fk()
        zinsaufwand = self.erfolgsrechnung.get_zinsaufwand()
        return (zinsaufwand/verzinsliches_fk) * 100
    
    def berechne_roi(self):
        '''
        Methode zur Berechnung des RoI.
        
        Rückgabewert:
            float: RoI in Prozenten.
        '''
        ebit = self.erfolgsrechnung.get_ebit()
        gk = self.bilanz.get_gk()
        
        return (ebit/gk) * 100
    
    def berechne_roe(self):
        '''
        Methode zur Berechnung des RoE.
        
        Rückgabewert:
            float: RoE in Prozenten.
        '''
        ek = self.bilanz.get_ek()
        erfolg = self.erfolgsrechnung.get_erfolg()
        
        return (erfolg/ek) * 100