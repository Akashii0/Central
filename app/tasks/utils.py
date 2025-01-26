from enum import Enum


# Enum for Task Status
class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


# Enum for Task Type
class TaskType(str, Enum):
    todo = "To-Do"
    dont_do = "Don't-Do"
