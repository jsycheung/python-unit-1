# Step 1 - Input function

# Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
book_list = ["1984", "Journey to the West", "The Hunger Games",
             "Harry Potter", "Quantum Chemistry", "Physical Chemistry"]


def create_book():
    title = input('What is the book title? ')
    author = input('Who is the author? ')
    try:
        year = int(input('In what year was it written? '))
    except:
        year = int(input('Please type a number for the year. '))
    try:
        pages = int(input('How many pages are there? '))
    except:
        pages = int(input('Please type a number for pages.'))
    try:
        rating = float(input('Give a rating to this book. '))
    except:
        rating = float(input('Please type a number for rating '))
    book_dict = {
        'title': title,
        'author': author,
        'year': year,
        'rating': rating,
        'pages': pages
    }
    book_list.append(book_dict['title'])
    print(f'New book added. The updated book list is {book_list}')


# Step 2 - Type conversion

# Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here


# Step 3 - Error handling

# Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here


# Step 4 - if/elif/else

# Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
ongoing = True


def main_menu():
    option = input(
        'Type "add" for adding new book, "all" for seeing all books, "search" for searching a book, "end" to end action. ').lower()
    if option == "add":
        create_book()
    elif option == "all":
        print(book_list)
    elif option == "search":
        keyword = input('Please input keyword. ').lower()
        result_list = []
        for book in book_list:
            if keyword in book.lower():
                result_list.append(book)
        if len(result_list) == 0:
            print('no books found')
        else:
            print(result_list)
    elif option == "end":
        global ongoing
        ongoing = False


while ongoing == True:
    main_menu()
# Step 5 - while loops

# Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
