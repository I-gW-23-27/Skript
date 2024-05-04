# Der binäre Suchbaum

## Bäume in der Informatik

<figure>
  <img src="./tree.png" alt="Christmas Tree">
  <figcaption>Quelle: xkcd.com/835, besucht am 4. Mai 24</figcaption>
</figure>



Ein Baum in der Informatik ist eine Datenstruktur die aus Knoten (engl.
Vertex bzw. vertices, V) und Kanten (engl. edge, E) besteht. Der erste
Knoten ist die Wurzel (engl. root). Alle anderen Knoten haben einen
Knoten als Elternknoten. Ein Elternknoten kann ein oder mehrere
Kindknoten haben. Ein Knoten ohne Kinder wird als Blatt bezeichnet.
Üblicherweise werden Bäume vom Wurzelknoten aus nach unten dargestellt.

![Beispielbaum](./bsp_tree.svg)

## Binärbäume

Ein Binärbaum ist ein Baum, bei dem ein Elternknoten maximal zwei
Kindknoten hat.

![Binärbaum](./binary_tree.svg)

## Binärer Suchbaum

Ein binärer Suchbaum ist ein Binärbaum, bei dem der linke Kindknoten
einen Wert kleiner oder gleich dem Wert des Wurzelknotens und der rechte
Kindknoten einen Wert grösser oder gleich dem Wert des Wurzelknotens
hat.

![Binärer Suchbaum](bst_ex.svg)

Binäre Suchbäume haben zwei wichtige Eigenschaften:

1. Binäre Suchbäume stellen eine schnelle Suche zur Verfügung.
2. Der Aufwand neue Elemente einzufügen bzw. bestehende Elemente zu
   entfernen ist klein.

