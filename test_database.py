from database import create_tables, insert_test_hives, get_all_hives



create_tables()


insert_test_hives()

# alle Hives wieder aus der Datenbank
hives = get_all_hives()

# was in der Datenbank steht ausgeben
for hive in hives:
    print(
        hive["id"],
        hive["title"],
        hive["deadline"],
        hive["current_participants"],
        "/",
        hive["min_participants"]
    )
#Ausgabe 1 Drachenwürfel-Set
