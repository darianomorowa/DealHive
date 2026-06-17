from database import (
    create_tables,
    insert_test_hives,
    get_all_hives,
    create_user_with_id,
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
        "Warhammer",
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
        "Warhammer",
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

# hier erstellen wir unseren Demo-Creator mit fester user_id 0
demo_creator_id = create_user_with_id(
    0,
    "demo_creator",
    "Demo Creator",
    "demo@example.com",
    "test_hash",
    "creator",
    "Musterstraße 1",
    "10115",
    "Berlin",
    "Deutschland"
)

# hier ordnen wir dem Demo-Creator drei Hives als Creator zu
assign_hive_to_user(demo_creator_id, 1, "creator")
assign_hive_to_user(demo_creator_id, 2, "creator")
assign_hive_to_user(demo_creator_id, 6, "creator")

# hier erstellen wir einen Demo-Buyer mit fester user_id 1
demo_buyer_id = create_user_with_id(
    1,
    "demo_buyer",
    "Demo Buyer",
    "buyer@example.com",
    "test_hash",
    "buyer",
    "Beispielstraße 5",
    "10117",
    "Berlin",
    "Deutschland"
)

# hier ordnen wir dem Demo-Buyer ein paar Hives als beigetretene Hives zu
assign_hive_to_user(demo_buyer_id, 3, "buyer")
assign_hive_to_user(demo_buyer_id, 4, "buyer")
assign_hive_to_user(demo_buyer_id, 7, "buyer")

# alle Hives wieder aus der Datenbank holen
hives = get_all_hives()

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

print("Demo-Creator mit user_id 0 wurde erstellt.")
print("Creator-Hive-Zuordnung wurde erstellt.")
print("Demo-Buyer mit user_id 1 wurde erstellt.")
print("Buyer-Hive-Zuordnung wurde erstellt.")