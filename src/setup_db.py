# setup_db.py
import sqlite3

def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite version:", sqlite3.version)
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
    finally:
        if conn:
            conn.close()

def create_table():
    conn = sqlite3.connect('app.db')
    try:
        c = conn.cursor()
        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id integer PRIMARY KEY, name text, email text, query text, response text)''')
        # Insert a row of data
        c.executescript("""
            INSERT INTO users VALUES (3, 'Alice Johnson', 'alice@example.com', 'Account help', 'Please verify your email address to reset your password');
            INSERT INTO users VALUES (4, 'Bob Brown', 'bob@example.com', 'Return policy', 'You have 30 days to return your purchase for a full refund');
            INSERT INTO users VALUES (5, 'Charlie Davis', 'charlie@example.com', 'Shipping options', 'We offer standard, expedited, and overnight shipping');
            INSERT INTO users VALUES (6, 'Dana White', 'dana@example.com', 'Product availability', 'That product is currently out of stock but will be available next week');
            INSERT INTO users VALUES (7, 'Evan Green', 'evan@example.com', 'Technical support', 'Please turn off your device and restart it');
        """)
        # Save (commit) the changes
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    create_connection('app.db')
    create_table()
