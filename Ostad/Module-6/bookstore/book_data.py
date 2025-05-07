import json
import os

FILE_NAME ='./books/book.json'

def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_books(books):
    with open(FILE_NAME, 'w') as f:
        return json.dump(books, f, indent=4)
