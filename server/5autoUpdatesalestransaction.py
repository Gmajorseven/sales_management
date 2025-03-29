import sqlite3

def updateSalestransaction():
    try:
        conn = sqlite3.connect("sales_management.db")
        cursor = conn.cursor()

        check_status = 'Pending'
        cursor.execute("SELECT DISTINCT Sales_transaction_id FROM Saling_products WHERE status = ?", (check_status,))
        bills_id = [item[0] for item in cursor.fetchall()]
        
        for i in range(len(bills_id)):
            bill_id = bills_id[i]
            cursor.execute('''
                UPDATE Sales_transaction SET st_total = (SELECT SUM(Products.price * Saling_products.buyed_qty) as st_total
                FROM Products INNER JOIN Saling_products ON Products.pro_id = Saling_products.Products_id WHERE Sales_transaction_id = ?)
                WHERE st_id = ?;
            ''', (bill_id, bill_id))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Error accessing database:", e)

def updateProductandSalingstatus():
    try:
        conn = sqlite3.connect("sales_management.db")
        cursor = conn.cursor()

        cursor.execute("SELECT DISTINCT Products_id FROM Saling_products")
        pros_id = [item[0] for item in cursor.fetchall()]

        for i in range(len(pros_id)):
            pro_id = pros_id[i]
            check_status = 'Pending'
            cursor.execute('''
                UPDATE Products SET qty = qty - (SELECT SUM(buyed_qty) as minus_qty FROM Saling_products WHERE Products_id = Products.pro_id
                AND status = ?) WHERE pro_id = ?;
            ''', (check_status, pro_id))
            new_status = 'Completed'
            cursor.execute('''
                UPDATE Saling_products SET status = ? WHERE Products_id = ?
            ''', (new_status, pro_id))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Error accessing database", e)

def main():
    updateSalestransaction()
    updateProductandSalingstatus()
    print("Update Total Sales transaction and Saling status successfully!")
if __name__ == "__main__":
    main()
