from book_data import load_books, save_books
from add_book import add_book
from view_books import view_books
from remove_book import remove_book
from search_book import search_book

def main():
    books = load_books()

    while True:
        print("\n--- Book Store Menu ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_book(books)
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            search_book(books)
        elif choice == '4':
            remove_book(books)
        elif choice == '5':
            save_books(books)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
