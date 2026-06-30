
import csv

FILE_NAME = "students.csv"


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 75:
        return "B+"
    elif percentage >= 70:
        return "B"
    elif percentage >= 65:
        return "C+"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def view_all_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            print("\n===== STUDENT PERFORMANCE TRACKER =====")

            for row in reader:
                print(f"\nRoll No    : {row['Roll No']}")
                print(f"Name       : {row['Name']}")
                print(f"Percentage : {row['Percentage']}%")
                print(f"Grade      : {row['Grade']}")
                print("-" * 35)

    except FileNotFoundError:
        print("Error: students.csv file not found!")


def search_student():
    roll_no = input("Enter Roll Number: ").strip()

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            found = False

            for row in reader:
                if row["Roll No"].strip() == roll_no:

                    subjects = {
                        "Maths": int(row["Maths"]),
                        "Science": int(row["Science"]),
                        "English": int(row["English"]),
                        "Computer Science": int(row["Computer Science"])
                    }

                    strongest = max(subjects, key=subjects.get)
                    weakest = min(subjects, key=subjects.get)

                    print("\n===== PERFORMANCE REPORT =====")
                    print("Name       :", row["Name"])
                    print("Roll No    :", row["Roll No"])
                    print("Total      :", row["Total"])
                    print("Percentage :", row["Percentage"] + "%")
                    print("Grade      :", row["Grade"])
                    print("Strongest Subject :", strongest)
                    print("Weakest Subject   :", weakest)

                    found = True
                    break

            if not found:
                print("Student not found!")

    except FileNotFoundError:
        print("Error: students.csv file not found!")


def class_analysis():
    try:
        percentages = []

        with open(FILE_NAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                percentages.append(float(row["Percentage"]))

        if percentages:
            print("\n===== CLASS ANALYSIS =====")
            print("Total Students     :", len(percentages))
            print("Highest Percentage :", max(percentages))
            print("Lowest Percentage  :", min(percentages))
            print("Average Percentage :", round(sum(percentages) / len(percentages), 2))
        else:
            print("No student data available!")

    except FileNotFoundError:
        print("Error: students.csv file not found!")


def topper():
    try:
        highest = 0
        topper_name = ""

        with open(FILE_NAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                percentage = float(row["Percentage"])

                if percentage > highest:
                    highest = percentage
                    topper_name = row["Name"]

        print("\n===== CLASS TOPPER =====")
        print("Name       :", topper_name)
        print("Percentage :", highest)

    except FileNotFoundError:
        print("Error: students.csv file not found!")


def grade_distribution():
    try:
        grades = {
            "A+": 0,
            "A": 0,
            "B+": 0,
            "B": 0,
            "C+": 0,
            "C": 0,
            "D": 0,
            "F": 0
        }

        with open(FILE_NAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                percentage = float(row["Percentage"])
                grade = calculate_grade(percentage)
                grades[grade] += 1

        print("\n===== GRADE DISTRIBUTION =====")

        for grade, count in grades.items():
            print(f"{grade} : {count} Students")

    except FileNotFoundError:
        print("Error: students.csv file not found!")


def student_rank():
    roll_no = input("Enter Roll Number: ").strip()

    try:
        students = []

        with open(FILE_NAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

        students.sort(
            key=lambda x: float(x["Percentage"]),
            reverse=True
        )

        found = False

        for rank, student in enumerate(students, start=1):
            if student["Roll No"].strip() == roll_no:

                print("\n===== STUDENT RANK =====")
                print("Name       :", student["Name"])
                print("Roll No    :", student["Roll No"])
                print("Percentage :", student["Percentage"] + "%")
                print("Rank       :", rank)

                found = True
                break

        if not found:
            print("Student not found!")

    except FileNotFoundError:
        print("Error: students.csv file not found!")


def top_3_students():
    try:
        students = []

        with open(FILE_NAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

        students.sort(
            key=lambda x: float(x["Percentage"]),
            reverse=True
        )

        print("\n===== TOP 3 STUDENTS =====")

        for i, student in enumerate(students[:3], start=1):
            print(f"{i}. {student['Name']} - {student['Percentage']}%")

    except FileNotFoundError:
        print("Error: students.csv file not found!")


def pass_fail_analysis():
    try:
        passed = 0
        failed = 0

        with open(FILE_NAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                percentage = float(row["Percentage"])

                if percentage >= 50:
                    passed += 1
                else:
                    failed += 1

        print("\n===== PASS / FAIL ANALYSIS =====")
        print("Passed Students :", passed)
        print("Failed Students :", failed)

    except FileNotFoundError:
        print("Error: students.csv file not found!")


while True:

    print("\n========== MENU ==========")
    print("1. View All Students")
    print("2. Search Student")
    print("3. Class Analysis")
    print("4. View Topper")
    print("5. Grade Distribution")
    print("6. Student Rank")
    print("7. Top 3 Students")
    print("8. Pass/Fail Analysis")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        view_all_students()

    elif choice == "2":
        search_student()

    elif choice == "3":
        class_analysis()

    elif choice == "4":
        topper()

    elif choice == "5":
        grade_distribution()

    elif choice == "6":
        student_rank()

    elif choice == "7":
        top_3_students()

    elif choice == "8":
        pass_fail_analysis()

    elif choice == "9":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please try again.")
