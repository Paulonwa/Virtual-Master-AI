import sqlite3

DATABASE_NAME = "virtualmaster.db"


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # Teams
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_name TEXT UNIQUE,
            short_name TEXT,
            rating REAL DEFAULT 1000
        )
        """)

        # Fixtures
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS fixtures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week INTEGER,
            home_team TEXT,
            away_team TEXT,
            kickoff TEXT,
            status TEXT
        )
        """)

        # Results
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fixture_id INTEGER,
            home_goals INTEGER,
            away_goals INTEGER,
            winner TEXT,
            btts INTEGER,
            over15 INTEGER,
            over25 INTEGER,
            over35 INTEGER
        )
        """)

        # Statistics
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS statistics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team TEXT UNIQUE,
            games INTEGER DEFAULT 0,
            wins INTEGER DEFAULT 0,
            draws INTEGER DEFAULT 0,
            losses INTEGER DEFAULT 0,
            goals_for INTEGER DEFAULT 0,
            goals_against INTEGER DEFAULT 0
        )
        """)

        # Predictions
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fixture_id INTEGER,
            home_probability REAL,
            draw_probability REAL,
            away_probability REAL,
            btts_probability REAL,
            over25_probability REAL,
            confidence REAL,
            model_used TEXT,
            prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = Database()
    db.create_tables()
    print("✅ VirtualMaster database created successfully.")
    db.close()
