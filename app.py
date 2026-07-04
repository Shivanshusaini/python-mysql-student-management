import mysql.connector
from mysql.connector import IntegrityError
from dotenv import load_dotenv

import os



class StudentRecord:


    

    def __init__(self):
        load_dotenv()

        self.conn = mysql.connector.connect(
            user='root',
            host='localhost',
            database='python_test_db',
            password=os.getenv("Db_password")
        )

        self.cursor = self.conn.cursor()

        print("Database Connected Successfully!")

    def create_table(self):

        table_query = """
        CREATE TABLE IF NOT EXISTS STUDENT(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(50) UNIQUE,
            AGE INT
        )
        """

        self.cursor.execute(table_query)
        print("Table Created Successfully!")

    def insert_data(self, name, age):

        query = """
        INSERT INTO STUDENT(NAME, AGE)
        VALUES(%s, %s)
        """

        try:

            self.cursor.execute(query, (name, age))
            self.conn.commit()

            print("Student Inserted Successfully!")

        except IntegrityError:

            self.conn.rollback()

            print("Student Already Exists!")

    def fetch_data(self):

        query = """
        SELECT * FROM STUDENT
        ORDER BY ID
        """

        self.cursor.execute(query)

        data = self.cursor.fetchall()

        if not data:
            print("No Records Found!")
            return

        print("\nStudent Records:")

        for row in data:
            print(row)

    def update_data(self, student_id, name, age):

        query = """
        UPDATE STUDENT
        SET NAME = %s, AGE = %s
        WHERE ID = %s
        """

        try:

            self.cursor.execute(query, (name, age, student_id))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("Student Updated Successfully!")
            else:
                print("Student ID Not Found!")

        except Exception as e:

            self.conn.rollback()

            print("Update Failed:", e)

    def delete_data(self, student_id):

        query = """
        DELETE FROM STUDENT
        WHERE ID = %s
        """

        try:

            self.cursor.execute(query, (student_id,))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("Student Deleted Successfully!")
            else:
                print("Student ID Not Found!")

        except Exception as e:

            self.conn.rollback()

            print("Delete Failed:", e)

    def close_connection(self):

        self.cursor.close()
        self.conn.close()

        print("Connection Closed Successfully!")


# ---------------- MAIN PROGRAM ---------------- #

def main():

    obj = StudentRecord()
    obj.create_table()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            name = input("Enter Name: ")

            try:
                age = int(input("Enter Age: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            obj.insert_data(name, age)

        elif choice == "2":

            obj.fetch_data()

        elif choice == "3":

            try:
                student_id = int(input("Enter Student ID: "))
                name = input("Enter New Name: ")
                age = int(input("Enter New Age: "))

            except ValueError:
                print("Please enter valid numbers!")
                continue

            obj.update_data(student_id, name, age)

        elif choice == "4":

            try:
                student_id = int(input("Enter Student ID: "))
            except ValueError:
                print("Please enter a valid ID!")
                continue

            obj.delete_data(student_id)

        elif choice == "5":

            obj.close_connection()
            print("Thank You!")
            break

        else:

            print("Invalid Choice!")


if __name__ == "__main__":
    main()