# Public-Key-Kryptographie

Obwohl es grundsätzlich möglich ist, mit dem One-Time-Pad eine sichere
Verschlüsselung zu realisieren, ist dieses Verfahren in der Realität kaum
praktikabel. Neben der Tatsache, dass der Schlüssel mindestens so lang sein
muss, wie die Nachricht selbst, braucht es ein Verfahren den, bzw. die Schlüssel
sicher zwischen Sender und Empfänger zu teilen.

Um das Problem des Schlüsselaustausches zu lösen, verwendet man spezielle
mathematische Funktionen. Diese Funktionen nennt man "Einwegfunktionen mit
Hintertüren". Eine Einwegfunktion $f(x) = x'$ lässt sich leicht berechnen, aber
ihre Umkehrung $f^{-1}(x') = x$ ist sehr schwierig zu berechnen. Die "Hintertür"
ist ein Geheimwissen, mit dem die Umkehrfunktion dann doch einfach berechnet
werden kann.

Die Einwegfunktion kann veröffentlicht werden, damit ein Absender mit deren
Hilfe eine Botschaft verschlüsseln kann. Nur der Empfänger ist dann noch in der
Lage, die Botschaft mit wenig Aufwand zu entschlüsseln. Allfällige 'Lauscher'
können die Umkehrfunktion nicht innert nützlicher Frist berechnen.