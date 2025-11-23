import sqlite3
import pickle

from Assessment import Assessment
from Course import Course

class CourseService:

    conn_str: str

    def __init__(self, conn_str: str):
        conn = sqlite3.connect(conn_str)
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            Course_Id INTEGER PRIMARY KEY,
            Course_Name TEXT,
            Desired_Mark REAL,
            Assessments BLOB NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Assessments (
            Assessment_Id INTEGER PRIMARY KEY,
            Assessment_Name TEXT,
            Assessment_Mark REAL,
            Assessments_Weight REAL,
            Course_Id INTEGER NOT NULL
            FOREIGN KEY (Course_Id) REFERENCES Hospital(Course_Id)
        );
        """)

