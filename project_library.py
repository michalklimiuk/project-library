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

def load_books_from_file():
    try:
        file = open("books.txt")

        for line in file.readlines():
            books.append(line.strip())

        file.close()
    except FileNotFoundError:
        return

def load_borrowed_from_file():
    try:
        file = open("borrowed.txt")

        for line in file.readlines():
            borrowed_books.append(line.strip())

        file.close()
    except FileNotFoundError:
        return

def save_books_to_file():
    file = open("books.txt", "w")
    for book in books:
        file.write(book+"\n")
    file.close()

def save_borrowed_to_file():
    file = open("borrowed.txt", "w")
    for book in borrowed_books:
        file.write(book+"\n")
    file.close()

print("-----------------------------------")
print("Welcome to YourPrivateLibrary")
print("-----------------------------------")
# log_in()
# print("-----------------------------------")

load_books_from_file()
load_borrowed_from_file()

while True:
    print("Library section")
    print("1. Show books")
    print("2. Add a book to library")
    print("3. Remove a book from library")
    print("4. Save books in library\n")
    print("User's section")
    print("5. Show borrowed books")
    print("6. Borrow a book from library")
    print("7. Return a book to library")
    print("8. Save borrowed books\n")
    print("9. Quit")
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
        save_books_to_file()
        print("-----------------------------------")

    if choice == 5:
        show_borrowed_books()
        print("-----------------------------------")
    
    if choice == 6:
        borrow_book()
        print("-----------------------------------")
    
    if choice == 7:
        return_book()
        print("-----------------------------------")
    
    if choice == 8:
        save_borrowed_to_file()
        print("-----------------------------------")
    
    if choice == 9:
        quit()
