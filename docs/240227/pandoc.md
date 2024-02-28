# Dateien konvertieren mit Pandoc

[Pandoc](https://pandoc.org/) 
ist ein Programm zur Konversion von Dateiformaten. Hier erhalten
Sie eine Anleitung für die Installation und die Konversion zwischen den
gängigsten Dateiformaten.

## Installation

Die Installationsdatei findet man via die Hauptseite von
[Pandoc](https://pandoc.org/).
Unter dem Menüprunkt *Installing* findet man einen Link *Download the
latest installer*. Dieser führt einem auf das GitHub Repository mit den
neuesten Installationsdateien für alle gängigen Betriebssysteme. Für die
Installation auf einem Windows Rechner ist die Datei mit der Endung
`.msi` (wahrscheinlich **M**icro**s**oft **I**nstaller) herunterzuladen.
Die heruntergeladene Datei kann mit einem Doppelklick installiert
werden.

## Verwendung von Pandoc

Pandoc ist ein Programm, welches von der Kommandozeile (Terminalfenster)
aus bedient wird. Um Pandoc verwenden zu können, ist es am einfachsten,
ein Terminalfenster im Verzeichnis zu öffnen, in welchem die zu
konvertierende Datei gespeichert ist.  
Dazu navigiert man mit dem Windows Explorer (Dateimanager) in dieses
Verzeichnis (für die Anleitung wird davon ausgegangen, dass die Datei im
Verzeichnis `C:\Users\username\Schule` liegt). Wenn der Ordner *Schule*
geöffnet ist, kann ein Terminalfenster geöffnet werden, indem man mit
der Tastenkombination `Ctrl` + `l` den Inhalt der Adresszeile von
Windows Explorer markiert und mit der Buchstabenfolge `cmd` überschreibt
und die Eingabe mit der Enter-Taste abschliesst.  
Danach öffnet sich ein Terminalfenster. Im Terminalfenster steht als
unterste Zeile der Pfad zum Ordner, in dem das Terminalfenster geöffnet
wurde (im Beispiel `C:\Users\username\Schule`) abgeschlossen mit dem
Eingabeprompt (`>`).  

Als erstes gehen wird davon aus, dass eine Datei `text.md`, welche im
Ordner *Schule* gespeichert ist, in ein Word-Dokument konvertiert werden
soll. Dazu wird nach dem Eingabeprompt der Befehl

```bash
pandoc -o text.docx text.md
```

eingegeben und mit Enter abgeschlossen. `-o text.docx` kann dabei
gedanklich mit "erstelle die Datei `text.docx` als Output übersetzt
werden.  
Durch die Angabe des Dateityps in der Endung der Output-Datei wird
Pandoc mitgeteilt, in welches Format die Eingabedatei konvertiert werden
soll. Pandoc stellt eine 
[ausführliche Anleitung](https://pandoc.org/MANUAL.html) 
aller möglicher Konversionen zur Verfügung.

Falls eine Datei in ein PDF konvertiert werden soll, muss auf dem
Rechner 
[LaTeX](https://de.wikipedia.org/wiki/LaTeX) 
installiert sein. Es gibt verschiedenen Versionen dieses
Textverarbeitungsprogramms. Am einfachsten wird 
[MiKTEX](https://miktex.org/) 
installiert. Im Downloadbereich findet sich eine Schritt für Schritt
Anleitung zur Installation.