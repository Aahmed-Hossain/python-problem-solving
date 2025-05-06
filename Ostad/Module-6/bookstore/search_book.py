from view_books import view_books

def search_book(books):
    keyword = input("Search by Title / Author / Genre: ").strip().lower()
    found_book = [book for book in books if keyword in book['title'].lower() or keyword in book['author'].lower() or keyword in book['genre'].lower()]

    if not found_book:
        print("No book matched.")
    else:
        view_books(found_book)
