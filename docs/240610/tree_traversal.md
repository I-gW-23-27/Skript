# Tree Traversal

Beim Tree Traversal geht es darum jeden Knoten in einem Baum zu
Besuchen. Mit Besuchen ist gemeint, dass mit dem Knoten etwas geschieht
\- zum Beispiel die Ausgabe der Knoten oder das Update der in
den Knoten abgelegten Files.

Um alle Knoten zu besuchen gibt es verschiedene Vorgehensweisen.
Grundsätzlich wird unterschieden zwischen Tiefen- und Breitensuche.

## Tiefensuche

In der Tiefensuche wird im Baum soweit nach unten gegangen, bis der
unterste Knoten eines Astes erreicht wird. Erst danach werden die Knoten
rechts besuch. Die unstenstehende Animation soll dies veranschaulichen.

<figure>
    <img src="./images/Depth-First-Search.gif" alt="Tiefensuche">
    <figcaption>Quelle: https://en.wikipedia.org/wiki/Depth-first_search</figcaption>
</figure>

Um eine Tiefensuche durchzuführen sind folgende Operationen auf jeden
besuchten Knoten anzuwenden:

1. Wenn der aktuelle Knoten leer ist `return`.
2. Die folgenden drei Operationen sind auf jeden Knoten anzuwenden. Die
   Reihenfolge der Operationen ist von der Variante der Tiefensuche
   abhängig (vgl. Unten).
   * N: Den aktuellen Knoten besuchen.
   * L: Rekursiv den linken Teilbaum des aktuellen Knotens durchlaufen.
   * R: Rekursiv den rechten Teilbaum des aktuellen Knotens durchlaufen.

Die Reihenfolge der besuchten Knoten wird als Sequenzialisierung des
Baums bezeichnet. Dabei gibt es drei Varianten der Sequenzialisierung:

* Pre-order (NLR)
  1. Den aktuellen Knoten besuchen.
  2. Rekursiv den linken Teilbaum des aktuellen Knotens durchlaufen.
  3. Rekursiv den rechten Teilbaum des aktuellen Knotens durchlaufen.
* Post-order (LRN)
  1. Rekursiv den linken Teilbaum des aktuellen Knotens durchlaufen.
  2. Rekursiv den rechten Teilbaum des aktuellen Knotens durchlaufen.
  3. Den aktuellen Knoten besuchen.
* In-order (LNR)
  1. Rekursiv den linken Teilbaum des aktuellen Knotens durchlaufen.
  2. Den aktuellen Knoten besuchen.
  3. Rekursiv den rechten Teilbaum des aktuellen Knotens durchlaufen.

Die untenstehende Grafik bildet die drei Varianten ab:

<figure>
    <img src="./images/Sorted_binary_tree_ALL_RGB.svg" alt="Visualisierung Tiefensuche">
    <figcaption>
    Tiefensuche in einem Binärbaum (gestrichelter Pfad):
    
    Pre-order (der Knoten wird beim roten Punkt besucht):  

                F, B, A, D, C, E, G, I, H;  

                In-order (der Knoten wird beim grünen Punkt besucht):  

                A, B, C, D, E, F, G, H, I;  

                Post-order (der Knoten wird beim blauen Punkt besucht):

                A, C, E, D, B, H, I, G, F.

                Quelle: https://en.wikipedia.org/wiki/Tree_traversal#Depth-first_search
    </figcaption>
</figure>