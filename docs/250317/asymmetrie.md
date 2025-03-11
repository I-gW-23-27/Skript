# Public-Key-Kryptographie

Obwohl es grundsätzlich möglich ist, mit dem One-Time-Pad eine sichere
Verschlüsselung zu realisieren, ist dieses Verfahren in der Realität kaum
praktikabel. Neben der Tatsache, dass der Schlüssel mindestens so lang sein
muss, wie die Nachricht selbst, braucht es ein Verfahren den, bzw. die Schlüssel
sicher zwischen Sender und Empfänger zu teilen.

Um das Problem des Schlüsselaustausches zu lösen, verwendet man spezielle
mathematische Funktionen. Diese Funktionen nennt man "Einwegfunktionen mit
Hintertüren". Eine Einwegfunktion $f(x) = x'$ lässt sich leicht berechnen, aber
ihre Umkehrung $f^{-1}(x') = x$ ist sehr schwierig zu berechnen. Die "Hintertür"
ist ein Geheimwissen, mit dem die Umkehrfunktion dann doch einfach berechnet
werden kann.

Die Einwegfunktion kann veröffentlicht werden, damit ein Absender mit deren
Hilfe eine Botschaft verschlüsseln kann. Nur der Empfänger ist dann noch in der
Lage, die Botschaft mit wenig Aufwand zu entschlüsseln. Allfällige 'Lauscher'
können die Umkehrfunktion nicht innert nützlicher Frist berechnen.

Weil Text als Zahlenfolge dargestellt werden kann, eignen sich mathematische
Funktionen besonders gut für die Verschlüsselung von Texten. Im folgenden soll
ein Modell für ein solches Verschlüsselungsverfahren vorgestellt werden.

## Verschlüsselung mit Hilfe eines Graphen

Ein Graph besteht aus Knoten und Kanten. Die Knoten sind durch Kanten
miteinander verbunden. Damit die Verschlüsselung mit Hilfe eines Graphen
erfolgen kann, muss der Graph öffentlich bekannt und die Knoten Nummeriert sein.
Die Verschlüsselung erfolgt in den unten dargestellten Schritten.

1. Der Klartext wird als Folge von Zahlen dargestellt, welche folgendermassen
   verschlüsselt werden:
2. Die einzelnen Zahlen der Zahlenfolge werden in Summanden zerlegt. Die Zahl
   der Summanden entspricht der Anzahl der Knoten im Graphen.
3. Jeder Summand wird einem Knoten zugeordnet.
4. Der 'Wert' eines Knotens berechnet sich als Summe des dem Knoten zugeordneten
   Summanden und allen Summanden der Nachbarknoten.
5. Der verschlüsselte Wert der Zahl ist die Folge der Werte der Knoten.

Das Vorgehen soll an einem Beispiel verdeutlicht werden. Dem Beispiel liegt der
folgende Graph zu Grunde.

![](graph0.svg)

In diesem Graphen wird die Zahl 999 verschlüsselt. Die Aufteilung in Summanden
sieht folgendermassen aus:

$$
999 = 0 + 77 + 39 + 123 + 264 + 96 + 133 + 67 + 200
$$

Die Summanden werden folgendermassen in den Graphen eingetragen:

![](graph1.svg)

Nach der Addition der Nachbarn, stellt sich der Graph folgendermassen dar:

![](graph2.svg)

Der verschlüsselte Wert kann jetzt als Zahlenfolge
123/570/229/426/827/770/306/570/627 übermittelt werden.
