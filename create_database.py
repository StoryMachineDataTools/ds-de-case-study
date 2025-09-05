import sqlite3


conn = sqlite3.connect("social_media_database.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE social_profiles (
    profile_name TEXT PRIMARY KEY,
    profile_url TEXT NOT NULL,
    follower_count INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")


conn.commit()
conn.close()