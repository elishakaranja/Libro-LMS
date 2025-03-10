from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Library(Base):
    __tablename__ = 'libraries'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False) 

    owner_id = Column(Integer, ForeignKey('library_owners.id'), nullable=False)  # Foreign Key linking owner to library 

    # Relationship - allows us to access owner from Library object
    owner = relationship("LibraryOwner", backref="libraries")#Everytime a new Library is created for a LibraryOwner the specific library is added to that owners "libraries "list 

    def __repr__(self):
        return f"<Library(id={self.id}, name={self.name}, location={self.location}, owner_id={self.owner_id})>"
