import csv
import os
FILE_NAME = "students.csv"
def show_menu():
    print("\n===== Student Record Management =====")
    print("1. View Records")
    print("2. Add Record")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")

def view_records():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def add_record():
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course Enrolled: ")

        writer.writerow([student_id, name, age, course])

        print("Record added successfully!")

def search_record():
    search_id = input("Enter Student ID to search: ")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        found = False
        for row in reader:
            if row[0] == search_id:
                print("ID:", row[0])
                print("Name:", row[1])
                print("Age:", row[2])
                print("Course:", row[3])
                found = True
                break
        if not found:
                print("Student not found.")

def update_record():
    update_id = input("Enter Student ID to update: ")
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            rows.append(row)

    found = False

    
    for row in rows[1:]:
        if row[0] == update_id:
            print("Current Record:", row)

            row[1] = input("Enter New Name: ")
            row[2] = input("Enter New Age: ")
            row[3] = input("Enter New Course: ")

            found = True
            break

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Record updated successfully!")
    else:
        print("Student not found.")

def delete_record():
    delete_id = input("Enter Student ID to delete: ")

    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == delete_id:
                found = True
                continue      # Skip this row (delete it)

            rows.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Record deleted successfully!")
    else:
        print("Student not found.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice =='1':
            view_records()
        elif choice =='2':
            add_record()
        elif choice =='3':
            search_record()
        elif choice =='4':
            update_record()
        elif choice =='5':
            delete_record()
        elif choice =='6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()