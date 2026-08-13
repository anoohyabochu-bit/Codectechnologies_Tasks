import sqlite3

DATABASE = "smart_home.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            device_type TEXT NOT NULL,
            status TEXT DEFAULT 'OFF'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id INTEGER NOT NULL,
            action TEXT NOT NULL,
            schedule_time TEXT NOT NULL,
            FOREIGN KEY(device_id) REFERENCES devices(id)
        )
    """)

    # Add default devices only if the table is empty
    cursor.execute("SELECT COUNT(*) FROM devices")
    count = cursor.fetchone()[0]

    if count == 0:
        devices = [
            ("Living Room Light", "Light", "OFF"),
            ("Bedroom Light", "Light", "OFF"),
            ("Living Room Fan", "Fan", "OFF"),
            ("Kitchen Light", "Light", "OFF")
        ]

        cursor.executemany(
            "INSERT INTO devices (name, device_type, status) VALUES (?, ?, ?)",
            devices
        )

    connection.commit()
    connection.close()


def get_devices():
    connection = get_connection()
    devices = connection.execute(
        "SELECT * FROM devices"
    ).fetchall()
    connection.close()

    return devices


def update_device_status(device_id, status):
    connection = get_connection()

    connection.execute(
        "UPDATE devices SET status = ? WHERE id = ?",
        (status, device_id)
    )

    connection.commit()
    connection.close()


def add_schedule(device_id, action, schedule_time):
    connection = get_connection()

    connection.execute(
        """
        INSERT INTO schedules (device_id, action, schedule_time)
        VALUES (?, ?, ?)
        """,
        (device_id, action, schedule_time)
    )

    connection.commit()
    connection.close()


def get_schedules():
    connection = get_connection()

    schedules = connection.execute("""
        SELECT schedules.*, devices.name
        FROM schedules
        JOIN devices ON schedules.device_id = devices.id
        ORDER BY schedule_time
    """).fetchall()

    connection.close()

    return schedules


def delete_schedule(schedule_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM schedules WHERE id = ?",
        (schedule_id,)
    )

    connection.commit()
    connection.close()