"""
db_handler.py
Handles SQLite database operations for StudyWise AI.
"""

import sqlite3
import os
from datetime import datetime


DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "studywise.db"
)


def init_db():
    """
    Creates the materials table if it does not already exist.
    """

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            filename TEXT NOT NULL,
            upload_date TEXT NOT NULL,
            extracted_text TEXT NOT NULL,
            page_count INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()
    init_quiz_table()


def add_material(subject, filename, extracted_text, page_count=0):
    """
    Adds a study material to the database.
    Returns the ID of the new material.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO materials
        (subject, filename, upload_date, extracted_text, page_count)
        VALUES (?, ?, ?, ?, ?)
    """, (
        subject,
        filename,
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        extracted_text,
        page_count
    ))

    conn.commit()

    new_id = cursor.lastrowid

    conn.close()

    return new_id


def get_all_materials():
    """
    Returns all materials without the full extracted text.
    """

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, subject, filename, upload_date, page_count
        FROM materials
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def get_material_by_id(material_id):
    """
    Returns one material including its extracted text.
    """

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM materials WHERE id = ?",
        (material_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None


def get_materials_by_subject(subject):
    """
    Returns materials belonging to a particular subject.
    """

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, subject, filename, upload_date, page_count
        FROM materials
        WHERE subject = ?
        ORDER BY id DESC
    """, (subject,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def delete_material(material_id):
    """
    Deletes a material from the database.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM materials WHERE id = ?",
        (material_id,)
    )

    conn.commit()
    conn.close()


def init_quiz_table():
    """
    Creates the quiz_results table if it does not already exist.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            material_id INTEGER,
            subject TEXT,
            score INTEGER,
            total INTEGER,
            percentage REAL,
            taken_date TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_quiz_result(material_id, subject, score, total, percentage):
    """
    Saves one quiz attempt's result.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO quiz_results
        (material_id, subject, score, total, percentage, taken_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        material_id,
        subject,
        score,
        total,
        percentage,
        datetime.now().strftime("%Y-%m-%d %H:%M")
    ))

    conn.commit()
    conn.close()


def get_quiz_history():
    """
    Returns all past quiz results, most recent first.
    """

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM quiz_results ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
