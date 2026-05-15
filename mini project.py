import mysql.connector
dbpassword=input("Enter MySQL Password: ")

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=dbpassword,
    database="student_management"
)

cursor = conn.cursor()

# Add Student

def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    marks = int(input("Enter Marks: "))

    query = "INSERT INTO students VALUES (%s, %s, %s, %s)"
    values = (student_id, name, department, marks)

    cursor.execute(query, values)
    conn.commit()

    print("Student Added Successfully")

# View Students

def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\nStudent Records")
    print("---------------------------")

    for row in records:
        print(row)

# Search Student

def search_student():
    student_id = int(input("Enter Student ID to Search: "))

    query = "SELECT * FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))

    record = cursor.fetchone()

    if record:
        print(record)
    else:
        print("Student Not Found")

# Update Marks

def update_marks():
    student_id = int(input("Enter Student ID: "))
    new_marks = int(input("Enter New Marks: "))

    query = "UPDATE students SET marks = %s WHERE student_id = %s"
    values = (new_marks, student_id)

    cursor.execute(query, values)
    conn.commit()

    print("Marks Updated Successfully")

# Delete Student

def delete_student():
    student_id = int(input("Enter Student ID to Delete: "))

    query = "DELETE FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))
    conn.commit()

    print("Student Deleted Successfully")

# Main Menu

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        view_students()

    elif choice == '3':
        search_student()

    elif choice == '4':
        update_marks()

    elif choice == '5':
        delete_student()

    elif choice == '6':
        print("Thank You")
        break

    else:
        print("Invalid Choice")