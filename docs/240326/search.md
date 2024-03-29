# Suchen

Ein bestimmtes Datum in einer Datensammlung zu suchen, ist eine immer
wieder vorkommende Aufgabe in der Informatik. Es gibt daher auch eine
Vielzahl an Suchalgorithmen. Zwei davon sollen hier vorgestellt werden.

## Lineare Suche

Mit der linearen Suche wird über eine Sequenz von Daten iteriert, bis
das gesuchte Element gefunden wird oder das Ende der Sequenz erreicht
ist. Die lineare Suche ist in Python sehr einfach zu realisieren:

```Python
def linear_search(seq, x):
    """
    Durchsucht sequenziell eine gegebene Liste und gibt den Index
    des gesuchten Wertes zurück.

    Parameter:
    seq (list): Die Liste, in der gesucht wird.
    x: Der Wert, nach dem in der Liste gesucht wird.

    Rückgabewert:
    int: Der Index des gesuchten Wertes in der Liste. Gibt -1 zurück, 
    wenn der Wert nicht in der Liste gefunden wird.

    Beispiel:
    >>> linear_search([1, 2, 3, 4], 3)
    2
    >>> linear_search(['a', 'b', 'c'], 'd')
    -1
    """
    index = 0
    for datum in seq:
        if datum = x:
            return index
        index += 1
    return -1
```

Die lineare Suche ist sehr einfach. Allerdings wächst der Suchaufwand
proportional zur Länge der zu durchsuchenden Sequenz. Der Algorithmus
der binären Suche beschreibt eine Suche, bei welcher der Suchaufwand
weniger schnell ansteigt.

## Binäre Suche

Grundlage für die binäre Suche ist eine Sequenz sortierter Daten.

Eine sortierte Sequenz kann durchsucht werden, in dem als erstes der
mittlere Wert der Sequenz mit dem gesuchten Wert verglichen wird. Ist
der gesuchte Wert kleiner als dieser mittlere Wert, dann ist die Suche
in der linken Hälfte der Sequenz fortzusetzen, ist der Wert grösser, in
der rechten Hälfte. In der entsprechenden Hälfte wird wieder der
mittlere Wert mit dem gesuchten Wert verglichen und dann entweder links
oder rechts von diesem Wert weiter gesucht. Dieses vorgehen wird so
lange fortgesetzt, bis entweder der gesuchte Wert gefunden wird oder
kein Wert zum vergleichen mehr übrig ist.

### Formale Beschreibung[^1]

**Algorithmus B** (*Binäre Suche*). Gegeben eine Sequenz von
Daten $D_1, D_2, ..., D_N$ mit Schlüsseln in aufsteigender Reihenfolge
$K_1 < K_2 < \cdots < K_N$, sucht der Algorithmus nach einem Schlüssel
$K$. 

**B1.** [Initialisierung.] Setze $lo \leftarrow 0$, $hi \leftarrow N-1$.

**B2.** [Mitte ermitteln.] Falls $lo > hi$ endet der Algorithmus ohne
Treffer. Andernfalls entspricht die ungefähre Mitte $mid \leftarrow
\lfloor(lo + hi)/2\rfloor$.

**B3.** [Vergleiche.] Falls $K < K_{mid}$ gehe zu B4; falls $K> K_{mid}$
gehe zu B5. Falls $K=K{mid}$ endet der Algorithmus erfolgreich.

**B4.** [Passe $hi$ an.] Setze $hi \leftarrow mid - 1$ und gehe zu B2.

**B5.** [Passe $lo$ an.] Setze $lo \leftarrow mid + 1$ und gehe zu B2.

### Flussdiagramm des Algorithmus

![Flow Chart Binary Search](./images/binary_search_flow_chart.svg)

### Iterative Implementierung in Python

```Python
def binary_search(seq, x):
    """
    Führt eine binäre Suche in einem sortierten Array durch und gibt 
    den Index des gesuchten Wertes zurück. 

    Parameter:
    seq (list): Das sortierte Array, in dem die Suche durchgeführt wird.
    x: Der zu suchende Wert.

    Rückgabewert:
    int: Der Index des gesuchten Wertes in `seq`. Gibt -1 zurück, wenn 
    der Wert nicht im Array gefunden wird.

    Anmerkungen:
    - Die Funktion erwartet, dass `seq` bereits sortiert ist.
    - Die Suche ist effizient, da sie die Liste in jeder Iteration halbiert.
    - Falls `x` mehrfach in `seq` vorkommt, wird der Index einer 
      der Instanzen von `x` zurückgegeben.

    Beispiel:
    >>> binary_search([1, 2, 3, 4, 5], 3)
    2
    >>> binary_search([1, 2, 4, 5], 3)
    -1
    """
    index = -1
    lo = 0
    hi = len(seq) - 1

    while lo < hi:
        middle = (lo + hi) // 2
        if x == seq[middle]:
            return middle
        elif x < seq[middle]:
            hi = (lo + middle) // 2
        else:
            lo = (middle + hi) // 2 + 1

    return index

```

### Effizienz der binären Suche

Da die binäre Suche den Suchbereich bei jedem gescheiterten Versuch
halbiert, braucht es maximal $\lfloor log_2(n) + 1 \rfloor$ Vergleiche,
um festzustellen, ob der gesuchte Wert in der durchsuchten Sequenz vorkommt.

[^1]: Die Beschreibung des Algorithmus ist eine Übersetzung aus: Knuth,
    Donald Ervin, The Art of Computer Programming (Sorting and
    Searching), 3. Aufl., Band 3, Reading, Mass: Addison-Wesley, 1997,
    Seite 410.
