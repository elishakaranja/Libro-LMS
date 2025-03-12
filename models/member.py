from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    library_id = Column(Integer, ForeignKey("libraries.id"))#link to library 
    library = relationship("Library", backref="members")



    def __repr__(self):
        return f"<Member(name='{self.name}', library='{self.library.name}')>"
