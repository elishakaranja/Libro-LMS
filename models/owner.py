from sqlalchemy import Column, Integer, String
from models.base import Base

class LibraryOwner(Base):
    __tablename__ = 'library_owners'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)  # Owners must have unique names but its only one owner

    def __repr__(self):
        return f"<LibraryOwner(id={self.id}, name={self.name})>"
