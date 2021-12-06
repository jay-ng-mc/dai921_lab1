from application import *

pubsub = create_subscriber()

while True:
# get action
    print("""

1. Borrow book
2. Return book
3. Inspect book
4. Subscribe to channel
5. Check new messages
""")
    action = input()
    if action not in [str(x) for x in range(1,6)]:
        print("Invalid input! Input just the integer of your choice.")
        continue

# get book id
    if action in [str(x) for x in range (1, 4)]:
        print("\nBook ISBN: ")
        book_id = input()
        try:
            int(book_id)
        except:
            print("Book ISBN must be integer")
            continue
    
    elif action == "4":
        print("\nChannel name: ")
        channel = input()

# do action
    if action == "1": borrow_book(book_id)
    elif action == "2": return_book(book_id)
    elif action == "3": inspect_book(book_id)
    elif action == "4": subscribe(pubsub, channel)
    elif action == "5": get_messages(pubsub)
    else: print('Action failed (DEBUG)')
