---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: *fff
author: Jacques Mock Schindler

---

<style>
    section { justify-content: start; }
</style>

# Binary Search Tree

---

## Repetitionsaufgabe

Zeichnen Sie aus der untenstehenden Zahlenfolge einen binären Suchbaum.

```txt
45, 50, 32, 66, 40, 42, 38, 20, 46, 60, 73
```

---

## Musterlösung

![BST Musterlösung](./bst.svg)

---

## Entfernen von Knoten

1. Entfernen des Knotens mit dem Schlüssel 20
2. Entfernen des Knotens mit dem Schlüssel 32
   
   Aufbauend auf der Lösung der Teilaufgabe 1
3. Entfernen des Knotens mit dem Schlüssel 45
   
   Aufbauend auf der Lösung der Teilaufgabe 2

---

## Musterlösung 1

![Musterlösung 1](./bst-20.svg)

---

## Musterlösung 2

![Musterlösung 2](./bst-32.svg)

---

## Musterlösung 3a

![Musterlösung 3a](./bst-45a.svg)

## Musterlösung 3b

![Musterlösung 3a](./bst-45b.svg)