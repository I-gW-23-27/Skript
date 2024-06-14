from pytamaro.de import (
    ellipse, rechteck, text,
    schwarz, rgb_farbe,
    ueberlagere, fixiere, kombiniere,
    oben_links, oben_rechts, unten_links, unten_mitte,
    zeige_grafik, Grafik,
)

class Node:
    
    
    def __init__(self, key, value=None, parent=None, left=None, right=None):
        self.key    = key
        self.value  = value
        self.parent = parent
        self.left   = left
        self.right  = right
        
    def draw(self):
        circle = ellipse(22, 22, schwarz)
        background = ellipse(20, 20, rgb_farbe(50, 255, 255))
        key = text(str(self.key), "arial", 12, schwarz)
        node = ueberlagere(key, ueberlagere(background, circle))
        zeige_grafik(node)
        