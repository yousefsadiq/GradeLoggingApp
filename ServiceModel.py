import sqlite3
import pickle

from AssessmentModel import Assessment
from CourseModel import Course

class CourseService:

    conn_str: str

    def __init__(self, conn_str: str):
        self.conn_str = conn_str
        conn = sqlite3.connect(self.conn_str)
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            Course_Id INTEGER PRIMARY KEY,
            Course_Name TEXT,
            Desired_Mark REAL
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

        conn.commit()
        conn.close()

    def add_course(self, course: Course) -> int:
        """
        Adds a new course to the database and returns the new Course_Id.
        """
        conn = sqlite3.connect(self.conn_str)
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO Course (Course_Name, Desired_Mark)
        VALUES (?, ?)
        """, (course.get_name(), course.desired_mark))

        new_id = cur.lastrowid
        conn.commit()
        conn.close()
        return new_id

    def update_course(self, course_id: int, course: Course) -> None:
        """
        Updates the name and desired mark of a specific course.
        """
        conn = sqlite3.connect(self.conn_str)
        cur = conn.cursor()

        cur.execute("""
        UPDATE Course
        SET Course_Name = ?, Desired_Mark = ?
        WHERE Course_Id = ?
        """, (course.get_name(), course.desired_mark, course_id))

        conn.commit()
        conn.close()

    def get_course(self, course_id: int) -> Course:
        """
        Retrieves a Course object, including all its Assessments populated from the DB.
        """
        conn = sqlite3.connect(self.conn_str)
        cur = conn.cursor()

        cur.execute(
            "SELECT Course_Name, Desired_Mark FROM Course WHERE Course_Id = ?", (course_id,))
        row = cur.fetchone()

        if not row:
            conn.close()
            return None

        course_name, desired_mark = row

        cur.execute("""
                    SELECT Assessment_Name, Assessments_Weight, Assessment_Mark
                    FROM Assessments
                    WHERE Course_Id = ?
                    """, (course_id,))

        assessment_rows = cur.fetchall()
        assessments_list = []
        for a_row in assessment_rows:
            # Unpack row: Name, Weight, Mark
            a_name, a_weight, a_mark = a_row
            assessments_list.append(Assessment(a_name, a_weight, a_mark))

        conn.close()

        return Course(desired_mark, course_name, assessments_list)

    def get_all_courses(self) -> list[tuple[int, Course]]:
        """
        Returns a list of tuples: (Course_Id, Course_Object)
        """
        conn = sqlite3.connect(self.conn_str)
        cur = conn.cursor()

        cur.execute("SELECT Course_Id FROM Course")
        rows = cur.fetchall()
        conn.close()

        results = []
        for row in rows:
            c_id = row[0]
            course_obj = self.get_course(c_id)
            results.append((c_id, course_obj))

        return results

    def delete_course(self, course_id: int) -> None:
        """
        Deletes a course and its associated assessments (via Cascade or manual deletion).
        """
        conn = sqlite3.connect(self.conn_str)
        cur = conn.cursor()

        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("DELETE FROM Course WHERE Course_Id = ?", (course_id,))
        conn.commit()
        conn.close()

    def add_assessment(self, course_id: int, assessment: Assessment) -> int:
        """
        Adds a new assessment to the database linked to a specific course and returns the new Assessment_Id.
        """
        conn = sqlite3.connect(self.conn_str)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Assessments (Assessment_Name, Assessments_Weight, Assessment_Mark, Course_Id)
            VALUES (?, ?, ?, ?)
            """, (assessment.get_name(), assessment.get_weight(), assessment.get_mark(), course_id))

        new_id = cur.lastrowid
        conn.commit()
        conn.close()
        return new_id

    def update_assessment(self, assessment_id: int, assessment: Assessment) -> None:
        """
        Updates an existing assessment's details.
        """
        conn = sqlite3.connect(self.conn_str)
        cur = conn.cursor()

        cur.execute("""
            UPDATE Assessments
            SET Assessment_Name    = ?,
                Assessments_Weight = ?,
                Assessment_Mark    = ?
            WHERE Assessment_Id = ?
            """, (assessment.get_name(), assessment.get_weight(), assessment.get_mark(), assessment_id))

        conn.commit()
        conn.close()

    def get_assessment(self, assessment_id: int) -> Assessment:
        """
        Retrieves a single Assessment object by its DB ID.
        """
        conn = sqlite3.connect(self.conn_str)
        cur = conn.cursor()

        cur.execute("""
            SELECT Assessment_Name, Assessments_Weight, Assessment_Mark
            FROM Assessments
            WHERE Assessment_Id = ?
            """, (assessment_id,))

        row = cur.fetchone()
        conn.close()

        if row:
            return Assessment(row[0], row[1], row[2])
        return None

    def delete_assessment(self, assessment_id: int) -> None:
        """
        Deletes a specific assessment
        """
        conn = sqlite3.connect(self.conn_str)
        cur = conn.cursor()
        cur.execute("DELETE FROM Assessments WHERE Assessment_Id = ?", (assessment_id,))
        conn.commit()
        conn.close()



