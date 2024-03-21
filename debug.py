# debug.py

from models.author import Author
from models.book import Book
import ipdb

Author.create_table()
Book.create_table()
def reset_database():
   
    Book.drop_table()
    Author.drop_table()
    Book.create_table()
    Author.create_table()

    # Create seed data
    author1 = Author.create("F. Scott Fitzgerald", "fitzgerald@example.com")
    author2 = Author.create("Harper Lee", "harperlee@gmail.com")
    author3 = Author.create("George Orwell", "georgeorwell@gmail.com")
    author4 = Author.create("J.K. Rowling" , "rowling@gmail.com")
    author5 = Author.create("Jane Austen", "janeausten@egmail.com")
    author6 = Author.create("J.D. Salinger", "salinger@gmail.com")
    author7 = Author.create("J.R.R. Tolkien", "tolkien@gmail.com")
    author8 = Author.create("Dan Brown", "danbrown@gmail.com")
    author9 = Author.create("Douglas Adams", "douglasadams@gmail.com")
   

    Book.create("The Great Gatsby", author1.id)
    Book.create("To Kill a Mockingbird", author2.id)
    Book.create("1984", author3.id)
    Book.create("Harry Potter and the Philosopher's Stone", author4.id)
    Book.create("Pride and Prejudice", author5.id)
    Book.create("The Catcher in the Rye", author6.id)
    Book.create("The Lord of the Rings", author7.id)
    Book.create("The Hobbit", author7.id)
    Book.create("The Da Vinci Code", author8.id)
    Book.create("The Hitchhiker's Guide to the Galaxy", author9.id)

reset_database()
ipdb.set_trace()
