class Student:
    def __init__(self, name, dob, email, phone):
        self.name = name
        self.dob = dob
        self.email = email
        self.phone = phone

    def introduce(self):
        print("name is: ", self.name)
        print("dob is: ", self.dob)
        print("email is: ", self.email)
        print("phone is: ", self.phone)


class StudentManager:
    def __init__(self, student_list):
        self.student_list = student_list

    def add_student(self, student):
        self.student_list.append(student)

    def show_all_student(self):
        for student in self.student_list:
            student.introduce()
            print("----------")


student_manager = StudentManager([])
while True:
    print("1. Add student")
    print("2. Show all student")
    print("3. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        dob = input("Enter dob: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        student = Student(name, dob, email, phone)
        student_manager.add_student(student)
    elif choice == 2:
        student_manager.show_all_student()
    elif choice == 3:
        break
    else:
        print("Invalid choice")
