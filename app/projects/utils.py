from enum import Enum


# Enum for Project Status
class ProjectStatus(str, Enum):
    ongoing = "ongoing"
    completed = "completed"
    paused = "paused"
