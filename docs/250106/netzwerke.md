# Einführung in Computernetzwerke

Computernetzwerke ermöglichen die Kommunikation zwischen Computern. In dieser
Unterrichtseinheit soll gezeigt werden, wie das technisch funktioniert.

Um die Bedeutung dieser technischen Grundlagen für die Gesellschaft aufzuzeigen,
sei hier auf ein Artikel aus der 
[NZZ vom 24. Oktober 2022](wie-china-unter-xi-das-internet-kontrolliert-ld.html) 
zur Zensur des
Internets in China verwiesen.

## OSI Layer Modell

Das OSI (Open System Interconnection) Modell ermöglicht es, die Kommunikation
über verschiedene technische Systeme hinweg zu beschreiben. Dieses theoretische
Modell beschreibt sieben Schichten (Layer) der Kommunikation. Die unterste
Schicht beschäftigt sich mit der Ebene der physikalischen Verbindung, die
oberste mit der Kommunikation innerhalb einer spezifischen Anwendung. Eine
detaillierte Beschreibung der einzelnen Schichten findet sich im entsprechenden
[Eintrag der Wikipedia](https://de.wikipedia.org/wiki/OSI-Modell).

## Das TCP/IP Protokoll

Vom OSI Layer Modell werden technisch nicht alle Ebenen umgesetzt. Durchgesetzt
hat sich das 
[TCP/IP
Referenzmodell](https://de.wikipedia.org/wiki/Internetprotokollfamilie#TCP/IP-Referenzmodell)
(Transmission Control Protocol/Internet Protocol). Dieses benutzt lediglich vier
der im OSI Modell beschriebenen Schichten. Eine Netzwerkschicht für die
physikalische Verbindung, eine Internetschicht für die Vermittlung zwischen den
Computern, eine Transportschicht für die eigentliche Übermittlung der Daten
sowie eine Anwendungsschicht für die Auslieferung der Daten an die konkrete
Anwendung auf dem Computer.

## IP Adressen

Aktuell soll hier vor Allem die Internetschicht betrachtet werden. Ausgangspunkt
für die entsprechenden Beobachtungen ist dabei die IP-Adresse. IP-Adressen geben
jedem mit einem Computernetzwerk verbundenen Computer eine eindeutige Adresse.
Über diese Adresse ist der Computer im Netzwerk erreichbar.

Aktuell bestehen zwei Versionen von IP-Adressen nebeneinander - IPv4- und
IPv6-Adressen. Eigentlich sollten die IPv6-Adressen die IPv4-Adressen ablösen.
Dieser Prozess geht allerdings nur sehr langsam vonstatten. Daher muss man sich
derzeit mit beiden Versionen der IP-Adressen auseinandersetzten.

### IPv4


