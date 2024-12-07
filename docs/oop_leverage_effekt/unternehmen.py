# unternehmen.py

import csv

from bilanz import Bilanz
from erfolgsrechnung import Erfolgsrechnung

class Unternehmen:
    def __init__(self, konti = {}) -> None:
        if len(konti) == 0:
            self.bilanz = Bilanz()
            self.erfolgsrechnung = Erfolgsrechnung()
        else:
            self.bilanz = Bilanz()
            self.erfolgsrechnung = Erfolgsrechnung()
            self.bilanz.set_konti(konti)
            self.erfolgsrechnung.set_konti(konti)
        
        
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
    
    def save_data(self):
        with open('data.csv', mode='w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)  # Übergabe des Dateiobjekts an csv.writer
            
            # Kopfzeile schreiben
            writer.writerow(['KtoNr', 'Kto', 'Saldo'])
            
            # Daten schreiben
            for ktonr, kto in self.bilanz.aktiven.items():
                writer.writerow([ktonr, kto[0], kto[1]])
                
            for ktonr, kto in self.bilanz.passiven.items():
                writer.writerow([ktonr, kto[0], kto[1]])
                
            for ktonr, kto in self.erfolgsrechnung.aufwand.items():
                writer.writerow([ktonr, kto[0], kto[1]])
            
            for ktonr, kto in self.erfolgsrechnung.ertrag.items():
                writer.writerow([ktonr, kto[0], kto[1]])
                
            