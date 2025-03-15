import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy.orm import sessionmaker
from main import engine
from models.book import Book
from models.library import Library
from models.member import Member
from models.owner import LibraryOwner

Session = sessionmaker(bind=engine)
my_session = Session()

owner1= LibraryOwner(name = "Dan")
my_session.add(owner1)
my_session.commit()


library1 = Library(name="Nairobi Library",location="Nairobi" ,owner_id = owner1.id )
my_session.add(library1)
my_session.commit() 


book1 = Book(title ="White Nights", author="Dostoyevsky",genre="Fiction",library_id = library1.id)#title aithor genre libid
my_session.add(book1)


member1 = Member(name= "Dolly", library_id= library1.id)#library_id,library
my_session.add(member1)

my_session.commit()

print("Test data successfully added!")


