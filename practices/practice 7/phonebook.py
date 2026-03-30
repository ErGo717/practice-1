import csv
from connect import get_connection


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


def insert_contact(username, phone):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
            (username, phone)
        )
        conn.commit()
        print("Contact added successfully.")
    except Exception as e:
        conn.rollback()
        print("Error while adding contact:", e)

    cur.close()
    conn.close()


def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    added = 0
    skipped = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                username = row["username"].strip()
                phone = row["phone"].strip()

                try:
                    cur.execute(
                        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                        (username, phone)
                    )
                    added += 1
                except Exception:
                    conn.rollback()
                    skipped += 1

        conn.commit()
        print(f"CSV import finished. Added: {added}, Skipped: {skipped}")

    except FileNotFoundError:
        print("CSV file not found.")

    cur.close()
    conn.close()


def update_contact(current_username, new_username=None, new_phone=None):
    conn = get_connection()
    cur = conn.cursor()

    try:
        if new_username and new_phone:
            cur.execute("""
                UPDATE phonebook
                SET username = %s, phone = %s
                WHERE username = %s
            """, (new_username, new_phone, current_username))

        elif new_username:
            cur.execute("""
                UPDATE phonebook
                SET username = %s
                WHERE username = %s
            """, (new_username, current_username))

        elif new_phone:
            cur.execute("""
                UPDATE phonebook
                SET phone = %s
                WHERE username = %s
            """, (new_phone, current_username))

        else:
            print("Nothing to update.")
            cur.close()
            conn.close()
            return

        conn.commit()

        if cur.rowcount == 0:
            print("Contact not found.")
        else:
            print("Contact updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Error while updating:", e)

    cur.close()
    conn.close()


def query_contacts(name_filter=None, phone_prefix=None):
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT username, phone FROM phonebook WHERE 1=1"
    params = []

    if name_filter:
        query += " AND username ILIKE %s"
        params.append(f"%{name_filter}%")

    if phone_prefix:
        query += " AND phone LIKE %s"
        params.append(f"{phone_prefix}%")

    query += " ORDER BY username"

    cur.execute(query, tuple(params))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    if not rows:
        print("No contacts found.")
        return

    print("\nContacts:")
    for username, phone in rows:
        print(f"Name: {username}, Phone: {phone}")


def delete_contact(username=None, phone=None):
    conn = get_connection()
    cur = conn.cursor()

    try:
        if username:
            cur.execute("DELETE FROM phonebook WHERE username = %s", (username,))
        elif phone:
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        else:
            print("Provide username or phone.")
            cur.close()
            conn.close()
            return

        conn.commit()

        if cur.rowcount == 0:
            print("Contact not found.")
        else:
            print("Contact deleted successfully.")

    except Exception as e:
        conn.rollback()
        print("Error while deleting:", e)

    cur.close()
    conn.close()


def show_all_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT username, phone FROM phonebook ORDER BY username")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    if not rows:
        print("PhoneBook is empty.")
        return

    print("\nAll contacts:")
    for username, phone in rows:
        print(f"Name: {username}, Phone: {phone}")


def menu():
    create_table()

    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Insert contact from console")
        print("2. Insert contacts from CSV")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Show all contacts")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            phone = input("Enter phone: ").strip()
            insert_contact(username, phone)

        elif choice == "2":
            filename = input("Enter CSV filename: ").strip()
            insert_from_csv(filename)

        elif choice == "3":
            current_username = input("Enter current username: ").strip()
            new_username = input("Enter new username (or press Enter to skip): ").strip()
            new_phone = input("Enter new phone (or press Enter to skip): ").strip()

            update_contact(
                current_username,
                new_username if new_username else None,
                new_phone if new_phone else None
            )

        elif choice == "4":
            name_filter = input("Search by name contains (or press Enter to skip): ").strip()
            phone_prefix = input("Search by phone prefix (or press Enter to skip): ").strip()

            query_contacts(
                name_filter if name_filter else None,
                phone_prefix if phone_prefix else None
            )

        elif choice == "5":
            delete_by = input("Delete by username or phone? ").strip().lower()

            if delete_by == "username":
                username = input("Enter username: ").strip()
                delete_contact(username=username)
            elif delete_by == "phone":
                phone = input("Enter phone: ").strip()
                delete_contact(phone=phone)
            else:
                print("Invalid option.")

        elif choice == "6":
            show_all_contacts()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()