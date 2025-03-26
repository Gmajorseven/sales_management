import pysqlite3 as sqlite3
from faker import Faker

fake = Faker()

def create_database():
    conn = sqlite3.connect("sales_management.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers(
            cus_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            name VARCHAR(30),
            email VARCHAR(30),
            tel VARCHAR(30)
        )
    ''')

    conn.commit()
    conn.close()

def insert_customers(n=100):
    conn = sqlite3.connect("sales_management.db")
    cursor = conn.cursor()

    for _ in range(n):
        name = fake.name()
        email = fake.unique.email()
        tel = fake.phone_number()

        cursor.execute("INSERT INTO Customers(name, email, tel) VALUES(?, ?, ?)", (name, email, tel))

    conn.commit()
    conn.close()

def main():
    create_database()
    insert_customers(100)
    print("Database and customer records created successfully!")

if __name__ == "__main__":
    main()
