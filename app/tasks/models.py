from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from app.core.database import DBBase
from app.tasks.utils import TaskStatus, TaskType


class Task(DBBase):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    description = Column(String, nullable=False)
    type = Column(Enum(TaskType), default=TaskType.todo)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending)
    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.now)

    project = relationship("Project", back_populates="tasks")
