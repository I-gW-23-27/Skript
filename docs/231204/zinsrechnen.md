# Zinsrechnen

Der Zins wird angegeben in % pro Jahr. Das bedeutet, dass wenn ein Kapital
von CHF 2'500 mit 5% verzinst wird, nach einem Jahr CHF 125 Zins
aufgelaufen ist ($\frac{2500 \cdot 5}{100} = 125$).

In der Realität steht Kapital allerdings kaum je genau während eines
Kalenderjahres zur Verfügung. Das heisst, ein angebrochenes Jahr muss
als Bruchteil eines Kalenderjahres berücksichtigt werden. Dazu wird in
der Schweiz (immer noch) häufig nach der
[*Deutschen
Usanz*](https://de.wikipedia.org/wiki/Zinsberechnungsmethode#30/360_%E2%80%93_deutsche_(kaufm%C3%A4nnische)_Zinsmethode)
gerechnet. Nach dieser Methode wird das Jahr mit 360 Tagen à 12 Monate
mit je 30 Tagen gerechnet. Wenn also die erwähnten CHF 2'500 vom 15.
Januar bis zum 23. Mai zur Verfügung stehen, lautet die Berechnung
$\frac{\frac{2500 \cdot 5}{100}}{360} \cdot (15 + 3 \cdot 30 + 23) =
44.44$ (15 Tage bis Ende Januar, 3 mal 30 Tage für die Monate Februar,
März und April, 23 Tage im Mai). Wie die Situation aussieht, wenn das
Kapital über den Jahreswechsel hinaus auf dem Konto liegt, wird zu eine
späteren Zeitpunkt besprochen.

Gesucht ist also ein Programm, das basierend auf dem Kapital, dem
Zinssatz und der Zeitspanne den Zins berechnet. Die dafür erforderlichen
Grundlagen finden sich in diesem
[Notebook](https://nbviewer.org/github/I-gW-23-27/Skript/blob/main/docs/231204/zinsrechnen.ipynb).

[Hier](https://nbviewer.org/github/I-gW-23-27/Skript/blob/main/docs/231204/musterloesung_zinsrechnen.ipynb)
finden Sie eine mögliche Umsetzung der Aufgabenstellung.