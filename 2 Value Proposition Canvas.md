---
title: Value prop Canvas
nav_exclude: true
nav_order: 99
---

# Value Proposition Canvas - Buyer

## Customer Segment

### To-Dos

- Produkte günstiger kaufen als zum Einzelpreis
- Mengenrabatte nutzen, ohne selbst große Mengen abnehmen zu müssen
- Offene Sammelaktionen entdecken und schnell beitreten

### Gains

- Rabatt wird tatsächlich erreicht und freigeschaltet
- Wenig Aufwand bei der Koordination
- Transparenz über den aktuellen Stand des Sammelkaufs

### Pains

- Mengenrabatte sind nur für Großabnehmer erreichbar
- Unsicherheit, ob genug Leute mitmachen


## Value Proposition

### Features

- Sammelaktionen erstellen mit Produkt, Mindestmenge und Rabattziel
- Offene Aktionen entdecken und beitreten
- Echtzeit-Anzeige wie viele Plätze noch fehlen

### Gain Creators

- Rabattschwellen werden kollektiv erreichbar
- Transparente Fortschrittsanzeige motiviert zum Beitreten
- Zwei klar getrennte Rollen: Initiator (Seller) und Joiner (Buyer)

### Pain Relievers

- Koordination läuft über die Plattform, kein manueller Aufwand
- Jeder sieht sofort ob eine Aktion noch offen ist
- Keine Mindestabnahme für Einzelpersonen nötig​​​​​​​​​​​​​​​​






# Value Proposition Canvas - Seller

## Customer Segment

### To-Dos

- Neue Käufergruppen erschließen, die sonst keine Großmengen abnehmen würden
- Mengenrabatte als Verkaufsanreiz gezielt einsetzen
- Produkte schnell in größeren Stückzahlen absetzen

### Gains

- Mindestabnahmemengen werden kollektiv durch Käufer erreicht
- Neue Kundensegmente werden erreichbar
- Planbare Verkaufsmenge durch feste Aktionsbedingungen

### Pains

- Mengenrabatte bleiben oft ungenutzt, weil Einzelkäufer die Schwelle nicht erreichen
- Kein direkter Kanal zu preissensitiven Käufern die koordiniert kaufen wollen
- Unsicherheit ob Mindestmenge überhaupt erreicht wird


## Value Proposition

### Features

- Deal-Angebote erstellen mit Produkt, Mindestmenge und Rabattstufe
- Echtzeit-Übersicht wie viele Käufer bereits beigetreten sind
- Automatische Benachrichtigung wenn Mindestmenge erreicht ist

### Gain Creators

- Neue Käufergruppen werden über die Plattform direkt erreichbar
- Verkaufsmengen sind durch Aktionsbedingungen planbar
- Kein manueller Koordinationsaufwand

### Pain Relievers

- Mindestmenge wird kollektiv durch Plattform gefüllt, nicht durch Einzelkäufer
- Direkter Kanal zu preissensitiven koordinierten Käufern
- Transparenz über Aktionsstatus reduziert Unsicherheit


## Ergänzung zum aktuellen App-Stand

Seit der ursprünglichen Formulierung der Value Proposition wurde der technische Umfang der App weiter konkretisiert. Die Grundidee bleibt gleich: DealHive soll Creator und Käufer bei Sammelkäufen im Bereich Brettspiele, TTRPGs, Tabletops und Zubehör zusammenbringen.

Der aktuelle App-Stand bildet den Kernprozess inzwischen konkreter ab:

* Creator können eigene Hives erstellen.
* Creator können eigene Hives im Creator Dashboard sehen.
* Creator können ihre eigenen Hives bearbeiten.
* Creator können Käufer eines Hives ansehen.
* Käufer können Hives entdecken und Detailseiten öffnen.
* Käufer können einem Hive mit einer bestimmten Menge beitreten.
* Käufer können ihre beigetretenen Hives unter „Meine Hives“ wiederfinden.
* Buyer und Creator können über einen einfachen Chat im Kontext eines Hives miteinander schreiben.
* Die App stellt über `/api/hives` eine einfache JSON-API bereit.

Damit wurde der Happy Path nicht nur konzeptionell beschrieben, sondern auch in der Flask-App umgesetzt. Besonders wichtig ist dabei, dass die App nicht als vollständiger Online-Shop gedacht ist. DealHive konzentriert sich weiterhin auf den ersten, realistischen MVP-Umfang: Sammelkäufe sichtbar machen, Nachfrage sammeln, Fortschritt zeigen und einfache Kommunikation zwischen Buyer und Creator ermöglichen.

Einige ursprünglich angedachte Felder aus den frühen Skizzen, zum Beispiel Material, Versandregion oder Produktbilder, sind im aktuellen MVP noch nicht vollständig umgesetzt. Stattdessen wurde der Umfang bewusst reduziert und auf die wichtigsten Felder beschränkt:

* Produktname
* Spielsystem
* Kurzbeschreibung
* Beschreibung
* Mindestmenge
* Basispreis
* Deadline
* Rabattstaffeln