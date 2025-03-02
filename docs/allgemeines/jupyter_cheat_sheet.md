# Jupyter Cheat Sheet

Die folgenden Anleitungen setzen voraus, dass eine funktionierende
Python-Installation auf dem System vorhanden ist. Alternativ gibt es
verschiedene Möglichkeiten on-line Jupyter Notebooks zu erstellen.

## Anlegen eines neuen Projekts

1. Neuer Ordner anlegen
   
   Legen Sie einen Ordner mit einem passenden Namen an.

2. Virtuelle Arbeitsumgebung anlegen
   
   Öffnen Sie im Projektordner ein Terminal (`ctrl + L`, `cmd` und `enter`).
   Geben Sie in diesem Terminal hinter dem eingabeprompt (`>`) über die Tastatur
   den Befehl `python -m venv venv` ein. Den Befehl schliessen Sie mit der
   `enter`-Taste ab.

3. Virtuelle Arbeitsumgebung starten
   
   Im immer noch geöffneten Terminal geben Sie über die Tastatur den Befehl
   `venv\Scripts\activate` ein. Den Befehl schliessen Sie mit der `enter`-Taste
   ab.
   
4. Installation der erforderlichen Libraries
   
   Innerhalb der aktivierten virtuellen Arbeitsumgebung (zu erkennen an `(venv)`
   am Anfang der Eingabezeile) installieren Sie mit dem Befehl `pip install
   jupyter` die Jupyter Library. Falls weitere Libraries wie zum Beispiel pandas
   oder matplotlib erforderlich sind, können diese gleichzeitig installiert
   werden (der Befehl lautet dann entsprechend `pip install jupyter pandas
   matplotlib`, alle gewünschten Libraries werden ohne Kommata aufgelistet). Der
   Befehl wird mit der `enter`-Taste abgeschlossen.

5. Starten des Jupyter Servers
   
   Der Jupyter Server, in welchem das Notebook bearbeitet werden kann, wird im
   immer noch geöffneten Terminal mit dem Befehl `jupyter notebook` gestartet.
   Den Befehl schliessen Sie mit der `enter`-Taste ab.  
   Dieser Befehl öffnet den Standardbrowser Ihres Rechners (wenn der Browser
   bereits geöffnet ist, öffnet sich ein neuer Tab).

6. Anlegen eines neuen Jupyter Notebooks
   
   Um ein neues Notebook anzulegen, klicken Sie oben rechts auf die Schaltfläche
   `New`. Im sich öffnenden drop-down Menü wählen Sie `Python 3 (ipykernel)`
   aus. Dies öffnet ein neues leeres Notebook.

## Starten eines bestehenden Projekts

1. Projektordner öffnen
   
   Navigieren Sie im Windows Explorer in den Projektordner.

2. Starten der virtuellen Arbeitsumgebung
   
   Öffnen Sie im Projektordner ein Terminal (`ctrl + L`, `cmd` und `enter`).
   Geben Sie in diesem Terminal hinter dem eingabeprompt (`>`) über die Tastatur
   den Befehl `python -m venv venv` ein. Den Befehl schliessen Sie mit der
   `enter`-Taste ab.

   Im Terminal geben Sie über die Tastatur den Befehl
   `venv\Scripts\activate` ein. Den Befehl schliessen Sie mit der `enter`-Taste
   ab.

3. Starten des Jupyter Servers
   
   Der Jupyter Server, in welchem das Notebook bearbeitet werden kann, wird im
   immer noch geöffneten Terminal mit dem Befehl `jupyter notebook` gestartet.
   Den Befehl schliessen Sie mit der `enter`-Taste ab.  
   Dieser Befehl öffnet den Standardbrowser Ihres Rechners (wenn der Browser
   bereits geöffnet ist, öffnet sich ein neuer Tab).

4. Öffnen des Jupyter Notebooks
   
   Im Browserfenster navigieren Sie zum Jupyter Notebook. Sie können das
   Notebook öffnen durch Doppelklick öffnen.