import pysqlite3 as sqlite3
import random
from datetime import datetime

def create_database(): 
    conn = sqlite3.connect("sales_management.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sales_transaction (
            st_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            st_date DATE DEFAULT (datetime('now', 'localtime')),
            st_total NUMERIC(10, 2),
            cus_id INTEGER,
            sp_id INTEGER,
            FOREIGN KEY (cus_id) REFERENCES Customers (cus_id),
            FOREIGN KEY (sp_id) REFERENCES Salespersons (sp_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Saling_products (
            Sales_transaction_id INTEGER,
            Products_id INTEGER,
            buyed_qty INTEGER,
            status TEXT CHECK(status IN ('Pending', 'Completed')) NOT NULL DEFAULT 'Pending',
            FOREIGN KEY (Sales_transaction_id) REFERENCES Sales_transaction (st_id),
            FOREIGN KEY (Products_id) REFERENCES Products (pro_id),
            PRIMARY KEY (Sales_transaction_id, Products_id)
        )
    ''')

    conn.commit()
    conn.close()

def insert_salestransaction(n=100):
    conn = sqlite3.connect("sales_management.db")
    cursor = conn.cursor()
    for _ in range(n):
        cus_id = random.randint(1, 100)
        sp_id = random.randint(1, 10)

        cursor.execute("INSERT INTO Sales_transaction (cus_id, sp_id) VALUES (?, ?)", (cus_id, sp_id))

    conn.commit()
    conn.close()

def insert_salingproducts(n=100):
    conn = sqlite3.connect("sales_management.db")
    cursor = conn.cursor()
    for i in range(1, n+1):
        st_id = i
        for j in range(random.randint(1, 5)):
            pro_id = random.randint(1, 49)
            buyed_qty = random.randint(1, 3)

            cursor.execute("INSERT OR IGNORE INTO Saling_products (Sales_transaction_id, Products_id, buyed_qty) VALUES (?, ?, ?)", (st_id, pro_id, buyed_qty))

    conn.commit()
    conn.close()

def main():
    create_database()
    insert_salestransaction(50)
    insert_salingproducts(50)
    print("Database sales transaction and saling products records created successfully!")

if __name__ == "__main__":
    main()



