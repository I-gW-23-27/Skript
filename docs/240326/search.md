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
    Durchsucht sequenziell ein gegebenes Array und gibt den Index
    des gesuchten Wertes zurück.

    Parameter:
    seq (list): Die Liste oder das Array, in dem gesucht wird.
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

## Binäre Suche

Daten zu sortieren ist eine Vorarbeit um effizienter suchen zu können.
Der Aufwand für die Sortierung lohnt sich allerdings nur, wenn mehrfach
nach einem Datum gesucht werden muss.