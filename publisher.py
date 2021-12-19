from application import *

while True:
    print("""
1. Add book
""")
    action = input()
    if action != "1":
        print('Invalid input! Input 1 to add a book.')
        continue

    # add book
    print("Book ISBN: ")
    isbn = input()
    try:
        int(isbn)
    except:
        print("Book ISBN must be integer!")
        continue
    print(book_exists(isbn))
    if not book_exists(isbn):
        print("Book Title: ")
        title = input()
        print("Book Author: ")
        author = input()
        print("Keywords (as comma separated list): ")
        keywords = input()
    print("Number of copies to add: ")
    copies = input()

    props = {
        "title": title if title else None,
        "author": author if author else None,
        "copies": copies,
        "keywords": keywords if keywords else None
    }

    add_book(isbn, props)
