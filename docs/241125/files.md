# File Handling in Python

Bisher wurden die verarbeiteten Daten immer direkt in den zu Übungszwecken
erstellten Jupyter Notebooks abgelegt. Dies ist nicht immer Hilfreich. Python
stellt daher Möglichkeiten zur Verfügung, Files zu lesen und zu Schreiben.

Mit der `open()` Funktion stellt Python eine Möglichkeit zur Verfügung, Daten
von einem File zu lesen und sie in ein File zu schreiben.  
Um Daten in ein File zu schreiben, wird die `open()` Funktion folgendermassen
verwendet:

```Python
with open('file.txt', 'w') as myfile:
    myfile.write('text')
```

Das Listing macht der Reihe nach folgendes:

* `with` stellt sicher, dass das geöffnete File auch im Falle eines Fehlers im
  Programm korrekt geschlossen wird.
* `open` öffnet das File, welches mit Pfad in der Klammer identifiziert wird.
  Das File muss dabei noch nicht bestehen. Wenn es schon besteht wird es mit dem
  Attribut `'w'` überschrieben. Wenn es ergänzt werden soll, muss das Attribut
  `'a'` verwendet werden.
* `as myfile` ermöglicht es, innerhalb des Python Programmes einen frei
  gewählten Namen für das geöffnete File zu verwenden.
* `myfile.write(...)` schreibt den Inhalt in der Klammer in das geöffnete File.

Um Daten aus einem File zu lesen, wird die `open()` Funktion wie im folgenden
Listing dargestellt verwendet:

```Python
with open('file.txt', 'r') as myfile:
    inhalt = myfile.read()
    print(inhalt)
```

Der Reihe nach, was beim Lesen anders ist als beim Schreiben:

* `open` erhält neben dem Pfad zum File das Attribut `r` für *read*.
* `inhalt = myfile.read()` weist den ausgelesenen Inhalt der Variabeln `inhalt` zu.

Falls der Inhalt der Datei zeilenweise gelesen werden soll, kann der Code
folgendermassen abgeändert werden:

```Python
with open('file.txt', 'r') as myfile:
    for zeile in myfile:
        print(zeile)
```