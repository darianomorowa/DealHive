from werkzeug.security import generate_password_hash, check_password_hash

from database import assign_hive_to_user


def test_password_hashing():
    password = "test123"

    hashed_password = generate_password_hash(password)

    assert hashed_password != password
    assert check_password_hash(hashed_password, password)

    print("✓ Passwort-Hashing Test erfolgreich")


def test_invalid_relation_type():
    try:
        assign_hive_to_user(
            user_id=1,
            hive_id=1,
            relation_type="invalid"
        )
        print("✗ Ungültige Rolle wurde nicht abgelehnt")
    except ValueError:
        print("✓ Ungültige Rolle wird korrekt abgelehnt")


def test_invalid_quantity():
    try:
        assign_hive_to_user(
            user_id=1,
            hive_id=1,
            relation_type="buyer",
            quantity=0
        )
        print("✗ Ungültige Menge wurde nicht abgelehnt")
    except ValueError:
        print("✓ Ungültige Menge wird korrekt abgelehnt")


if __name__ == "__main__":
    test_password_hashing()
    test_invalid_relation_type()
    test_invalid_quantity()

    print("Alle Funktionstests abgeschlossen.")
