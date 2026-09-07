from database import get_connection
from tabulate import tabulate

def generate_weekly_report():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, quantity, price FROM inventory")
    items = cursor.fetchall()
    conn.close()

    print("\n📊 Weekly Inventory Report")
    print(tabulate(items, headers=["Item", "Quantity", "Price"], tablefmt="grid"))
