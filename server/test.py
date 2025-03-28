import sqlite3

def select_data(db_name):
    try:
        # Connect to the database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Construct the SQL query
        cursor.execute('''
            SELECT Products_id FROM Saling_products
            WHERE Sales_transaction_id == 1;
        ''')
        
        # Fetch all results
        rows = cursor.fetchall()
        
        # Store results in a list
        data_list = [row for row in rows]
        
        # Close the connection
        conn.close()
        
        return data_list
    except sqlite3.Error as e:
        print("Error accessing database:", e)
        return []

if __name__ == "__main__":
    db_name = "sales_management.db"  # Change to your database file
    data = select_data(db_name)
    num = data.pop(0)
    print(num[0])


