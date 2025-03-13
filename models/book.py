from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=True)

    # Foreign Key to link each Book to a Library
    library_id = Column(Integer, ForeignKey('libraries.id'), nullable=False)

    # to access the library from a book
    library = relationship("Library", backref="books")

    member_id = Column(Integer, ForeignKey("members.id"), nullable=True)  # Nullable because a book can be available
   
    member = relationship("Member", backref="borrowed_books") #every member should have a list of borrowed books 

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, author={self.author}, genre={self.genre}, library_id={self.library_id})>"
