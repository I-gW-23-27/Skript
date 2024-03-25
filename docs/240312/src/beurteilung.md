# Beurteilung von Algorithmen

Die Effizienz eines Algorithmus kann grundsätzlich nach seinem
Rechenaufwand oder Speicherbedarf beurteilt werden. Man spricht in
diesem Zusammenhang auch von Zeit- bzw. Platzkomplexität.

Die entsprechenden Überlegungen sollen am Beispiel von Selection Sort
illustriert werden.

## Zeitkomplexität

Die Zeitkomplexität eines Algorithmus misst sich in der Anzahl der
erforderlichen Rechenoperationen. Im Beispiel Selection Sort besteht ein
Rechenschritt aus dem Vergleich zweier Elemente der Sequenz. 
Das ergibt bei einer Sequenz mit $n$ Elementen $\frac{n(n-1)}{2}$
Vergleiche (die Summe von $1+2+3+...+(n-1)$). 

![Visualisierung Vergleichsoperationen](../images/selection_sort_komplexity.svg)

Der Einfachheit halber
konzentriert man sich für die 
Beurteilung der Zeitkomplexität auf jenen Teil des Rechenaufwandes, der
in Abhängigkeit der Inputgrösse am stärksten zunimmt. Wenn
$\frac{n(n-1)}{2}$ ausmultipliziert wird, erhält man $\frac{1}{2}n^2 -
\frac{1}{2}n$. Das am stärksten wachsende Element in in diesem Term ist
$n^2$. Entsprechend kann man sagen, der Rechenaufwand von Selection Sort
nimmt im Quadrat zur Anzahl der zu sortierenden Element zu.

## Platzkomplexität

Selection Sort sortiert die Elemente, indem es sie direkt in der zu
sortierenden Sequenz austauscht. Solche Algorithmen, die den
Sortiervorgang innerhalb der ursprünglichen Sequenz ohne die
Notwendigkeit zusätzlichen Speichers für eine weitere Sequenz
durchführen, werden als *in-place* Algorithmen bezeichnet. In Bezug auf
den Speicherbedarf ist dies sehr günstig. Das Verfahren braucht neben
dem Platz für die eigentliche Sequenz so gut wie keinen zusätzlichen
Speicherplatz. Der Speicherplatzbedarf wird daher als konstant bezeichnet.
