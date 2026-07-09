from models import Student, Major
from registry import StudentRegistry

def main():
    print("--- Initializing Student Registry ---")
    registry = StudentRegistry()

    # Create mockup student data
    student1 = Student(student_id=101, name="Alice Vance", major=Major.COMPUTER_SCIENCE)
    student2 = Student(student_id=102, name="Bob Miller", major=Major.DATA_SCIENCE)

    student1.grades = [4.0, 3.7, 3.9]
    student2.grades = [3.2, 3.5, 3.0]

    # Register records
    registry.register_student(student1)
    registry.register_student(student2)

    # Fetch and display records
    print(f"Loaded Student: {registry.get_student(101).name} | GPA: {registry.get_student(101).gpa}")
    
    # Query top performers
    print("\n--- Querying Top Performers (GPA >= 3.5) ---")
    for student in registry.get_top_performers():
        print(f"- {student.name} ({student.major.value})")


if __name__ == "__main__":
    main()
