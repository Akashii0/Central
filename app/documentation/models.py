from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import DBBase


class Document(DBBase):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_type = Column(String, nullable=True)
    upload_date = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    description = Column(Text, nullable=True)

    # Relationships
    project = relationship("Project", back_populates="documents")

    def __repr__(self):
        return f"<Document(file_name={self.file_name}, file_path={self.file_path})>"
