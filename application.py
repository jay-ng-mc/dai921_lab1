import redis
import asyncio

r = redis.Redis(host='localhost', port=6379, db=0)

# subscriber functions
def create_subscriber():
    pubsub = r.pubsub()
    return pubsub

def subscribe(pubsub, channel):
    pubsub.subscribe(channel.lower())
    print('Subscribed to ', channel.lower())

def get_messages(pubsub):
    messages = {}
    if not r.pubsub_channels():
        print('No subscribed channels')
        return
    while True:
        message = pubsub.get_message()
        if not message: break
        if message['type']=='message':
            channel = str(message['channel'])
            if channel not in messages.keys(): messages[channel] = []
            messages[channel].append(message['data'])
    if messages: 
        print('New books with id(s): ')
        print(messages)
    else: print('No messages')

def book_exists(book_id):
    book = r.hkeys(book_id)
    print(book)
    if book: return True
    else: return False

def borrow_book(book_id):
    book = r.hgetall(book_id)
    book_copies = int(r.hget(book_id, 'copies'))
    if book_copies > 0:
        r.hincrby(book_id, 'copies', -1)
        print('Borrowed book\nDetails: ')
        print(book)
    else:
        print('No available copies')

def return_book(book_id):
    book = r.hgetall(book_id)
    if not book:
        print('Book not from our library or has expired! (DEBUG): book_id not found')
        return
    r.hincrby(book_id, 'copies', 1)
    print('Returned book')

def inspect_book(book_id):
    book = r.hgetall(book_id)
    print(book)
    print('Inspected book')

# publisher functions
def add_book(book_id, props):
    # check if already exist, just increment copies if exists
    book = r.hkeys(book_id)
    if book:
        copies = int(r.hget(book_id, 'copies')) + int(props['copies'])
        r.hset(name=book_id, key="copies", value=copies)
    else:
        r.hset(name=book_id, mapping=props)

    # publish to channels
    kwlist = [x.strip() for x in props['keywords'].split(',')]
    for kw in kwlist:
        r.publish(kw.lower(), book_id)
    print('added book')
