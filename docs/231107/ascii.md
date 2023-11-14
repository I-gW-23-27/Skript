# Zeichencodierung

## Die ASCII-Tabelle

Die
[ASCII-Tabelle](https://www.torsten-horn.de/techdocs/ascii.htm)
ist eine Codierungstabelle, in der Zeichen in einem
7-Bit-Code dargestellt werden. Dies ermöglicht die Darstellung von 128
Zeichen.

Die Zeichen des lateinischen Alphabets besetzten dabei die Codes 65 bis
90 (Grossbuchstaben) und 97 bis 122 (Kleinbuchstaben). Wenn diese Zahlen
als Binärzahlen dargestellt werden, kann damit Text mit Null und Eins
dargestellt werden.

"Hello World!" in Dezimalzahlen ist 72 101 108 108 111 32 87 111 114 108
100 33. Binär codiert

1001000 1100101 1101100 1101100 1101111 100000 1010111 1101111 1110010
1101100 1100100 100001

So kann Text mit Nullen und Einsen dargestellt werden.

## Unicode

Die Zeichencodierung mit der ASCII Tabelle erlaubt lediglich die
Darstellung des lateinischen Alphabets. Dies ist unzureichend. Nach
mehreren Zwischenschritten werden heute die darstellbaren Zeichen mit
der
[Unicode Tabelle](https://home.unicode.org)
codiert. Die Unicode Tabelle codiert die Zeichen in
$17 \cdot 2^{16}$ Zeichen. Damit ist es theoretisch möglich,
mehr als eine Million Zeichen zu codieren. Die Zeichen werden dabei mit
einer Hexadezimalzahl und vorangestelltem U+ beschrieben. Das grosse
lateinische A wird so zu `U+0041`. Dabei entspricht das hexadezimale 41
dem dezimalen 65.

"Hello World!" in Unicode ist entsprechend U+0048 U+0065 U+006C  U+006C
U+006F U+0020 U+0057 U+0065 U+0072 U+006C U+0064 U+0041.

Die grosse Anzahl möglicher Zeichen lässt es ausserdem zu, Emojis in
Unicode zu codieren (U+1F609).