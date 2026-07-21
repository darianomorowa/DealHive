import os
from datetime import date, timedelta

from werkzeug.security import generate_password_hash
from database import (
    create_tables,
    insert_hive,
    insert_hive_tier,
    create_test_user,
    assign_hive_to_user,
    get_all_hives
)


# wenn eine alte lokale Datenbank existiert, löschen wir sie bewusst
# dadurch starten die Demo-Daten immer aus einem sauberen Zustand
if os.path.exists("dealhive.db"):
    os.remove("dealhive.db")


# hier erstellen wir die Tabellen neu
create_tables()


# Test-Creator für den Demo-Stand
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


# Test-Buyer für Demo-Beitritte und Käuferübersicht
test_buyers = [
    (
        "buyer_lena",
        "Lena Buyer",
        "lena.buyer@example.com",
        "test123",
        "buyer",
        "Brettspielstraße 4",
        "10119",
        "Berlin",
        "Deutschland"
    ),
    (
        "buyer_max",
        "Max Buyer",
        "max.buyer@example.com",
        "test123",
        "buyer",
        "Tabletopweg 8",
        "10245",
        "Berlin",
        "Deutschland"
    ),
    (
        "buyer_sam",
        "Sam Buyer",
        "sam.buyer@example.com",
        "test123",
        "buyer",
        "Dungeonallee 12",
        "10405",
        "Berlin",
        "Deutschland"
    )
]


creator_ids = {}
buyer_ids = {}


# hier erstellen wir die Creator und merken uns ihre IDs
for creator in test_creators:
    creator_id = create_test_user(
        creator[0],
        creator[1],
        creator[2],
        generate_password_hash(creator[3]),
        creator[4],
        creator[5],
        creator[6],
        creator[7],
        creator[8]
    )

    creator_ids[creator[0]] = creator_id


# hier erstellen wir die Buyer und merken uns ihre IDs
for buyer in test_buyers:
    buyer_id = create_test_user(
        buyer[0],
        buyer[1],
        buyer[2],
        generate_password_hash(buyer[3]),
        buyer[4],
        buyer[5],
        buyer[6],
        buyer[7],
        buyer[8]
    )

    buyer_ids[buyer[0]] = buyer_id

def future_deadline(days_from_today):
    return (
        date.today() + timedelta(days=days_from_today)
    ).isoformat()


