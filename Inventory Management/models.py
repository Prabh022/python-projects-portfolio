from database import get_connection

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)",
            (self.name, self.quantity, self.price)
        )
        conn.commit()
        conn.close()
