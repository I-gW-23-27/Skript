# User-Eingaben in Python

Python stellt für die Entgegennahme von User-Eingaben die Funktion
`input()` zur Verfügung. Mit der Funktion `input()` wird die
User-Eingabe einer Variabel zugewiesen (`x = input()`). Durch den Aufruf
der Funktion wird ein Terminal geöffnet, in dem die User-Eingabe
vorgenommen werden kann. Damit der User weiss, was für eine Eingabe von
ihm erwartet wird, kann `input()` ein String als Parameter mitgegeben
werden. Wenn der Variabel `name` der Name des Users zugewiesen werden
soll, sieht dies folgendermassen aus:

```{Python}
name = input("Geben Sie Ihren Namen ein: ")
```

`input()` weist der Variabel einen String zu. Wenn die Weiterverarbeitung
der User-Eingabe einen anderen Datentypen erfordert, muss dieser
entsprechend umgewandelt werden. Diese Umwandlung wird 
[*Typecasting*](https://www.w3schools.com/python/python_casting.asp)
genannt. Wenn die User-Eingabe eine Zahl ist, die für eine Berechnung
verwendet wird, muss der Eingabestring in das erforderliche Zahlenformat
umgewandelt - *gecastet* - werden. Dies kann entweder direkt bei der
Entgegennahme der Eingabe erfolgen (`x = float(input("Geben Sie eine Zahl
ein: "))`) oder indem die Variabel *gecastet* wird (`x = float(x)`).

[Hier finden Sie ein Arbeitsblatt zur Funktion `input()`](https://nbviewer.org/github/I-gW-23-27/Skript/blob/main/docs/231128/input.ipynb).