# Skript für den Informatikunterricht in der Klasse 1gW im Frühlingssemester 2024

In diesem Repository finden sich die im Obligatorischen Fach Informatik
in der Klasse 1gW verwendeten Unterlagen.

## Mathjax

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

## Erstellen von Präsentationen aus den Jupyter Notebooks

[Hier](https://digitalhumanities.hkust.edu.hk/tutorials/turn-your-jupyter-notebook-into-interactive-presentation-slides-using-anaconda/)
findet sich eine Anleitung. Es wird insbesondere auch beschrieben, wie
Code-Zellen zum erstellen von Grafiken in einer Präsentation
ausgeblendet werden.
