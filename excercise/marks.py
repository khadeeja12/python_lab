# Function to get student details and store them in a dictionary
def get_student_details(N):
    students = {}
    for _ in range(N):
        name = input("Enter student's name: ")
        roll_no = input("Enter student's roll number: ")
        total_mark = int(input("Enter student's total mark: "))
        students[roll_no] = {'name': name, 'total_mark': total_mark}
    return students

# Function to find and print the details of the student with the highest total mark
def print_top_student(students):
    if not students:
        print("No students available.")
        return
    
    top_student_roll_no = max(students, key=lambda roll_no: students[roll_no]['total_mark'])
    top_student = students[top_student_roll_no]
    
    print(f"\nDetails of the student with the highest total mark:")
    print(f"Name: {top_student['name']}")
    print(f"Roll Number: {top_student_roll_no}")
    print(f"Total Marks: {top_student['total_mark']}")

# Number of students
N = int(input("Enter the number of students: "))

# Get student details
students = get_student_details(N)

# Print details of the top student
print_top_student(students)
