# Merge Sort

Die allgemein Idee bei Merge Sort ist das Zusammenführen (engl. to
merge) von zwei bereits sortierten Sequenzen. Um dies möglichst einfach 



**Ziel**: Sortierung einer Sequenz von \(n\) Elementen in aufsteigender Reihenfolge durch rekursive Teilung und Fusionierung.

**Eingabe**: Eine Sequenz von \(n\) Elementen \(A[1 \ldots n]\).

**Ausgabe**: Eine permutierte Ordnung von \(A\) in aufsteigender Reihenfolge.

#### Schritt 1: Teilen

1. Definiere \(n\) als die Länge der Sequenz \(A\).
2. Wenn \(n \leq 1\), ist die Sequenz bereits sortiert. Terminiere den Algorithmus.
3. Andernfalls teile \(A\) in zwei Hälften \(A_1[1 \ldots \lfloor n/2 \rfloor]\) und \(A_2[\lfloor n/2 \rfloor + 1 \ldots n]\).

#### Schritt 2: Erobern

4. Wende Merge Sort rekursiv auf \(A_1\) und \(A_2\) an.

#### Schritt 3: Kombinieren

5. Fusioniere die sortierten Sequenzen \(A_1\) und \(A_2\) zu einer einzigen sortierten Sequenz \(A'\).
   - Initialisiere drei Zeiger \(i\), \(j\), und \(k\) auf die Anfänge von \(A_1\), \(A_2\), und \(A'\) entsprechend.
   - Wiederhole, solange \(A_1\) und \(A_2\) Elemente enthalten:
     - Wenn \(A_1[i] \leq A_2[j]\), füge \(A_1[i]\) zu \(A'\) hinzu und erhöhe \(i\) und \(k\).
     - Andernfalls, füge \(A_2[j]\) zu \(A'\) hinzu und erhöhe \(j\) und \(k\).
   - Füge verbleibende Elemente von \(A_1\) oder \(A_2\) zu \(A'\) hinzu.

#### Schritt 4: Resultat

6. Ersetze \(A\) mit \(A'\) als die sortierte Sequenz.

### Analyse

- **Zeitkomplexität**:
  - Im besten, mittleren und schlechtesten Fall: \(O(n \log n)\), wobei \(n\) die Länge der Eingabesequenz ist.
- **Raumkomplexität**: \(O(n)\), aufgrund der Notwendigkeit, zusätzliche Sequenzen für die Fusionierungsschritte zu speichern.

**Bemerkungen**:
Merge Sort demonstriert das Divide-and-Conquer-Paradigma mit optimaler Zeitkomplexität für eine Vielzahl von Anwendungsfällen. Trotz seiner optimalen Laufzeit erfordert der Algorithmus zusätzlichen Speicherplatz, was bei der Bewertung seiner Anwendbarkeit berücksichtigt werden sollte.

---

Diese Beschreibung nutzt die Möglichkeiten von GitHub Flavored Markdown, um eine klare und strukturierte Darstellung des Merge Sort Algorithmus im Stil von Donald E. Knuth zu bieten.