def view_books(books):
    if not books:
        print("No book available")
        return

    print("{:<15} {:<20} {:<10} {:<10} {:<8} {:<8}".format("ISBN", "Title", "Author", "Genre", "Price", "Qty"))
    print('-' * 80)

    for book in books:
        print("{:<15} {:<20} {:<10} {:<10} {:<8} {:<8}".format(book["isbn"], book["title"], book["author"], book["genre"], book["price"], book["quantity"]))
