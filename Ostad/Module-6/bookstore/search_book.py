from view_books import view_books

def search_book(books):
    searched_keyword = input("Search by Title / Author / Genre: ").strip().lower()
    found_books = [book for book in books if searched_keyword in book['title'].lower() or searched_keyword in book['author'].lower() or searched_keyword in book['genre'].lower()]

    if not found_books:
        print("No book matched.")
    else:
        view_books(found_books)
