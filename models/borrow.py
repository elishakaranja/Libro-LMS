#from main import session
from models.book import Book
from models.library import Library
from models.member import Member
from main import engine 

def borrow_book(member_name,library_name,book_title,session):
        #find the member 
        member = session.query(Member).filter_by(name = member_name).first()
        if not member:
            print(f"Error '{member_name}' is not a member. Try another name or sign up")
            return
        
        #find library 
        library = session.query(Library).filter_by(name = library_name).first()
        if not library:
            print(f"Error: '{library_name}' does not exist")
            return

        #find book in specified library
        book = session.query(Book).filter_by(title = book_title, library_id =library.id).first()

        if not book:
            print(f" Error: '{book_title}' not found in '{library_name}' ")
            return
         #checking if book has been borrowed 
        if book.member_id:
             print(f"Sorry ,the book '{book_title}' has already been borrowed by somoene else") 
             return 

        
        #borrowing a book 
        
        book.member_id = member.id
        #save change to db 
        session.commit()
        print(f"'{book_title}' has been successfully borrowed. it is with {member_name}.")       
        return


        

def return_book(member_name,book_title,session):
        #find the member and book ,no need for library 
        #check if the book's member_id = member.id if yes ,set member_id to none
        #else show an error 
        
     
        member = session.query(Member).filter_by(name = member_name).first()
        if not member:
            print(f"Error: '{member_name}' is not a member")
            return
        book = session.query(Book).filter_by(title = book_title,member_id = member.id).first()
        if not book:
            print(f"Error: The book '{book_title}' cannot be found or is not borrowed by '{member_name}'")
            return
        
        #returning the book if found
        book.member_id = None
        print(f"Error: the book '{book_title}' has been returned by '{member_name}' ")
        session.commit()


        
            