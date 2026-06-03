from database import create_tables, insert_test_hive, get_all_hives



create_tables()


insert_test_hive()

# alle Hives wieder aus der Datenbank
hives = get_all_hives()

# was in der Datenbank steht ausgeben
for hive in hives:
    print(hive["id"], hive["title"])

#Ausgabe 1 Drachenwürfel-Set
