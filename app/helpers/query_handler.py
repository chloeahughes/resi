import sqlite3

def fetch_data(query):
    connection = sqlite3.connect("data/my_database.db")
    cursor = connection.cursor()

    # Basic search logic
    cursor.execute("SELECT * FROM growth_data WHERE city LIKE ?", (f"%{query}%",))
    results = cursor.fetchall()
    connection.close()

    # Convert to dictionary
    return [{"city": row[0], "growth_rate": row[1]} for row in results]
