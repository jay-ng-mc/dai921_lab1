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
    print("Book Title: ")
    title = input()
    print("Book Author: ")
    author = input()
    print("Number of copies to add: ")
    copies = input()
    print("Keywords (as comma separated list): ")
    keywords = input()

    props = {
        "title": title,
        "author": author,
        "copies": copies,
        "keywords": keywords
    }

    add_book(isbn, props)
