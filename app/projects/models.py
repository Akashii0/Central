from datetime import datetime
from sqlalchemy import Column, Enum, Integer, String, DateTime, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import DBBase
from app.projects.utils import ProjectStatus


class Project(DBBase):
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.ongoing)
    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.now)

    # Relationships
    client = relationship("Client", back_populates="projects")
    documents = relationship("Document", back_populates="project")
    tasks = relationship("Task", back_populates="project")
