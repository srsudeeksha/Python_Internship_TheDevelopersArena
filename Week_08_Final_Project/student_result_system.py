# week8_student_result_system.py

def get_student_data():
    students = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        marks = float(input(f"Enter marks for {name}: "))
        grade = calculate_grade(marks)
        students[name] = {"Marks": marks, "Grade": grade}
    return students

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

def display_results(students):
    print("\n📊 Student Results:")
    for name, data in students.items():
        print(f"{name} → Marks: {data['Marks']}, Grade: {data['Grade']}")

def main():
    students = get_student_data()
    display_results(students)

if __name__ == "__main__":
    main()
