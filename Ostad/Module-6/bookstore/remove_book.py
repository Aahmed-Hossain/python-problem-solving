def remove_book(books):
    isbn = input("Enter ISBN: ").strip()
    for book in books:
        if book['isbn'] == isbn:
            books.remove(book)
            print(f"The book with ISBN - {isbn} removed.")

        else:
            print(f"Book not found with the ISBN - {isbn}")
