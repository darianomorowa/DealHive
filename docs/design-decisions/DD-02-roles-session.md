---

title: DD-02
parent: Design Decisions
nav_order: 2
------------

{: .no_toc }

# 02: Buyer- und Creator-Rollen über Session steuern

## Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23-Jun-2026

## Problemstellung

DealHive hat zwei unterschiedliche Nutzungsperspektiven. Käufer sollen Hives ansehen, Details prüfen und einem Hive beitreten. Creator sollen Hives erstellen, eigene Hives verwalten und Hives bearbeiten können.

Gleichzeitig wollten wir Nutzer nicht fest in eine einzige Rolle einsperren. Ein User kann selbst Creator sein und eigene Produkte anbieten, aber trotzdem auch als Käufer mal ein hübsches Bling-Bling gönnen kann. Gerade im Tabletop- und TTRPG-Bereich ist das realistisch, weil viele Leute selbst etwas bauen oder verkaufen und trotzdem Miniaturen, Würfel, Terrain oder Zubehör von anderen Creatorn kaufen.

Wir brauchten also eine einfache Rollenlogik, die beide Perspektiven abbildet, ohne zwei komplett getrennte Accounts oder Login-Systeme bauen zu müssen.

## Entscheidung

Wir haben entschieden, Buyer und Creator über die Flask-Session zu steuern.

Beim Login werden wichtige Nutzerdaten in der Session gespeichert:

```python
session["user_id"] = user["id"]
session["username"] = user["username"]
session["role"] = user["role"]
```

Dadurch weiß die App bei späteren Requests, welcher Nutzer angemeldet ist und welche Ansicht gerade aktiv ist.

Die Sidebar nutzt diese Session-Daten, um passende Links anzuzeigen. Creator-Links wie „Hive erstellen“ oder „Creator Dashboard“ erscheinen nur in der Creator-Ansicht.

Wichtig ist aber: Die Sidebar allein ist nicht die eigentliche Sicherheit. Die geschützten Routen prüfen zusätzlich serverseitig, ob ein Nutzer eingeloggt ist und ob die passende Rolle aktiv ist. Sonst könnte man einfach eine URL eintippen und versuchen, die Seite trotzdem zu öffnen.

Kurz gesagt: Ein Account kann beide Perspektiven haben, aber die App entscheidet über die aktive Session-Rolle, welche Funktionen gerade sichtbar und nutzbar sind.

## Betrachtete Optionen

| Kriterium                   | Getrennte Accounts für Buyer und Creator     | Eine users-Tabelle mit Session-Rolle       | Nur Links ausblenden          |
| --------------------------- | -------------------------------------------- | ------------------------------------------ | ----------------------------- |
| **Umfang**                  | Zu groß für die erste brauchbare Version     | Gut machbar                                | Sehr einfach, aber zu schwach |
| **Verständlichkeit**        | Mehr Login-Logik nötig                       | Klar und gut erklärbar                     | Wirkt eher wie UI-Trick       |
| **Implementierungsaufwand** | Hoch                                         | Mittel                                     | Niedrig                       |
| **Flexibilität für Nutzer** | Nutzer müssten eventuell zwei Accounts haben | Ein Account kann beide Perspektiven nutzen | Unklar geregelt               |
| **Sicherheit im Prototyp**  | Möglich, aber aufwendig                      | Ausreichend für das Projekt                | Nicht ausreichend             |
| **Prüfungserklärung**       | Zu viel Nebenthema                           | Gut am Code zeigbar                        | Schwer zu verteidigen         |

Wir haben uns für eine gemeinsame users-Tabelle mit Rollensteuerung über die Session entschieden. Dieser Ansatz ist für unseren Projektumfang klein genug, aber trotzdem flexibel genug, damit ein Nutzer sowohl Creator als auch Käufer sein kann.
