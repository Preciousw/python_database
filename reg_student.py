from main import Student

try:
    student_name = input("Enter your name \n")
    student_id = input("Enter your student ID \n")
    student_class = input("Enter your class \n")

    Student.create( student_name = student_name,student_id  = student_id, student_class = student_class)
    print("Student profile created succcessfully")

except :
    print("Registration failed. Use a different ID")
