# src/db_helpers.py
import sqlite3
from typing import List, Tuple, Any, Dict

DB_PATH = "db/food.db"

def get_conn():
    return sqlite3.connect(r"C:\Users\abinsanal\Videos\local food waste\db\food.db")

def run_query(sql: str, params: Tuple = ()) -> List[Tuple]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    return rows

# --- Example CRUD ---
def add_provider(name: str, type_: str, address: str, city: str, contact: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO providers (name, type, address, city, contact)
        VALUES (?, ?, ?, ?, ?)
    """, (name, type_, address, city, contact))
    conn.commit()
    conn.close()
def update_provider(provider_id: int, name: str, type_: str, address: str, city: str, contact: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE providers
        SET name=?, type=?, address=?, city=?, contact=?
        WHERE provider_id=?
    """, (name, type_, address, city, contact, provider_id))
    conn.commit()
    conn.close()

def delete_provider(provider_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM providers WHERE provider_id=?", (provider_id,))
    conn.commit()
    conn.close()


def get_providers():
    return run_query("SELECT * FROM providers")
