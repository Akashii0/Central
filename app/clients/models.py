from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.core.database import DBBase


class Client(DBBase):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)
    company = Column(String, nullable=True)
    address = Column(String, nullable=True)
    profile_picture = Column(String, default='./fallback.png', nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.now)

    projects = relationship("Project", back_populates="client")

    def __repr__(self):
        return f"<Client(name={self.name}, email={self.email}, company={self.company})>"
