'''
1. SQLite3-ის ბაზის შექმნა და ცხრილის დამატება
id: INTEGER PRIMARY KEY
first_name TEXT,
last_name TEXT,
age INTEGER,
grade TEXT
2. მონაცემების ჩაწერა ცხრილში  დაამატეთ 10 ჩანაწერი ცხრილში
3. მონაცემების წაკითხვა ცხრილიდან  წაიკითხეთ ყველა მონაცემი ცხრილიდან
 წაიკითხეთ მონაცემები სორტირებულად age-ის მიხედვით
 წაიკითხეთ მხოლოდ ის მონაცემები, რომლის grade არის A ან B
4. დაწერეთ სკრიპტი, რომელიც განაახლებს რომელიმე მონაცემს ცხრილში
5. წაშალეთ რომელიმე მონაცემი
6. დაამატეთ ცხრილს email სვეტი
'''

#ANSWER 1: ბაზის შექმნა და ცხრილის დამატება
import sqlite3

conn = sqlite3.connect("task.db")
cursor = conn.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    '''
)
conn.commit()
print("Task 1 Competed - created task.db and students table in it")

#ANSWER 2. მონაცემების ჩაწერა ცხრილში  დაამატეთ 10 ჩანაწერი ცხრილში

ten_records =[
        ["Tornike", "Skhirtladze", 40, "B"],
        ["Maiko", "Mekokishvili", 21, "A"],
        ["Mariam", "Agiashvili", 30, "C"],
        ["Inga", "Antidze", 32, "C"],
        ["Roini", "Bezhanidze", 35, "A"],
        ["David", "Mchedlishvili", 42, "A"],
        ["Mariami", "Papava", 31, "A"],
        ["Tamar", "Khutsishvili", 29, "A"],
        ["Nino", "Gelkhviidze", 24, "C"],
        ["Mate", "Gvetadze", 28, "B"]
   ]

cursor.executemany(
    '''
        INSERT INTO students(
            first_name, last_name, age, grade
        )
        VALUES(?,?,?,?)
    ''', ten_records
)
conn.commit()
print("Task 2 Competed - added 10 records into students table")

#ANSWER 3.1 წაიკითხეთ ყველა მონაცემი ცხრილიდან

cursor.execute("SELECT * FROM students")
records = cursor.fetchall()

print("All records: \n", records, "\n")

#ANSWER 3.2 წაიკითხეთ მონაცემები სორტირებულად age-ის მიხედვით

cursor.execute("SELECT * FROM students ORDER BY age DESC")
records_by_age = cursor.fetchall()
print("Records sorted by age descending: \n",records_by_age, "\n")

#ANSWER 3.3 წაიკითხეთ მხოლოდ ის მონაცემები, რომლის grade არის A ან B
cursor.execute("SELECT * FROM students WHERE grade = 'A' OR grade = 'B'")
records_ab = cursor.fetchall()
print("Records for only A nad B graded students: \n", records_ab,"\n")

#ANSWER 4. დაწერეთ სკრიპტი, რომელიც განაახლებს რომელიმე მონაცემს ცხრილში
def update_by_id(cursor):
    id=int(input("Please enter the id of the record to change: "))
    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    record_id=cursor.fetchone()
    if record_id:
        print(f"This record found for id {id}: {record_id}")
        new_grade=input(f"Please insert new grade (A/B/C) for student {record_id[1]} {record_id[2]}:")
        cursor.execute(
            "UPDATE students SET grade = ? WHERE id = ?",
            (new_grade, id)
        )
        conn.commit()
        print("Grade Updated!")
    else:
        print(f"No record found for id {id}, please restart the script")

#ANSWER 5. წაშალეთ რომელიმე მონაცემი
def delete_by_id(cursor):
    id = int(input("Please enter the id of the record to delete: "))
    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    record_id = cursor.fetchone()
    if record_id:
        print(f"This record found for id {id}: {record_id}")
        confirm = input(f"Please confirm the student {record_id[1]} {record_id[2]} to be deleted from db y/n ?: ")
        if confirm.lower() == "y":
            cursor.execute(
                "DELETE FROM students WHERE id = ?",  (id,)
            )
            conn.commit()
            print("Record Deleted!")
    else:
        print(f"No record found for id {id}, please restart the script")



update_by_id(cursor)
delete_by_id(cursor)

#ANSWER 6. დაამატეთ ცხრილს email სვეტი
cursor.execute("ALTER TABLE students ADD COLUMN email TEXT")
conn.commit()
print("Column 'email' added to the students table.")


conn.close()