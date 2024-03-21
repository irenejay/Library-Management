
from models.author import Author
from models.book import Book

def exit_program():
    print("Goodbye!")
    exit()

def list_authors():
    authors = Author.get_all()
    for author in authors:
        print(author)

def find_author_by_name():
    name = input("Enter the author's name: ")
    author = Author.find_by_name(name)
    print(author) if author else print(f'Author {name} not found')

def find_author_by_id():
    id_ = input("Enter the author's id: ")
    author = Author.find_by_id(id_)
    print(author) if author else print(f'Author {id_} not found')
    


def create_author():
    name = input("Enter the author's name: ")
    try:
        author = Author.create(name)
        print(f'Success: {author}')
    except Exception as exc:
        print("Error creating author: ", exc)

def update_author():
    id_ = input("Enter the author's id: ")
    if author := Author.find_by_id(id_):
        try:
            name = input("Enter the author's new name: ")
            author.name = name
            author.update()
            print(f'Success: {author}')
        except Exception as exc:
            print("Error updating author: ", exc)
    else:
        print(f'Author {id_} not found')

def delete_author():
    id_ = input("Enter the author's id: ")
    if author := Author.find_by_id(id_):
        author.delete()
        print(f'Author {id_} deleted')
    else:
        print(f'Author {id_} not found')

# Now let's create similar functions for Book
def list_books():
    books = Book.get_all()
    for book in books:
        print(book)

def find_book_by_title():
    title = input("Enter the book's title: ")
    book = Book.find_by_title(title)
    print(book) if book else print(f'Book {title} not found')

def find_book_by_id():
    id_ = input("Enter the book's id: ")
    book = Book.find_by_id(id_)
    print(book) if book else print(f'Book {id_} not found')

def create_book():
    title = input("Enter the book's title: ")
    author_id = input("Enter the author's id: ")
    try:
        book = Book.create(title, author_id)
        print(f'Success: {book}')
    except Exception as exc:
        print("Error creating book: ", exc)

def update_book():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        try:
            title = input("Enter the book's new title: ")
            author_id = input("Enter the author's id: ")
            book.title = title
            book.author_id = author_id
            book.update()
            print(f'Success: {book}')
        except Exception as exc:
            print("Error updating book: ", exc)
    else:
        print(f'Book {id_} not found')

def delete_book():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'Book {id_} deleted')
    else:
        print(f'Book {id_} not found')
