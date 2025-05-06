def is_valid_book(book, books):
    for b in books:
        if b['isbn'] == book['isbn']:
            return False

    return True

def add_book(books):
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

        book = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "genre": genre,
            "price": price,
            "quantity": quantity
        }

        if is_valid_book(book, books):
            books.append(book)
        else:
            print("Error: A book with this ISBN already exists.")

    except ValueError as ve:
        print('Input Error', ve)
