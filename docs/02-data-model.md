---

title: Data Model
nav_order: 2
------------

{: .no_toc }

# Data Model

<details open markdown="block">
<summary>Table of contents</summary>

1. TOC
   {:toc}

</details>


Diese Seite beschreibt das Datenmodell unserer Anwendung.
Die Datenbank basiert auf SQLite und wird in `database.py` über die Funktion `create_tables()` erstellt.

Aktuell besteht das Datenmodell aus fünf Tabellen:

* `users`
* `hives`
* `user_hives`
* `hive_tiers`
* `messages`

Die wichtigsten Tabellen für den Grundaufbau sind `users`, `hives` und `user_hives`.
Zusätzlich gibt es `hive_tiers` für Preisstaffeln und `messages` für den Chat.

## Vereinfachte ER-Übersicht

```text
users
  id
  username
  role
   |
   | 1:n
   v
user_hives
  user_id
  hive_id
  relation_type
  quantity
   ^
   | n:1
   |
hives
  id
  title
  current_participants
  min_participants
  base_price
   |
   | 1:n
   v
hive_tiers
  hive_id
  threshold_quantity
  discount_percent

hives
  id
   |
   | 1:n
   v
messages
  hive_id
  sender_id
  receiver_id
  message_text
```

Die Tabelle `user_hives` ist die zentrale Verbindung zwischen Nutzern und Hives. Über `relation_type` wird unterschieden, ob ein User als `creator` oder als `buyer` mit einem Hive verbunden ist. Über `quantity` wird gespeichert, wie viele Einheiten ein Buyer bestellen möchte.


---

## Übersicht der Datenbanktabellen

### Tabelle `users`

In der Tabelle `users` werden alle registrierten Nutzer gespeichert.
Sie enthält Login-Daten, Rolleninformationen und Profildaten wie Name, E-Mail und Adresse.

| Spalte          | Bedeutung                                       |
| --------------- | ----------------------------------------------- |
| `id`            | Eindeutige ID des Nutzers                       |
| `username`      | Benutzername für Login und Anzeige              |
| `name`          | Vollständiger Name des Nutzers                  |
| `email`         | E-Mail-Adresse des Nutzers                      |
| `password_hash` | Gespeichertes Passwort bzw. Passwort-Hash       |
| `role`          | Rolle des Nutzers, z. B. `buyer` oder `creator` |
| `street`        | Straße des Nutzers                              |
| `postal_code`   | Postleitzahl                                    |
| `city`          | Stadt                                           |
| `country`       | Land                                            |

---

### Tabelle `hives`

In der Tabelle `hives` werden alle Sammelaktionen gespeichert.
Ein Hive beschreibt ein Angebot, dem Nutzer beitreten können, um gemeinsam eine bestimmte Mindestmenge zu erreichen.

| Spalte                 | Bedeutung                                         |
| ---------------------- | ------------------------------------------------- |
| `id`                   | Eindeutige ID des Hives                           |
| `title`                | Titel des Hives                                   |
| `game_system`          | Zugehöriges Spielsystem, z. B. D&D oder Warhammer |
| `short_description`    | Kurze Beschreibung für Übersichtsseiten           |
| `description`          | Ausführliche Beschreibung des Hives               |
| `deadline`             | Deadline der Sammelaktion                         |
| `current_participants` | Aktuelle Teilnehmer- bzw. Bestellmenge            |
| `min_participants`     | Mindestmenge, die erreicht werden soll            |
| `base_price`           | Grundpreis des Produkts vor Rabatt                |

---

### Tabelle `user_hives`

Die Tabelle `user_hives` verbindet Nutzer mit Hives.
Darüber wird gespeichert, ob ein Nutzer einen Hive erstellt hat oder einem Hive beigetreten ist.

