import logging

from app import books

logger = logging.getLogger('scraper.menu')

USER_CHOICE = '''
Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalgoue
- 'q' to exit


'''



def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key = lambda x: x.star_rating * -1)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding cheapest books....')
    cheapest_books = sorted(books, key = lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

books_generator = (x for x in books)

def get_next_book():
    logger.info('Getting next book from generator of all books...')
    print(next(books_generator))

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n':get_next_book
}
def menu():
    user_input = input(USER_CHOICE)

    while user_input != 'q':

        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command')
        user_input = input(USER_CHOICE)
    logger.debug('Terminating Program.')

menu()