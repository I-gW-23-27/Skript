# Divide and Conquer

Das Prinzip *divide and conquer* (teile und herrsche) wird am Beispiel
von Merge Sort - einem Sortieralgorithmus - vorgestellt.
Dieses Prinzip basiert auf der Idee, das kleine Probleme einfacher zu
lösen sind als grosse. Deshalb versucht man, das zu lösende Problem in
Teilprobleme aufzuteilen und diese, kleineren Probleme, zu lösen um
anschliessend die Teillösungen zu einer Lösung für das Ursprungsproblem
zusammenzusetzen. 

Diese Idee wird oft durch *Rekursion* umgesetzt. Der Begriff Rekursion
kann am besten am Beispiel einer Kindergeschichte erklärt werden:

>Es isch e mal en Maa gsi, de hät en hole Zah gha. I dem Zah häts es
>Truckli gha und i däm Truckli häts es Briefli gha. I dem Briefli isch
>gstande, es isch e mal en Maa gsi, de hät en hole Zah gha. I dem Zah
>häts es Truckli gha und id däm Truckli häts es Briefli gha...

Rekursive Funktionen sind entsprechend Funktionen, die sich selber
aufrufen. 

Bevor der Algorithmus von Merge Sort besprochen wird, soll an ein paar 
[Beispielen](https://colab.research.google.com/github/I-gW-23-27/Skript/blob/main/docs/240312/src/rekursion.ipynb) 
gezeigt werden, wie rekursiv implementierte Problemlösungen
funktionieren. Hier finden Sie die illustrierte
[Musterlösung](src/rekursion_muloe.ipynb)
(stand 11. März 24).