import csv
import os
import pandas as pd
file_name = "students.csv"
def create_file():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Age", "Course", "Marks"])
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([sid, name, age, course, marks])

    print("Student added successfully!\n")
def view_students():
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            print("\n--- Student Records ---")
            for row in reader:
                print(row)
    except:
        print("No data found!\n")
def search_student():
    sid = input("Enter Student ID to search: ")
    found = False

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == sid:
                print("Student Found:", row)
                found = True

    if not found:
        print("Student not found!\n")
def update_marks():
    sid = input("Enter Student ID to update: ")
    rows = []
    updated = False

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == sid:
                new_marks = float(input("Enter new marks: "))
                row[4] = str(new_marks)
                updated = True
            rows.append(row)

    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    if updated:
        print("Marks updated successfully!\n")
    else:
        print("Student not found!\n")
def delete_student():
    sid = input("Enter Student ID to delete: ")
    rows = []
    deleted = False

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != sid:
                rows.append(row)
            else:
                deleted = True

    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    if deleted:
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")

def marks_summary():
    total = 0
    count = 0

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            total += float(row[4])
            count += 1

    if count > 0:
        avg = total / count
        print("Total Marks:", total)
        print("Average Marks:", avg)
    else:
        print("No data available!\n")

def pandas_report():
    try:
        df = pd.read_csv(file_name)

        print("\n--- Full Data ---")
        print(df)

        print("\nAverage Marks:", df["Marks"].mean())

        print("\nCourse-wise Marks:")
        print(df.groupby("Course")["Marks"].mean())

    except:
        print("No data for analysis!\n")

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Marks Summary")
        print("7. Pandas Report")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            marks_summary()
        elif choice == "7":
            pandas_report()
        elif choice == "8":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

create_file()
menu()
