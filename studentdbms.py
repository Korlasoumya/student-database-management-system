class Student:
    def _init_(self, session, course, name, dob, gender, email, mobile, marks):
        self.session = session
        self.course = course
        self.name = name
        self.dob = dob
        self.gender = gender
        self.email = email
        self.mobile = mobile
        self.marks = marks  # Dictionary to store marks in different subjects

    def calculate_average(self):
        return sum(self.marks.values()) / len(self.marks) if self.marks else 0

    def display_info(self):
        print(f"Session: {self.session}")
        print(f"Course: {self.course}")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Gender: {self.gender}")
        print(f"Email: {self.email}")
        print(f"Mobile: {self.mobile}")
        print(f"Marks: {self.marks}")
        avg_marks = self.calculate_average()
        print(f"Average Marks: {avg_marks:.2f}")
        self.display_performance(avg_marks)
        print("-----------------------------------")

    def display_performance(self, avg_marks):
        if avg_marks >= 90:
            print("Performance: Excellent")
        elif avg_marks >= 75:
            print("Performance: Good")
        elif avg_marks >= 50:
            print("Performance: Average")
        else:
            print("Performance: Poor")


class StudentManagementSystem:
    def _init_(self):
        self.students = []

    def add_student(self):
        print("\n--- Add New Student ---")
        session = input("Enter Session: ")
        course = input("Enter Course: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Date of Birth (DD-MM-YYYY): ")
        gender = input("Enter Gender (M/F): ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile Number: ")

        # Taking marks input
        marks = {}
        subjects = input("Enter subjects separated by comma (e.g., Math,Science,English): ").split(',')
        for subject in subjects:
            mark = int(input(f"Enter marks for {subject.strip()}: "))
            marks[subject.strip()] = mark

        # Creating a new student object
        student = Student(session, course, name, dob, gender, email, mobile, marks)
        self.students.append(student)
        print("Student added successfully!\n")

    def view_students(self):
        print("\n--- List of Students ---")
        if not self.students:
            print("No students available.")
        else:
            for idx, student in enumerate(self.students, 1):
                print(f"Student {idx}:")
                student.display_info()

    def search_student(self):
        print("\n--- Search for a Student ---")
        search_name = input("Enter the student's name to search: ")
        found = False
        for student in self.students:
            if student.name.lower() == search_name.lower():
                student.display_info()
                found = True
                break
        if not found:
            print("No student found with that name.\n")

    def run(self):
        while True:
            print("\n=== Student Management System ===")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student by Name")
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                print("Exiting the system...")
                break
            else:
                print("Invalid choice, please try again.\n")


# Main program execution
if __name__ == "_main_":
    sms = StudentManagementSystem()
    sms.run()
