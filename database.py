import sqlite3

# Create database connection
conn = sqlite3.connect("finance.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    type TEXT
)
""")
conn.commit()

def add_transaction(date, category, amount, trans_type):
    cursor.execute("INSERT INTO transactions (date, category, amount, type) VALUES (?, ?, ?, ?)", 
                   (date, category, amount, trans_type))
    conn.commit()

def get_transactions():
    cursor.execute("SELECT * FROM transactions")
    return cursor.fetchall()

# Remove a Transaction
def remove_transaction(transaction_id):
    """Corrected function to delete transactions from the correct database."""
    conn = sqlite3.connect("finance.db")  # Corrected database name
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
    conn.commit()
    conn.close()
