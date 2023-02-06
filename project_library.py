import getpass

books = []
book_id = 0
borrowed_books = []

def log_in():

    input_username = str(input("Enter your username: "))
    input_password = getpass.getpass("Enter your password: ")

    while True:
        if input_username == 'username' and input_password == 'password':
            print("-----------------------------------")
            print('You have successfully logged in.')
            break
        else:
            print("Something's wrong, Try again.")
            print("-----------------------------------")
            continue

def add_book():
    book_id = len(books)
    author = str(input("Enter author's name: "))
    name = str(input("Enter book's name: "))
    
    book_id += 1
    book = (f'{book_id} - Author: {author} - Title: {name}')
    
    books.append(book)
    print(f"Book added to library")

def show_books():
    print("Books in library: ", books)

def show_borrowed_books():
    print("Borrowed books: ", borrowed_books)

def remove_book():
    print(books)
    book_to_remove_id = int(input("Enter ID of book to remove: "))
    books.remove(books[book_to_remove_id - 1])
    print(f"Book removed from library")

def borrow_book():
    show_books()
    book_to_borrow_id = int(input("Enter ID of book to borrow: "))
    borrowed_books.append(books[book_to_borrow_id - 1])
    books.remove(books[book_to_borrow_id - 1])
    
    print(f"Book borrowed from library")

def return_book():
    show_borrowed_books()
    book_to_remove_id = int(input("Enter ID of book to return to library: "))
    books.append(borrowed_books[book_to_remove_id - 1])
    borrowed_books.remove(borrowed_books[book_to_remove_id - 1])
    
    print(f"Book removed from library")
    


# print("-----------------------------------")
# print("Welcome to YourPrivateLibrary")
# print("-----------------------------------")
# log_in()
# print("-----------------------------------")

while True:
    print("Library section")
    print("1. Show books")
    print("2. Add a book to library")
    print("3. Remove a book from library\n")
    print("User's section")
    print("4. Show borrowed books")
    print("5. Borrow a book from library")
    print("6. Return a book to library")
    print("-----------------------------------")
    choice = int(input("What do you want to do?: "))
    

    if choice == 1:
        show_books()
        print("-----------------------------------")

    if choice == 2:
        add_book()
        print("-----------------------------------")
    
    if choice == 3:
        remove_book()
        print("-----------------------------------")

    if choice == 4:
        show_borrowed_books()
        print("-----------------------------------")
    
    if choice == 5:
        borrow_book()
        print("-----------------------------------")
    
    if choice == 6:
        return_book()
        print("-----------------------------------")