| Spalte          | Bedeutung                                            |
| --------------- | ---------------------------------------------------- |
| `id`            | Eindeutige ID der Zuordnung                          |
| `user_id`       | Verweis auf den Nutzer aus der Tabelle `users`       |
| `hive_id`       | Verweis auf den Hive aus der Tabelle `hives`         |
| `relation_type` | Art der Beziehung, z. B. `creator` oder `buyer`      |
| `quantity`      | Menge, die ein Buyer bei einem Hive bestellen möchte |

Diese Tabelle ist wichtig, weil ein Hive nicht direkt nur einem Nutzer gehört.
Stattdessen wird die Beziehung zwischen Nutzern und Hives über `user_hives` gespeichert. Dadurch kann ein Hive einen Creator und mehrere Buyer haben.

---

### Tabelle `hive_tiers`

Die Tabelle `hive_tiers` speichert die Preisstaffeln bzw. Rabattstufen eines Hives.
Die Preiskategorien sind also nicht in einem Dictionary gespeichert, sondern relational in einer eigenen Datenbanktabelle.

| Spalte               | Bedeutung                                              |
| -------------------- | ------------------------------------------------------ |
| `id`                 | Eindeutige ID der Preisstaffel                         |
| `hive_id`            | Verweis auf den zugehörigen Hive                       |
| `threshold_quantity` | Mindestmenge, ab der diese Rabattstufe gilt            |
| `discount_percent`   | Rabatt in Prozent, der ab dieser Menge angewendet wird |

Beispiel: Wenn `threshold_quantity` den Wert `10` hat und `discount_percent` den Wert `15`, bedeutet das: Ab 10 bestellten Einheiten gilt 15 Prozent Rabatt.

Der Grundpreis steht nicht in `hive_tiers`, sondern in `hives.base_price`.
Die Funktion `calculate_current_price(hive_id)` nutzt den Grundpreis, die aktuelle Bestellmenge und die passenden Rabattstaffeln, um den aktuellen Preis zu berechnen.

---

### Tabelle `messages`

Die Tabelle `messages` speichert Chat-Nachrichten zwischen Nutzern im Kontext eines bestimmten Hives.

| Spalte         | Bedeutung                                         |
| -------------- | ------------------------------------------------- |
| `id`           | Eindeutige ID der Nachricht                       |
| `hive_id`      | Verweis auf den Hive, zu dem die Nachricht gehört |
| `sender_id`    | User-ID des Absenders                             |
| `receiver_id`  | User-ID des Empfängers                            |
| `message_text` | Inhalt der Nachricht                              |
| `timestamp`    | Zeitpunkt, zu dem die Nachricht gespeichert wurde |

Dadurch können Nachrichten einem bestimmten Hive und zwei bestimmten Nutzern zugeordnet werden.

---

## Übersicht der Datenbankfunktionen

