# Git und GitHub Workflow

## `git clone`

Um die Dateien aus einem GitHub Repository lokal bearbeiten zu können,
muss das Repository lokal verfügbar gemacht - geklont - werden. 

Wie das funktioniert, soll anhand eines Beispiels gezeigt werden. 
Für das Beispiel gehen wir davon aus,
dass es auf dem Rechner einen Ordner *Informatik* gibt. Der Ganze Pfad
zu diesem Ordner lautet `C:\Users\username\Schule\Informatik`.

Als erstes ist ein Terminalfenster zu öffnen. Standardmässig sollte in
der letzten Zeile des Terminalfenster `C:\Users\username>` stehen. In
einem zweiten Schritt muss in den Ordner gewechselt werden, in welchen
das Repository geklont werden soll. Dazu wird nach dem *Eingabeprompt*
(`>`) der Befehl `cd "Schule\Informatik"` eingegeben.
Die letzte Zeile im Terminalfenster hat nun den Inhalt
`C:\Users\username\Schule\Informatik>`. 
Als letzter Schritt kann nun der Befehl `git clone url_zum_repository`
eingegeben werden `url_zum_repository` kann in GitHub von "hinter" dem
grünen Knopf *Code" kopiert werden.

Als Resultat des Befehls `git clone` hat man im Ordner *Informatik*
einen Ordner mit dem Namen des Repositorys mit allen Dateien zur
Verfügung. 

## `git commit`

Um den aktuellen Zustand eines Dokuments bzw. des ganzen Repositorys als
Snapshot festzuhalten verwendet man den Befehl `git commit`.

Wenn nur ein einzelnes Dokument Gegenstand eines Commits sein soll, muss
dieses File zuerst mit `git add Pfad\zum\Dokment` vorgemerkt - gestaged
\- werden. Um im Beispiel zu bleiben, gehen wir davon aus, dass wir
immer noch ein Terminalfenster offen haben und uns im Repository
befinden. Auf der untersten Zeile des Terminalfensters steht also
`C:\Users\username\Schule\Informatik\Repository>`. Geändert wurde das
Dokument `README.md`. Dieses Dokument soll für einen Commit vorgemerkt
werden. Dies geschieht mit dem Befehl `git add README.md`. Der
eigentliche Commit erfolgt nun mit dem Befehl `git commit`. Auf diesen
Befehl hin öffnet sich ein Editorfenster, in dem Sie die Commit
Nachricht eingeben können.