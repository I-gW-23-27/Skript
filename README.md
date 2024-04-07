# Skript für den Informatikunterricht in der Klasse 1gW

In diesem Repository finden sich die im Obligatorischen Fach Informatik
in der Klasse 1gW verwendeten Unterlagen.

## Informationsfetzen für den Unterhalt des Webauftritts

Im folgenden eine Art Notizbuch mit Informationsfragmenten für das
Handling des Unterrichtsbezogenen Webauftrtitts.

### Mathjax

Für die Darstellung mathematischer Formeln auf GitHub Pages braucht es
die JavaScript Display Engine. Diese ist allerdings nicht standardmässig
implementiert.

Um Mathjax zu implementieren muss im Ordner `docs` ein Unterordner
`_layouts` angelegt werden. Darin braucht es die Datei `default.html`
des verwendeten Themes. Die Unterlagen werden in diesem Repository im
[Theme *Slate*](https://github.com/pages-themes/slate) dargestellt. Dort
findet sich die entsprechende Datei.

In der Datei `default.html` muss im `<head>` folgender Code eingefügt
werden:

```{html}
<script type="text/javascript" async
   src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      extensions: ["tex2jax.js"],
      jax: ["input/TeX", "output/HTML-CSS"],
      tex2jax: {
        inlineMath: [ ['$','$'], ["\\(","\\)"] ],
        displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
        processEscapes: true
      },
      "HTML-CSS": { availableFonts: ["TeX"] }
    });
</script>
```

### Erstellen von Präsentationen aus den Jupyter Notebooks

[Hier](https://digitalhumanities.hkust.edu.hk/tutorials/turn-your-jupyter-notebook-into-interactive-presentation-slides-using-anaconda/)
findet sich eine Anleitung. Es wird insbesondere auch beschrieben, wie
Code-Zellen zum erstellen von Grafiken in einer Präsentation
ausgeblendet werden.

### Unicode Zeichen in Dia Diagrammen

Um mathematische Formeln in Dia zu schreiben, müssen die Zeichen mit
Unicode eingegeben werden. Dazu muss das u aus Unicode mit `Ctrl` +
`Shift` + `u` eingegeben werden. Dann kommt der Wert hinter dem +. Die
ganze Eingabe ist mit Enter abzuschliessen.

### SVG mit TikZ erstellen

Die `.tex` Datei muss die folgende Struktur aufweisen:

```tex
\documentclass[dvisvgm]{standalone}

\usepackage[usenames,dvipsnames]{xcolor}
\usepackage{tikz}
\usetikzlibrary {positioning,
                 shapes.geometric}

\begin{document}
\begin{tikzpicture}
... 
\end{tikzpicture}
\end{document}
```

Die Konversion der Datei erfolgt mit den zwei Befehlen

```bash
lualatex --output-format=dvi inputdatei.tex

dvisvgm --no-fonts inputdatei.dvi
```

## Nützliche Links für den Informatikunterricht


Hier soll eine Sammlung interessanter Links für den Informatikunterricht
entstehen.

### Programmvisualisierung

[Python Tutor](https://pythontutor.com/render.html#mode=edit)

### Algorithmen

[Visualisierung von
Sortieralgorithmen](https://www.toptal.com/developers/sorting-algorithms)
[Visualisierung von Algorithmen und
Datenstrukturen](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

[Merge Sort](https://opendsa-server.cs.vt.edu/embed/mergesortAV)  
Die Visualisierung kann mit eigenen Werten gefüttert werden. Weitere
Visualisierungen können mit Suchbegriff und opendsa gefunden werden.

### Jupyter Notebook

[Print Ready
Notebooks](http://blog.juliusschulz.de/blog/ultimate-ipython-notebook)

[Learning Scientific Programming with Python](https://scipython.com/)

### Cyber Security

* [Hacksplaining](https://www.hacksplaining.com/)
  
  Die Seite erklärt, wie verschiedene Angriffe funktionieren.

* [w3schools](https://www.w3schools.com/cybersecurity/)
  
  Tutorial Sammlung für Cyber Security Themen

* [Lightbeam (Firefox Plug-In)](https://de.wikipedia.org/wiki/Lightbeam)
  
  Ein Plug-In für den Firefox Browser, welches graphisch darstellt, wie
  Coockies den Browserverlauf aufzeichnen.

### Visuals

[xkcd](https://xkcd.com/)
