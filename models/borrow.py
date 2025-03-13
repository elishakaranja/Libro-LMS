from models.book import Book
from models.library import Library
from models.member import Member

def borrow_book(self,member_name,library_name,book_title,session):
        #find the member 
        member = session.query(Member).filter_by(name = member_name)
        if not member:
            print(f"Error '{member_name}' is not a member. Try another name or sign up")
            return
        
        #find library 
        library = session.query(Library).filter_by(name = library_name).first()
        if not library:
            print(f"Error: '{library_name}' does not exist")
            return

        #find book in specified library
        book = session.query(Book).filter_by(title = book_title, library_id =library.id_).first()

        if not book:
            print(f" Error: '{book_title}' not found in '{library_name}' ")
            return

        if book.member_id:#if book has been borrowed 
             print(f"Sorry ,the book '{book_title}' has already been borrowed by somoene else") 
              
        session.commit()

def return_book(self,member_name,library_name,book_title,session):
        #find the member and library
        #check if the book is member_id = member.id if yes ,set member_id to none 
        member = session.query(Member).filter_by(name = member_name).first()
        if not member:
            print("Error: '{member_name}' is not a member")
        library = session.query(Library).filter_by(library_name = library.name).first()