class Student:
    def __init__(self, roll_no, name, age, branch):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.branch = branch

    def __str__(self):
        return(f"Roll No: {self.roll_no}, "
               f"Name: {self.name}, "
               f"Age: {self.age}, "
               f"Branch: {self.branch}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if self.search_students(student.roll_no):
            print("Student with this Roll Number already exists!")
            return
        self.students.append(student)
        print("Student added succesfully!")

    def display_students(self):
        if not self.students:
            print("No Students Found!")
            return
        print("\n Student Records: ")
        for student in self.students:
            print(student)

    def search_students(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                return student
            
        return None
    
    def update_student(self, roll_no):
        student = self.search_students(roll_no)

        if student:
            print("\nEnter new details: ")
            student.name = input("New Name: ")
            student.age = int(input("Enter new Age: "))
            student.branch = input("New Branch: ")

            print("Student updated succesfully!")

        else:
            print("Student not found!")

    def delete_student(self, roll_no):
        student = self.search_students(roll_no)
        if student:
            self.students.remove(roll_no)
            print("Student deleted succesfully!")

        else:
            print("Student not found!")

manager = StudentManager()

while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        branch = input("Enter Branch: ")

        student = Student(roll_no, name, age, branch)
        manager.add_student(student)

    elif choice == "2":
        manager.display_students()

    elif choice == "3":
        roll_no = int(input("Enter Roll Number to Search: "))
        manager.search_students(roll_no)

        if student:
            print("\nStudent Found: ")
            print(student)
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll_no = int(input("Enter Roll Number to Update: "))
        manager.update_student(roll_no)

    elif choice == "5":
        roll_no = int(input("Enter Roll Number to Delete: "))
        manager.delete_student(roll_no)

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
