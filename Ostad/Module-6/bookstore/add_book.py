from book_data import  save_books

def is_valid_book(new_book, all_books):
    for b in all_books:
        if b['isbn'] == new_book['isbn']:
            return False

    return True

def add_book(new_book):
    try:
        title = input("Enter Title: ").strip()
        author = input("Enter Author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        genre = input("Enter Genre: ").strip()
        price = float(input("Enter Price: ").strip())
        quantity = int(input("Enter Quantity: ").strip())
        if price <= 0:
            raise ValueError("Enter Must Positive Value")
        if quantity < 0:
            raise ValueError("Enter Must Positive Value")

        all_books = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "genre": genre,
            "price": price,
            "quantity": quantity
        }

        if is_valid_book(new_book, all_books):
            all_books.append(new_book)
            save_books(all_books)
            print(f"🔥Book added sucessfully with ISBN: {isbn}")
        else:
            print("Error: A book with this ISBN already exists.")

    except ValueError as ve:
        print('Input Error', ve)
