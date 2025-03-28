import pysqlite3 as sqlite3
from faker import Faker

fake = Faker()

def create_database():
    conn = sqlite3.connect("sales_management.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Salespersons (
            sp_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            name VARCHAR(30),
            email VARCHAR(30),
            tel VARCHAR(30),
            salary NUMERIC(10, 2)
        )
    ''')

    conn.commit()
    conn.close()

def insert_salespersons(n):
    conn = sqlite3.connect("sales_management.db")
    cursor = conn.cursor()

    for _ in range(n):
        name = fake.name()
        email = fake.unique.email()
        tel = fake.phone_number()
        salary = round(fake.random_number(digits=5, fix_len=True) * 0.01, 2)

        cursor.execute("INSERT INTO Salespersons(name, email, tel, salary) VALUES(?, ?, ?, ?)", (name, email, tel, salary))

    conn.commit()
    conn.close()

def main():
    create_database()
    insert_salespersons(10)
    print("Database and salespersons records created successfully!")

if __name__ == "__main__":
    main()
