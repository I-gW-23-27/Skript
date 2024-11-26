# bilanz.py

class Bilanz:
    def __init__(self, aktiven, passiven):
        self.aktiven  = aktiven
        self.passiven = passiven
        
    def get_verzinsliches_fk(self):
        # TODO: implementieren einer Methode, welche das verzinsliche FK zurückgibt
        verzinsliches_fk = {}
        for kto_nr, value in self.passiven.items():
            if kto_nr >= 2400 and kto_nr < 2500:
                verzinsliches_fk[kto_nr] = value
                
                      
        total_verzinsliches_fk = 0
        
        for kto_nr, value in verzinsliches_fk.items():
            total_verzinsliches_fk += value[1]
        
        return total_verzinsliches_fk
    
    def get_ek(self):
        # TODO: implementieren einer Methode, welche das EK zurückgbit
        pass