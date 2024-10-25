# Aufgaben zur logischen Verknüpfung von Wahrheitswerten

## Überblick über logische Verknüpfungen

Bei der logischen und Verknüpfung ($\land$) von mehreren Werten, müssen alle
einzelnen Werte wahr sein, damit auch das Resultat der Verknüpfung wahr ist. Was
das Bedeutet, ist in den untenstehenden beiden Wahrheitstabellen dargestellt. 

### Verknüpfung von zwei Werten

$$
\begin{array}{|c|c|c|}
    \hline
    A & B & A \land B \\
    \hline
    0 & 0 & 0 \\
    0 & 1 & 0 \\
    1 & 0 & 0 \\
    1 & 1 & 1 \\
    \hline
\end{array}
$$

### Verknüpfung von drei Werten

\[
\begin{array}{|c|c|c|c|}
    \hline
    A & B & C & A \land B \land C \\
    \hline
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 1 & 1 & 0 \\
    1 & 0 & 0 & 0 \\
    1 & 0 & 1 & 0 \\
    1 & 1 & 0 & 0 \\
    1 & 1 & 1 & 1 \\
    \hline
\end{array}
\]