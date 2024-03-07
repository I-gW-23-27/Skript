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
anderen Element in der Sequenz. Bei Selection Sort besteht ein
Rechenschritt aus dem Vergleich zweier Elemente der Sequenz. 
Das ergibt bei einer Sequenz der Länge $n$ $\frac{n(n-1)}{2}$
Vergleiche. Der Einfachheit halber konzentriert man sich für die
Beurteilung der Zeitkomplexität auf jenen Teil des Rechenaufwandes, der
in Abhängigkeit der Inputgrösse am stärksten zunimmt. Wenn
$\frac{n(n-1)}{2}$ ausmultipliziert wird, erhält man $\frac{1}{2}n^2 -
\frac{1}{2}$. Das am stärksten wachsende Element in in diesem Term ist
$n^2$. Entsprechend kann man sagen, der Rechenaufwand von Selection Sort
nimmt im Quadrat zur Anzahl der zu sortierenden Element zu.
