import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#import fire
from sqlalchemy.orm import sessionmaker
#from sqlalchemy import create_engine
from models.base import Base
from models.borrow import borrow_book, return_book
from models.owner import LibraryOwner
from models.library import Library
from models.member import Member
from models.book import Book
from main import engine  # Importing the engine from main.py for the database connection
from models.ai import get_book_recommendations
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



Session = sessionmaker(bind=engine)
session = Session()

def create_library(owner_name, library_name,location):
    """Creates a new library and assigns an owner."""
    session = Session()
    
    owner = session.query(LibraryOwner).filter_by(name=owner_name).first()
    if not owner:
        owner = LibraryOwner(name=owner_name)
        session.add(owner)
        session.commit()
    
    library = Library(name=library_name, location = location,owner_id=owner.id)
    session.add(library)
    session.commit()
    print(f"Library '{library_name}' , '{location}' created with owner '{owner_name}'.")
    session.close()



def view_libraries(show_pause = True): # show pause to display input pause ,False wont display
    """Displays all available libraries."""
    session = Session()
    libraries = session.query(Library).all()

    if not libraries:
        print("No libraries found.")
    else:
        print("\nAvailable Libraries:")
        for lib in libraries:
            print(f"--- {lib.name} , ({lib.location})")
    #preventing refresh once main_menu() runs by adding a pause
    if show_pause:
        input("\nPress Enter to return to the main menu...")
    session.close()

    



def join_library(member_name, library_name=None):
    """Allows a member to join a library."""
    session = Session()

    if not library_name:
        
        library_name = input("Enter the library name you want to join: ")

    library = session.query(Library).filter_by(name=library_name).first()
    if not library:
        print(f"Library '{library_name}' does not exist.")
        session.close()
        return
    

    member = Member(name=member_name, library_id=library.id)
    session.add(member)
    session.commit()
    print(f"Member '{member_name}' joined library '{library_name}'.")
    session.close()


def add_book(library_name,owner_name, book_title, author_name):
    """Adds a book to a specific library."""
    session = Session()

    library = session.query(Library).filter_by(name=library_name).first()
    if not library:
        print(f"Library '{library_name}' does not exist.")
        session.close()
        return
    # Verify ownership
    owner = session.query(LibraryOwner).filter_by(id=library.owner_id, name=owner_name).first()
    if not owner:
        print(f"Only the owner of '{library_name}' can add books.")
        session.close()
        return

    book = Book(title=book_title, author=author_name, library_id=library.id)
    session.add(book)
    session.commit()
    print(f"Book '{book_title}' by '{author_name}' added to library '{library_name}'.")
    session.close()




def borrow(member_name, library_name, book_title):
    result = borrow_book(member_name,library_name, book_title, session)
    return result

def return_a_book(member_name,book_title):
    result = return_book(member_name,book_title,session)

    return result

#search functionalty 
def search_books(library_name, search_query):
    """Search for books by title or author in a specific library."""
    session = Session()

    # Find the library
    library = session.query(Library).filter_by(name=library_name).first()
    if not library:
        print(f"Library '{library_name}' does not exist.")
        session.close()
        return

    # Search for books by title or author
    books = session.query(Book).filter(
        Book.library_id == library.id,
        (Book.title.ilike(f"%{search_query}%") | Book.author.ilike(f"%{search_query}%"))
    ).all()

    # Display results
    if books:
        print("\nSearch Results:")
        for book in books:
            print(f"- {book.title} by {book.author}")
    else:
        print("No matching books found.")

    session.close()

def recommend_books():
    book_title = input("Enter a book title: ")
    recommendations = get_book_recommendations(book_title)

    print("\nRecommended Books:")
    for book in recommendations:
        print(f"- {book}")






def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("1. Create a library")
        print("2. Join a library")
        print("3. View all libraries") 
        print("4. Add a book")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Search books")
        print("8. Get Book recommendation")
        print("9. Exit")
        ##//////////////////////////////////////////
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            owner = input("Enter owner name: ")
            library = input("Enter library name: ")
            location = input("Enter library location: ")
            create_library(owner, library, location)
        elif choice == "2":
            
            member = input("Enter your name: ")
            view_libraries(False)
            input("Press Entre to entre library name")
            
            
            library = input("Enter library name: ")
            join_library(member, library)


        elif choice == "3":
            view_libraries()


        elif choice == "4":
            library = input("Enter library name: ")
            owner = input("Enter owner name")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            add_book(library,owner, title, author)
        elif choice == "5":
            member = input("Enter your name: ")
            library = input("Enter library name: ")
            book = input("Enter book title: ")

            # if book =="1": #for handling books
            #     pass

            borrow(member, library, book)


        elif choice == "6":
            member = input("Enter your name: ")
            book = input("Enter book title: ")
            return_a_book(member, book)
        elif choice == "7":
            library_name = input("Enter library name: ")
            search_query = input("Enter book title or author to search: ")
            search_books(library_name, search_query)

        elif choice == "8":
            recommend_books()

        elif choice == "9":
            print("Exiting Libro. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")




if __name__ == "__main__":
    #fire.Fire({"borrow":borrow,"return_book":return_a_book, "create_library": create_library,"join_library": join_library,"add_book": add_book,})
    main_menu() 