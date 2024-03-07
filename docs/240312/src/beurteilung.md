# Beurteilung von Algorithmen

Die Effizienz eines Algorithmus kann grundsätzlich nach seinem
Rechenaufwand oder Speicherbedarf beurteilt werden. Man spricht in
diesem Zusammenhang auch von Zeit- bzw. Platzkomplexität.

Die entsprechenden Überlegungen sollen am Beispiel von Selection Sort
illustriert werden.

## Zeitkomplexität

Die Zeitkomplexität eines Algorithmus misst sich in der Anzahl der
erforderlichen Rechenoperationen. Im Beispiel Selection Sort ist ein
Rechenschritt der Vergleich eines Elements der zu vergleichenden Sequenz
\- im weiteren Textverlauf einfach als Sequenz bezeichnet - mit einem
anderen Element in der Sequenz. Selection Sort erfordert, dass jedes
Element der Sequenz mit jedem anderen Element verglichen werden muss.
Das ergibt bei einer Sequenz der Länge $n$ $n^2$ Vergleiche. Das heisst,
der Rechenaufwand von Selection Sort steigt quadratisch im Verhältnis
der Anzahl zu sortierenden Element.
