from typing import Dict, Optional
from models import Student, Major


class StudentRegistry:
    """
    A Singleton registry to manage student records.
    Demonstrates thread-safe-like design using single-instance management.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StudentRegistry, cls).__new__(cls)
            cls._instance._records = {}
        return cls._instance

    def register_student(self, student: Student) -> None:
        """Adds a student to the registry. Prevents duplicate IDs."""
        if student.student_id in self._records:
            raise KeyError(f"Student with ID {student.student_id} already exists.")
        self._records[student.student_id] = student

    def get_student(self, student_id: int) -> Optional[Student]:
        """Retrieves a student by their unique ID."""
        return self._records.get(student_id)

    def get_top_performers(self, threshold: float = 3.5) -> list[Student]:
        """Filters and returns students with a GPA above the threshold."""
        return [s for s in self._records.values() if s.gpa >= threshold]