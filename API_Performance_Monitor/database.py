import sqlite3

DATABASE = "performance.db"


def create_database():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS api_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            api_url TEXT NOT NULL,
            response_time REAL NOT NULL,
            status_code INTEGER,
            status TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_metric(api_url, response_time, status_code, status):
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO api_metrics
        (api_url, response_time, status_code, status)
        VALUES (?, ?, ?, ?)
    """, (api_url, response_time, status_code, status))

    conn.commit()
    conn.close()


def get_metrics():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, api_url, response_time, status_code, status, timestamp
        FROM api_metrics
        ORDER BY id DESC
    """)

    metrics = cursor.fetchall()

    conn.close()

    return metrics

if __name__ == "__main__":
    create_database()
    print("Database created successfully!")