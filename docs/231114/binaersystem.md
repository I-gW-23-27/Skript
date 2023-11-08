# Das Binärsystem

Das dezimale Zahlensystem ist allen vertraut. Dabei hat man sehr früh im
Schulunterricht gelernt, dass jede Zahl zwei Werte zum Ausdruck bringt -
einerseits den Wert der Ziffer und andererseits den Wert der Stelle.
Anhand der Zahl 127 soll das illustriert werden.

$$127 = 7 \cdot 1 + 2 \cdot
10 + 1 \cdot 100 = 7 \cdot 10^0 + 2 \cdot 10^1 + 1 \cdot 10^2$$

Genau gleich funktioniert das Binärsystem. Dabei wird lediglich mit der
Basis $2$ gerechnet. Als Beispiel dient hier die Binärzahl 101010.

$$101010 = 0 \cdot 2^0 + 1 \cdot 2^1 + 0 \cdot 2^2 + 1 \cdot 2^3 + 0
\cdot 2^4 + 1 \cdot 2^5 = 2 + 8 + 32 = 42$$

Um eine Dezimalzahl in eine Binärzahl umzurechnen, geht man
folgendermassen vor:

- die Dezimalzahl wird modulo ($mod$) zwei gerechnet
- das Resultat der Modulorechnung (0 oder 1) wird auf die Stelle rechts neben der letzten
  eingetragenen Stelle eingetragen
- die Dezimalzahl wird ganzzahlig ($div$) durch zwei geteilt
- das Resultat ist die neue Dezimalzahl

Dieses vorgehen wird solange wiederholt, bis das Resultat der
ganzzahligen Division Null ist.

Als Beispiel nehmen wir wiederum die Dezimalzahl 42.

$$42 mod 2 = 0 \rightarrow 0$$

$$42 div 2 = 21$$

$$21 mod 2 = 1 \rightarrow 10$$

$$21 div 2 = 10$$

$$10 mod 2 = 0 \rightarrow 010$$

$$10 div 2 = 5$$

$$5 mod 2 = 1 \rightarrow 1010$$

$$5 div 2 = 2$$

$$2 mod 2 = 0 \rightarrow 01010$$

$$2 div 2 = 1$$

$$1 mod 2 = 1 \rightarrow 101010$$

$$1 div 2 = 0$$

Die Beschreibung der Vorgehensweise für die Umrechnung der Dezimalzahl
in eine Binärzahl ist ein Algorithmus.