| Funktionsname                                | Funktion / Zweck                                                                                                                                               |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_connection()`                           | Öffnet die Verbindung zur SQLite-Datenbank `dealhive.db` und sorgt dafür, dass Spalten über Namen angesprochen werden können.                                  |
| `create_tables()`                            | Erstellt alle benötigten Tabellen, falls sie noch nicht existieren: `hives`, `users`, `user_hives`, `hive_tiers` und `messages`.                               |
| `insert_test_hives(test_hives)`              | Fügt mehrere Test-Hives in die Tabelle `hives` ein. Wird für Testdaten genutzt.                                                                                |
| `get_all_hives()`                            | Lädt alle Hives aus der Datenbank und gibt sie als Liste zurück.                                                                                               |
| `get_hive_by_id(hive_id)`                    | Lädt einen einzelnen Hive anhand seiner ID. Wenn kein Hive gefunden wird, wird `None` zurückgegeben.                                                           |
| `insert_hive(...)`                           | Speichert einen neuen Hive in der Datenbank und gibt die ID des neu erstellten Hives zurück.                                                                   |
| `update_hive(...)`                           | Aktualisiert die Grunddaten eines bestehenden Hives, zum Beispiel Titel, Beschreibung, Deadline, Mindestmenge und Basispreis.                                  |
| `create_test_user(...)`                      | Erstellt einen Testnutzer, falls dieser noch nicht existiert, und gibt dessen User-ID zurück.                                                                  |
| `assign_hive_to_user(...)`                   | Verknüpft einen User mit einem Hive. Über `relation_type` wird gespeichert, ob der User Creator oder Buyer ist. Zusätzlich kann eine Menge gespeichert werden. |
| `increase_hive_participants(...)`            | Erhöht die aktuelle Teilnehmer- bzw. Bestellmenge eines Hives um einen bestimmten Wert.                                                                        |
| `get_hives_for_user(user_id, relation_type)` | Lädt alle Hives, die einem bestimmten User mit einer bestimmten Rolle zugeordnet sind, zum Beispiel Creator-Hives oder Buyer-Hives.                            |
| `create_user_with_id(...)`                   | Erstellt einen User mit einer festen ID. Das wird vor allem für Demo- oder Testdaten genutzt.                                                                  |
| `create_user(...)`                           | Speichert einen neu registrierten Nutzer in der Tabelle `users`.                                                                                               |
| `get_user_by_username(username)`             | Lädt einen User anhand seines Usernames. Diese Funktion wird beim Login genutzt.                                                                               |
| `get_user_by_id(user_id)`                    | Lädt einen vollständigen User anhand seiner ID. Diese Funktion wird zum Beispiel für die Profilseite genutzt.                                                  |
| `update_user_profile(...)`                   | Aktualisiert die Profildaten eines Users, zum Beispiel Name, E-Mail, Rolle und Adresse.                                                                        |
| `save_private_message(...)`                  | Speichert eine private Nachricht zwischen zwei Usern zu einem bestimmten Hive.                                                                                 |
| `get_private_messages(...)`                  | Lädt alle privaten Nachrichten zwischen zwei Usern für einen bestimmten Hive, sortiert nach Zeitpunkt.                                                         |
| `get_hive_creator_id(hive_id)`               | Gibt die User-ID des Creators zurück, der einem bestimmten Hive zugeordnet ist.                                                                                |
| `insert_hive_tier(...)`                      | Speichert eine einzelne Rabattstaffel für einen Hive, bestehend aus Mindestmenge und Rabatt-Prozent.                                                           |
| `get_hive_tiers(hive_id)`                    | Lädt alle Rabattstaffeln eines Hives, sortiert nach Mindestmenge.                                                                                              |
| `replace_hive_tiers(...)`                    | Löscht die alten Rabattstaffeln eines Hives und speichert neue Rabattstaffeln aus dem Formular.                                                                |
| `calculate_current_price(hive_id)`           | Berechnet den aktuellen Preis eines Hives anhand des Basispreises, der aktuellen Bestellmenge und der erreichten Rabattstaffel.                                |

---

## Relationships

Ein Nutzer wird in der Tabelle `users` gespeichert.
Ein Hive wird in der Tabelle `hives` gespeichert.
Die Verbindung zwischen Nutzern und Hives wird über `user_hives` hergestellt.

Beispiel:

* Ein Creator erstellt einen Hive.
* In `user_hives` wird gespeichert, dass dieser User mit `relation_type = creator` zu diesem Hive gehört.
* Wenn ein Buyer einem Hive beitritt, wird ebenfalls ein Eintrag in `user_hives` gespeichert, aber mit `relation_type = buyer`.
* Über `quantity` wird gespeichert, wie viele Einheiten der Buyer bestellen möchte.

Die Rabattlogik wird über `hive_tiers` abgebildet.
Dort werden die Mengenstufen und Rabattprozente gespeichert. Der aktuelle Preis wird dann aus `hives.base_price`, `hives.current_participants` und den passenden Einträgen aus `hive_tiers` berechnet.

Der Chat wird über `messages` gespeichert.
Jede Nachricht gehört zu einem Hive und hat einen Sender sowie einen Empfänger.
