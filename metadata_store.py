import sqlite3

conn = sqlite3.connect("metadata.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS files (
    file_name TEXT PRIMARY KEY,
    chunk_ids TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS chunks (
    chunk_id TEXT PRIMARY KEY,
    data_nodes TEXT,
    checksum TEXT
)
""")

conn.commit()
