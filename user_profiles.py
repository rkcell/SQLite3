import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

def alter_table(cursor):
    column_name=input("Enter new column name ")
    column_type=input("Enter column type: ")

    cursor.execute(f'''
        ALTER TABLE user_profiles
        ADD COLUMN {column_name} {column_type}
    ''')

def records():
    username = input("Input username: ")
    email = input("Enter email: ")
    password = input("Enter password")
    profile_picture = 0
    date_of_birth = input("Input date of birth in format YYYY-MM-DD: ")
    signup_date = "2024-12-19"
    last_login_date="2024-12-19"
    bio = input("Provide your biography: ")
    phone_number= input("Enter your phone number: ")
    is_active=True
    account_balance=float(input("Enter your balance: "))
    education_level= input("Enter you education level: ")

    return [username, email, password, profile_picture, date_of_birth, signup_date, last_login_date, bio, phone_number, is_active, account_balance,  education_level ]


cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS user_profiles(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            profile_picture BLOB DEFAULT NULL,
            date_of_birth DATE,
            signup_date DATETIME,
            last_login_date DATETIME,
            bio TEXT,
            phone_number TEXT,
            is_active BOOLEAN DEFAULT 1,
            account_balance REAL,
            education_level TEXT
        )
    '''
)

# cursor.execute(
#     '''
#     INSERT INTO user_profiles(
#         username, email, password, profile_picture, date_of_birth, signup_date, last_login_date, bio, phone_number,
#         is_active, account_balance, education_level
#     )
#     VALUES(
#         ?,?,?,?,?,?,?,?,?,?,?,?
#         )
#
#     ''', records()
# )
alter_table(cursor)

print("Done!")
conn.commit()
conn.close()
