class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(self.grades.values())
        count = len(self.grades)
        return total / count

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                average = student.get_average_grade()
                print(f"Average grade for {student.name}: {average}")
                return
        print("Student not found.")

    def get_class_average_for_subject(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            print(f"No grades found for subject {subject}.")
        else:
            average = total / count
            print(f"Class average for {subject}: {average}")

# Demonstration of functionalities
def main():
    # Create a classroom instance
    classroom = Classroom()

    # Add students
    student1 = Student("Alice")
    student1.add_grade("Math", 90)
    student1.add_grade("Science", 85)

    student2 = Student("Bob")
    student2.add_grade("Math", 80)
    student2.add_grade("Science", 88)

    classroom.add_student(student1)
    classroom.add_student(student2)

    # Display all students
    print("Displaying all students:")
    classroom.display_students()

    # Get average grade of a student
    print("\nGetting average grade for Alice:")
    classroom.get_student_average("Alice")

    # Get class average for a subject
    print("\nGetting class average for Math:")
    classroom.get_class_average_for_subject("Math")

if __name__ == "__main__":
    main()
