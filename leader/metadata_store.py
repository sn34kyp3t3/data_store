# metadata_store.py

import sqlite3


class MetadataManager:
    def __init__(self, db_path="metadata.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (
            file_name TEXT PRIMARY KEY,
            chunk_ids TEXT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            chunk_id TEXT PRIMARY KEY,
            data_nodes TEXT,
            checksum TEXT
        )
        """)
        self.conn.commit()

    def add_file(self, file_name, chunk_ids):
        self.cursor.execute(
            "INSERT INTO files VALUES (?, ?)", (file_name, chunk_ids))
        self.conn.commit()

    def add_chunk(self, chunk_id, data_nodes, checksum):
        self.cursor.execute(
            "INSERT INTO chunks VALUES (?, ?, ?)", (chunk_id,
                                                    data_nodes, checksum)
        )
        self.conn.commit()

    def get_file_chunks(self, file_name):
        self.cursor.execute(
            "SELECT chunk_ids FROM files WHERE file_name=?", (file_name,)
        )
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_chunk_nodes(self, chunk_id):
        self.cursor.execute(
            "SELECT data_nodes FROM chunks WHERE chunk_id=?", (chunk_id,)
        )
        result = self.cursor.fetchone()
        return result[0] if result else None
