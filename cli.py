
from models.author import Author
from models.book import Book
from main import (
    exit_program,
    list_authors,
    find_author_by_name,
    find_author_by_id,
    create_author,
    update_author,
    delete_author,
    list_books,
    find_book_by_title,
    find_book_by_id,
    create_book,
    update_book,
    delete_book,
   
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_authors()
        elif choice == "2":
            find_author_by_name()
        elif choice == "3":
            find_author_by_id()
        elif choice == "4":
            create_author()
        elif choice == "5":
            update_author()
        elif choice == "6":
            delete_author()
        elif choice == "7":
            list_books()
        elif choice == "8":
            find_book_by_title()
        elif choice == "9":
            find_book_by_id()
        elif choice == "10":
            create_book()
        elif choice == "11":
            update_book()
        elif choice == "12":
            delete_book()
        else:
            print("Invalid choice")
          

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all authors")
    print("2. Find author by name")
    print("3. Find author by id")
    print("4: Create author")
    print("5: Update author")
    print("6: Delete author")
    print("7. List all books")
    print("8. Find book by title")
    print("9. Find book by id")
    print("10: Create book")
    print("11: Update book")
    print("12: Delete book")

if __name__ == "__main__":
   main()
