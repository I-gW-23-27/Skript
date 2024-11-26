# erfolgsrechnung.py

class Erfolgsrechnung:
    def __init__(self, ertrag, aufwand) -> None:
        self.ertrag = ertrag
        self.aufwand = aufwand
        self.zinsaufwand = None
        
    def get_betrieblicher_ertrag(self):
        pass
    
    def get_bruttoergebnis(self):
        pass
    
    def get_bruttoergebnis_inkl_personal(self):
        pass
    
    def get_ebitda(self):
        pass
    
    def get_ebit(self):
        pass
    
    def get_ebt(self):
        pass
    
    def get_erfolg_vor_steuern(self):
        pass
    
    def get_erfolg(self):
        pass
        
    def get_zinsaufwand(self):
        if self.zinsaufwand == None:
            zinsaufwand = self.aufwand[6900][1]
            self.zinsaufwand = zinsaufwand
            return zinsaufwand
        else:
            return self.zinsaufwand
    
    def set_zinsaufwand(self, zinsaufwand):
        self.zinsaufwand = zinsaufwand