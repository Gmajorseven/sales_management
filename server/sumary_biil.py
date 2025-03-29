import sqlite3

def sumary_bill():
    try:
        conn = sqlite3.connect("sales_management.db")
        cursor = conn.cursor()

        cursor.execute("SELECT Sales_transaction_id FROM Saling_products WHERE status == 'Pending'")
        bills_id = [item[0] for item in cursor.fetchall()]
        bills_id = set(bills_id)
        bills_id = list(bills_id)

        for i in range(len(bills_id)):
            total = 0
            bill_id = bills_id[i]
            cursor.execute("SELECT Products_id FROM Saling_products WHERE Sales_transaction_id == ?", (bill_id,))
            pros_id = [item[0] for item in cursor.fetchall()]
            cursor.execute("SELECT buyed_qty FROM Saling_products WHERE Sales_transaction_id == ?", (bill_id,))
            buyed_qty = [item[0] for item in cursor.fetchall()]

            for j in range(len(pros_id)):
                pro_id = pros_id[j]
                cursor.execute("SELECT price FROM Products WHERE pro_id == ?", (pro_id,))
                price = [item[0] for item in cursor.fetchall()]
                total += price[0]*buyed_qty[0]
                #minus_qty = buyed_qty[0]
                #cursor.execute("UPDATE Products SET qty = qty - ? WHERE pro_id == ? ", (minus_qty, pro_id))
                buyed_qty.pop(0)
            rounded_total = round(total, 2)
            print(bill_id)
            print(rounded_total)

            #cursor.execute("UPDATE Sales_transaction SET st_total = ? WHERE st_id = ?", (rounded_total, bill_id))
            #cursor.execute("UPDATE Saling_products SET status == 'Completed' WHERE Sales_transaction_id == ?", (bill_id))
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Error accessing database:", e)
        return []

def main():
    sumary_bill()

if __name__ == "__main__":
    main()
