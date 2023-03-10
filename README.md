# project-library

Introduction
YourPrivateLibrary is a Python console application that allows users to add, remove and borrow books from a library. It is a simple implementation of a library management system with basic functionality like saving books to a file and loading books from the file.

Usage
To use this program, you need to run the Python script in a console. You can do this by navigating to the folder where the script is located and running it by typing the command python3 <filename>.py.

After running the program, you will be presented with a menu that lists all available options. Choose an option by typing the number corresponding to the action you want to perform.

Actions
Show books: This action will show all the books that are currently in the library.
Add a book to library: This action will allow you to add a new book to the library.
Remove a book from library: This action will allow you to remove a book from the library.
Save books in library: This action will save all the books currently in the library to a file.
Show borrowed books: This action will show all the books that are currently borrowed from the library.
Borrow a book from library: This action will allow you to borrow a book from the library.
Return a book to library: This action will allow you to return a book to the library.
Save borrowed books: This action will save all the borrowed books to a file.
Quit: This action will quit the program.
Note: Before using the program, you need to log in with your username and password. The default username and password are "username" and "password", respectively. You can change these in the code by editing the corresponding lines.

File Management
The program saves books and borrowed books to files. The books are saved in the "books.txt" file, and the borrowed books are saved in the "borrowed.txt" file. When you run the program, it will load the books and borrowed books from these files, and when you save the books or borrowed books, it will overwrite the contents of the corresponding file.

Conclusion
YourPrivateLibrary is a simple Python console application that allows users to manage a library. It is a basic implementation of a library management system with basic functionality like adding, removing, and borrowing books. The program saves books and borrowed books to files and loads them when the program is run.

```
-----------------------------------
Welcome to YourPrivateLibrary      
-----------------------------------
Enter your username: username
Enter your password: 
-----------------------------------
You have successfully logged in.   
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library      
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 1
Books in library:  []
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 2
Enter author's name: author1
Enter book's name: title1
Book added to library
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 3
['1 - Author: author1 - Title: title1']
Enter ID of book to remove: 1
Book removed from library
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 1
Books in library:  []
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 2
Enter author's name: author2
Enter book's name: title2
Book added to library
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 6
Books in library:  ['1 - Author: author2 - Title: title2']
Enter ID of book to borrow: 1
Book borrowed from library
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 5
Borrowed books:  ['1 - Author: author2 - Title: title2']
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 7
Borrowed books:  ['1 - Author: author2 - Title: title2']
Enter ID of book to return to library: 1
Book returned from library
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 5
Borrowed books:  []
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 1
Books in library:  ['1 - Author: author2 - Title: title2']
-----------------------------------
Library section
1. Show books
2. Add a book to library
3. Remove a book from library
4. Save books in library

User's section
5. Show borrowed books
6. Borrow a book from library
7. Return a book to library
8. Save borrowed books

9. Quit
-----------------------------------
What do you want to do?: 9
```
