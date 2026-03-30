from connect import get_connection


def print_rows(rows):
    if not rows:
        print("No contacts found.")
        return

    print("\nContacts:")
    for row in rows:
        print(f"ID: {row[0]}, Username: {row[1]}, Phone: {row[2]}")


def search_contacts():
    pattern = input("Enter pattern to search: ").strip()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    print_rows(rows)


def upsert_one_contact():
    username = input("Enter username: ").strip()
    phone = input("Enter phone: ").strip()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (username, phone))
    conn.commit()

    cur.close()
    conn.close()

    print("Upsert completed.")


def bulk_upsert_contacts():
    n = int(input("How many contacts do you want to enter? "))
    usernames = []
    phones = []

    for i in range(n):
        print(f"\nContact {i + 1}")
        usernames.append(input("Username: ").strip())
        phones.append(input("Phone: ").strip())

    conn = get_connection()
    cur = conn.cursor()

    bad_rows = []

    cur.execute(
        "CALL bulk_upsert_contacts(%s, %s, %s)",
        (usernames, phones, [])
    )

    try:
        result = cur.fetchone()
        if result and result[0]:
            bad_rows = result[0]
    except Exception:
        bad_rows = []

    conn.commit()
    cur.close()
    conn.close()

    print("Bulk upsert finished.")
    if bad_rows:
        print("Incorrect data:")
        for item in bad_rows:
            print("-", item)
    else:
        print("No incorrect data.")


def show_paginated():
    limit_value = int(input("Enter LIMIT: "))
    offset_value = int(input("Enter OFFSET: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s)",
        (limit_value, offset_value)
    )
    rows = cur.fetchall()

    cur.close()
    conn.close()

    print_rows(rows)


def delete_contact():
    delete_by = input("Delete by username or phone? ").strip().lower()

    conn = get_connection()
    cur = conn.cursor()

    if delete_by == "username":
        username = input("Enter username: ").strip()
        cur.execute("CALL delete_contact_proc(%s, %s)", (username, None))
    elif delete_by == "phone":
        phone = input("Enter phone: ").strip()
        cur.execute("CALL delete_contact_proc(%s, %s)", (None, phone))
    else:
        print("Invalid option.")
        cur.close()
        conn.close()
        return

    conn.commit()
    cur.close()
    conn.close()

    print("Delete completed.")


def menu():
    while True:
        print("\n--- PRACTICE 8 MENU ---")
        print("1. Search contacts by pattern")
        print("2. Upsert one contact")
        print("3. Bulk upsert contacts")
        print("4. Show contacts with pagination")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_contacts()
        elif choice == "2":
            upsert_one_contact()
        elif choice == "3":
            bulk_upsert_contacts()
        elif choice == "4":
            show_paginated()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()