# Demo-Hives mit Basispreis, Mindestmenge, aktuellen Bestellungen und Rabattstaffeln
# current_participants entspricht hier der Summe der unten eingetragenen Buyer-Mengen
test_hives = [
    {
        "title": "Drachenwürfel-Set",
        "game_system": "D&D",
        "short_description": "Handgemachtes Würfelset mit Drachenmotiv.",
        "description": "Ein 7-teiliges Resin-Würfelset mit Drachenmotiv für Fantasy-Rollenspiele.",
        "deadline": future_deadline(30),
        "min_participants": 20,
        "base_price": 35.00,
        "creator": "dice_creator",
        "buyers": [
            ("buyer_lena", 6),
            ("buyer_max", 8),
            ("buyer_sam", 4)
        ],
        "tiers": [
            (20, 5),
            (40, 10),
            (60, 20)
        ]
    },
    {
        "title": "Dungeon-Terrain-Set",
        "game_system": "D&D",
        "short_description": "Modulares Terrain für Dungeon-Runden.",
        "description": "Ein Set aus modularen Dungeon-Teilen für Pen-&-Paper-Kämpfe, Burgen und Verliese.",
        "deadline": future_deadline(40),
        "min_participants": 40,
        "base_price": 89.00,
        "creator": "terrain_creator",
        "buyers": [
            ("buyer_lena", 10),
            ("buyer_max", 12),
            ("buyer_sam", 9)
        ],
        "tiers": [
            (40, 8),
            (80, 15)
        ]
    },
    {
        "title": "Holz-Würfelturm",
        "game_system": "Systemunabhängig",
        "short_description": "Schlichter Würfelturm aus Holz.",
        "description": "Ein stabiler Würfelturm aus Holz für Brettspiele, TTRPGs und gemütliche Spielabende.",
        "deadline": future_deadline(50),
        "min_participants": 25,
        "base_price": 24.99,
        "creator": "dice_creator",
        "buyers": [
            ("buyer_lena", 5),
            ("buyer_max", 4),
            ("buyer_sam", 3)
        ],
        "tiers": [
            (25, 10),
            (50, 18)
        ]
    },
    {
        "title": "Goblin-Miniaturen-Set",
        "game_system": "Warhammer Fantasy",
        "short_description": "Kleine Goblin-Miniaturen zum Bemalen.",
        "description": "Ein Set aus Goblin-Miniaturen für Tabletop-Spiele, Bemalprojekte und kleine Fantasy-Armeen.",
        "deadline": future_deadline(60),
        "min_participants": 30,
        "base_price": 49.99,
        "creator": "miniature_creator",
        "buyers": [
            ("buyer_lena", 7),
            ("buyer_max", 9),
            ("buyer_sam", 6)
        ],
        "tiers": [
            (30, 10),
            (60, 20)
        ]
    },
    {
        "title": "Zauberbuch-Kartenhalter",
        "game_system": "Pathfinder",
        "short_description": "Kartenhalter im Zauberbuch-Stil.",
        "description": "Ein Kartenhalter für Zauber-, Item- oder Monsterkarten im Look eines alten Zauberbuchs.",
        "deadline": future_deadline(70),
        "min_participants": 15,
        "base_price": 19.99,
        "creator": "dice_creator",
        "buyers": [
            ("buyer_lena", 3),
            ("buyer_max", 4),
            ("buyer_sam", 2)
        ],
        "tiers": [
            (15, 8),
            (30, 15)
        ]
    },
    {
        "title": "Kampagnen-Token-Set",
        "game_system": "D&D",
        "short_description": "Token für Zustände und Gegner.",
        "description": "Ein Token-Set für Zustände, Gegner, Marker und wichtige Momente in längeren Kampagnen.",
        "deadline": future_deadline(80),
        "min_participants": 50,
        "base_price": 14.99,
        "creator": "terrain_creator",
        "buyers": [
            ("buyer_lena", 14),
            ("buyer_max", 18),
            ("buyer_sam", 12)
        ],
        "tiers": [
            (50, 10),
            (100, 20)
        ]
    },
    {
        "title": "Resin-Würfel Nebelblau",
        "game_system": "Systemunabhängig",
        "short_description": "Blaues Resin-Würfelset mit Nebel-Effekt.",
        "description": "Ein handgemachtes Würfelset aus Resin mit blauem Nebel-Effekt für verschiedene Rollenspielsysteme.",
        "deadline": future_deadline(90),
        "min_participants": 20,
        "base_price": 32.50,
        "creator": "dice_creator",
        "buyers": [
            ("buyer_lena", 2),
            ("buyer_max", 3),
            ("buyer_sam", 2)
        ],
        "tiers": [
            (20, 10),
            (40, 18)
        ]
    },
    {
        "title": "Tabletop-Spielmatte",
        "game_system": "Warhammer 40k",
        "short_description": "Bedruckte Spielmatte für Gefechte.",
        "description": "Eine Spielmatte für Tabletop-Gefechte mit Geländeoptik.",
        "deadline": future_deadline(100),
        "min_participants": 30,
        "base_price": 59.99,
        "creator": "miniature_creator",
        "buyers": [
            ("buyer_lena", 5),
            ("buyer_max", 6),
            ("buyer_sam", 5)
        ],
        "tiers": [
            (30, 10),
            (60, 18)
        ]
    },
    {
        "title": "Mimic-Würfelturm",
        "game_system": "D&D",
        "short_description": "Würfelturm in Form eines Mimics.",
        "description": "Ein Würfelturm im Mimic-Design für Fantasy-Rollenspiele und Spieltische mit etwas Chaos.",
        "deadline": future_deadline(110),
        "min_participants": 25,
        "base_price": 39.99,
        "creator": "dice_creator",
        "buyers": [
            ("buyer_lena", 4),
            ("buyer_max", 4),
            ("buyer_sam", 3)
        ],
        "tiers": [
            (25, 10),
            (50, 20)
        ]
    },
    {
        "title": "Abenteuer-Modul: Krypta der Bienenkönigin",
        "game_system": "Pathfinder",
        "short_description": "Kurzes Abenteuer-Modul für eine Session.",
        "description": "Ein kurzes Fantasy-Abenteuer rund um eine verlassene Krypta und eine wütende Bienenkönigin.",
        "deadline": future_deadline(120),
        "min_participants": 20,
        "base_price": 9.99,
        "creator": "terrain_creator",
        "buyers": [
            ("buyer_lena", 5),
            ("buyer_max", 6),
            ("buyer_sam", 3)
        ],
        "tiers": [
            (20, 15),
            (50, 25)
        ]
    }
]


# hier speichern wir alle Demo-Hives, Creator-Zuordnungen, Buyer-Zuordnungen und Rabattstaffeln
for hive in test_hives:
    current_participants = 0

    for buyer in hive["buyers"]:
        current_participants += buyer[1]

    new_hive_id = insert_hive(
        hive["title"],
        hive["game_system"],
        hive["short_description"],
        hive["description"],
        hive["deadline"],
        current_participants,
        hive["min_participants"],
        hive["base_price"]
    )

    # hier ordnen wir den Hive einem Creator zu
    assign_hive_to_user(
        creator_ids[hive["creator"]],
        new_hive_id,
        "creator"
    )

    # hier speichern wir die Rabattstaffeln für den Hive
    for tier in hive["tiers"]:
        insert_hive_tier(
            new_hive_id,
            tier[0],
            tier[1]
        )

    # hier ordnen wir Buyer mit konkreter Menge zu
    # current_participants wurde oben schon passend als Summe dieser Mengen gesetzt
    for buyer in hive["buyers"]:
        assign_hive_to_user(
            buyer_ids[buyer[0]],
            new_hive_id,
            "buyer",
            quantity=buyer[1]
        )


# Ausgabe zur schnellen Kontrolle im Terminal
hives = get_all_hives()

for hive in hives:
    print(
        hive["id"],
        hive["title"],
        hive["game_system"],
        hive["current_participants"],
        "/",
        hive["min_participants"],
        "Basispreis:",
        hive["base_price"]
    )

print("Demo-Datenbank wurde neu erstellt.")
print("Creator, Buyer, Hives, Mengen und Rabattstaffeln wurden gespeichert.")