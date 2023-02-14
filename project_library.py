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
    with open("books.txt") as file_books:
        for line in file_books:
            pass
        last_line_books = line

    with open("borrowed.txt") as file_borrowed:
        for line in file_borrowed:
            pass
        last_line_borrowed = line

    if last_line_borrowed[0] > last_line_books[0]:
        book_id = int(last_line_borrowed[0])

    if last_line_borrowed[0] < last_line_books[0]:
        book_id = int(last_line_books[0])

    author = str(input("Enter author's name: "))
    name = str(input("Enter book's name: "))

    book_id += 1
    book = (f'{book_id} - Author: {author} - Title: {name}')
    
    books.append(book)
    print(f"Book added to library")
    save_books_to_file()

def show_books():
    print("Books in library: ", books)

def show_borrowed_books():
    print("Borrowed books: ", borrowed_books)

def remove_book():
    print(books)
    
    while True:
        try:
            book_to_remove_id = int(input("Enter ID of book to remove: "))
            result = ''.join([element for element in books if element.startswith(f'{book_to_remove_id}')])
            books.remove(result)
            break
        except ValueError:
            print("Enter correct value.")
            continue
        
    print(f"Book removed from library")

def borrow_book():
    show_books()

    while True:
        try:
            book_to_borrow_id = int(input("Enter ID of book to borrow: "))

            result = ''.join([element for element in books if element.startswith(f'{book_to_borrow_id}')])
    
            borrowed_books.append(result)
            books.remove(result)
            break
        except ValueError:
            print("Enter correct value.")
            continue

    print(f"Book borrowed from library")

def return_book():
    show_borrowed_books()
    
    while True:
        try:
            book_to_remove_id = int(input("Enter ID of book to return to library: "))

            result = ''.join([element for element in borrowed_books if element.startswith(f'{book_to_remove_id}')])
            books.append(result)
            borrowed_books.remove(result)
            break
        except ValueError:
            print("Enter correct value.")
            continue

    print(f"Book returned from library")

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
