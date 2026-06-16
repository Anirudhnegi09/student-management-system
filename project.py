#student management system
#   create a student management syystem using python and object oriented programming(oop)

# the system should allow the user to:
# add a new student .
# view all student 
# search for student using student id
# update a students marks
# delete a student record 
# display the student with highest marks 
# exit the application.
# each student should have:
# student id 
# student Name 
# age 
# marks




class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print("-" * 30)


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    
    def add_student(self):
        student_id = input("Enter Student ID: ")

        
        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        student = Student(student_id, name, age, marks)
        self.students.append(student)

        print("Student added successfully!")

    
    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n--- Student Records ---")
        for student in self.students:
            student.display()

    
    def search_student(self):
        student_id = input("Enter Student ID to search: ")

        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent Found:")
                student.display()
                return

        print("Student not found.")
 
    
    def update_marks(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student.student_id == student_id:
                new_marks = float(input("Enter New Marks: "))
                student.marks = new_marks
                print("Marks updated successfully!")
                return

        print("Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student record deleted successfully!")
                return

        print("Student not found.")

    
    def highest_marks_student(self):
        if not self.students:
            print("No student records available.")
            return

        top_student = max(self.students, key=lambda student: student.marks)

        print("\n--- Student with Highest Marks ---")
        top_student.display()



def main():
    sms = StudentManagementSystem()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Marks")
        print("5. Delete Student Record")
        print("6. Display Student with Highest Marks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sms.add_student()
        elif choice == "2":
            sms.view_students()
        elif choice == "3":
            sms.search_student()
        elif choice == "4":
            sms.update_marks()
        elif choice == "5":
            sms.delete_student()
        elif choice == "6":
            sms.highest_marks_student()
        elif choice == "7":
            print("Exiting Student Management System...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
      