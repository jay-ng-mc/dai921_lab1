import redis
import asyncio

r = redis.Redis(host='localhost', port=6379, db=0)

# subscriber functions
def create_subscriber():
    pubsub = r.pubsub()
    return pubsub

def subscribe(pubsub, channel):
    pubsub.subscribe(channel)
    print('Subscribed to ', channel)

def get_messages(pubsub):
    messages = pubsub.get_message()
    print(messages)

def borrow_book(book_id):
    book = r.hgetall(book_id)
    # if int(book['copies']) > 0:
        
    print('borrowed book')

def return_book(book_id):
    book = r.hgetall(book_id)
    print('returned book')

def inspect_book(book_id):
    book = r.hgetall(book_id)
    print('inspected book')

# publisher functions
def add_book(book_id, props):
    # check if already exist, just increment copies if exists
    book = r.hvals(book_id)
    if book:
        r.hset(name=book_id, key="copies", value=book['copies'])
    else:
        r.hset(name=book_id, mapping=props)

    # publish to channels
    kwlist = [x.strip() for x in props['keywords'].split(',')]
    for kw in kwlist:
        r.publish(kw, book_id)
    print('added book')

def debug_publish(channel):
    r.publish(channel, 'test message')