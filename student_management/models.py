from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict


class Major(Enum):
    COMPUTER_SCIENCE = "Computer Science"
    DATA_SCIENCE = "Data Science"
    SOFTWARE_ENGINEERING = "Software Engineering"


@dataclass
class Student:
    """Represents a student entity with automated ID validation."""
    student_id: int
    name: str
    major: Major
    grades: List[float] = field(default_factory=list)

    def __post_init__(self):
        if self.student_id <= 0:
            raise ValueError("Student ID must be a positive integer.")
        if not self.name.strip():
            raise ValueError("Student name cannot be empty.")

    @property
    def gpa(self) -> float:
        """Calculates and returns the Grade Point Average (GPA)."""
        if not self.grades:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 2)