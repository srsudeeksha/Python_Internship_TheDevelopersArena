# Student Scores Program - Week 2 Task

# Function to calculate average score
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

# Dictionary to store student data
students = {}

# Number of students to enter
num_students = int(input("Enter the number of students: "))

for _ in range(num_students):
    name = input("Enter student name: ")

    # Validate score so it doesn't exceed 100
    while True:
        try:
            score = float(input(f"Enter score for {name}: "))
            if score <= 100:
                students[name] = score
                break
            else:
                print("❌ Invalid score! Maximum score is 100.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid score.")

# Display all students and scores
print("\n--- Student Scores ---")
for name, score in students.items():
    print(f"{name}: {score}")

# Calculate and display average
average_score = calculate_average(list(students.values()))
print(f"\nAverage Score: {average_score:.2f}")