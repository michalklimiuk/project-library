import getpass

books = []

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
    author = str(input("Enter author's name: "))
    name = str(input("Enter book's name: "))

    book = author + " - " + name

    books.append(book)

def show_books():
    print("Books in library: ", books)

print("-----------------------------------")
print("Welcome to your library")
print("-----------------------------------")
log_in()
print("-----------------------------------")

while True:
    print("1. Show books")
    print("2. Add a book to library")
    choice = int(input("What do you want to do?: "))
    

    if choice == 1:
        show_books()

    if choice == 2:
        add_book()