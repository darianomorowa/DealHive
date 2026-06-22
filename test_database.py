import random

from database import (
    create_tables,
    insert_test_hives,
    get_all_hives,
    create_test_user,
    assign_hive_to_user
)

# diese Liste wurde komplett mit KI erstellt
# Reihenfolge ist wichtig:
# title, game_system, short_description, description, deadline, current_participants, min_participants
test_hives = [
    (
        "Drachenwürfel-Set",
        "D&D",
        "Handgemachtes Würfelset mit Drachenmotiv.",
        "Ein 7-teiliges Resin-Würfelset mit Drachenmotiv für Fantasy-Rollenspiele.",
        "31.05.2026",
        18,
        20
    ),
    (
        "Dungeon-Terrain-Set",
        "D&D",
        "Modulares Terrain für Dungeon-Runden.",
        "Ein Set aus modularen Dungeon-Teilen für Pen-&-Paper-Kämpfe, Burgen und Verliese.",
        "28.05.2026",
        31,
        40
    ),
    (
        "Holz-Würfelturm",
        "Systemunabhängig",
        "Schlichter Würfelturm aus Holz.",
        "Ein stabiler Würfelturm aus Holz für Brettspiele, TTRPGs und gemütliche Spielabende.",
        "02.06.2026",
        12,
        25
    ),
    (
        "Goblin-Miniaturen-Set",
        "Warhammer Fantasy",
        "Kleine Goblin-Miniaturen zum Bemalen.",
        "Ein Set aus Goblin-Miniaturen für Tabletop-Spiele, Bemalprojekte und kleine Fantasy-Armeen.",
        "05.06.2026",
        22,
        30
    ),
    (
        "Zauberbuch-Kartenhalter",
        "Pathfinder",
        "Kartenhalter im Zauberbuch-Stil.",
        "Ein Kartenhalter für Zauber-, Item- oder Monsterkarten im Look eines alten Zauberbuchs.",
        "10.06.2026",
        9,
        15
    ),
    (
        "Kampagnen-Token-Set",
        "D&D",
        "Token für Zustände und Gegner.",
        "Ein Token-Set für Zustände, Gegner, Marker und wichtige Momente in längeren Kampagnen.",
        "15.06.2026",
        44,
        50
    ),
    (
        "Resin-Würfel Nebelblau",
        "Systemunabhängig",
        "Blaues Resin-Würfelset mit Nebel-Effekt.",
        "Ein handgemachtes Würfelset aus Resin mit blauem Nebel-Effekt für verschiedene Rollenspielsysteme.",
        "20.06.2026",
        7,
        20
    ),
    (
        "Tabletop-Spielmatte",
        "Warhammer 40k",
        "Bedruckte Spielmatte für Gefechte.",
        "Eine Spielmatte für Tabletop-Gefechte mit Geländeoptik.",
        "25.06.2026",
        16,
        30
    ),
    (
        "Mimic-Würfelturm",
        "D&D",
        "Würfelturm in Form eines Mimics.",
        "Ein Würfelturm im Mimic-Design für Fantasy-Rollenspiele und Spieltische mit etwas Chaos.",
        "30.06.2026",
        11,
        25
    ),
    (
        "Abenteuer-Modul: Krypta der Bienenkönigin",
        "Pathfinder",
        "Kurzes Abenteuer-Modul für eine Session.",
        "Ein kurzes Fantasy-Abenteuer rund um eine verlassene Krypta und eine wütende Bienenkönigin.",
        "05.07.2026",
        14,
        20
    ),
]


# hier erstellen wir die Tabellen, falls sie noch nicht existieren
create_tables()

# hier geben wir unsere Testdaten-Liste an die Insert-Funktion weiter
insert_test_hives(test_hives)

# damit die zufällige Zuordnung bei jedem Ausführen gleich bleibt
# dadurch ist es für Tests nicht komplett chaotisch
random.seed(42)

# hier erstellen wir mehrere Creator mit echten Datenbank-IDs
test_creators = [
    (
        "dice_creator",
        "Dice Creator",
        "dice.creator@example.com",
        "test123",
        "creator",
        "Würfelweg 1",
        "10115",
        "Berlin",
        "Deutschland"
    ),
    (
        "terrain_creator",
        "Terrain Creator",
        "terrain.creator@example.com",
        "test123",
        "creator",
        "Bastelstraße 7",
        "10243",
        "Berlin",
        "Deutschland"
    ),
    (
        "miniature_creator",
        "Miniature Creator",
        "miniature.creator@example.com",
        "test123",
        "creator",
        "Figurenallee 12",
        "10405",
        "Berlin",
        "Deutschland"
    )
]

creator_ids = []

# hier erstellen wir die Creator und speichern ihre echten IDs
for creator in test_creators:
    creator_id = create_test_user(
        creator[0],
        creator[1],
        creator[2],
        creator[3],
        creator[4],
        creator[5],
        creator[6],
        creator[7],
        creator[8]
    )

    creator_ids.append(creator_id)

# alle Hives wieder aus der Datenbank holen
hives = get_all_hives()

# hier ordnen wir jedem Hive zufällig einen echten Creator zu
for hive in hives:
    creator_id = random.choice(creator_ids)
    assign_hive_to_user(creator_id, hive["id"], "creator")

# was in der Datenbank steht ausgeben
for hive in hives:
    print(
        hive["id"],
        hive["title"],
        hive["game_system"],
        hive["short_description"],
        hive["deadline"],
        hive["current_participants"],
        "/",
        hive["min_participants"]
    )

print("Creator wurden mit echten Datenbank-IDs erstellt.")
print("Creator-Hive-Zuordnung wurde erstellt.")