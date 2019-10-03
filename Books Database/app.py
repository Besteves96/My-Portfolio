from utils import database

user_choice = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your Choice: 
"""

def menu():
    database.create_book_table()
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Unknown command. Please try again')

        user_input = input(user_choice)






def prompt_add_book():
    name_input = input('What is the name of the Book you would like to add?')
    author_input = input("What is the name of the Author of the Book?")
    database.add_book(name_input, author_input)

def list_books():
    books = database.get_all_books()
    for n in books:
        Read = 'YES' if n['read'] else 'NO'
        print(f'Name: {n["name"]}, Author: {n["author"]}, Read: {Read}')

def prompt_read_book():
    read_input = input('What is the name of the book you would like to mark as read')

    database.mark_book_as_read(read_input)


def prompt_delete_book():
    delete_input = input('Which Book would you like to delete?')
    database.delete_book(delete_input)




menu()



#def prompt_add_book() ask for book name and authorx
#def list_books() show all books in our listx
#def promt_read_book() ask for book name and change it to "read" in our list
# def prompt_delete_book() ask for book name and remove book from list
