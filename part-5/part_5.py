# Step 1 - Store data in a .txt

# This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def create_book():
    title = input('What is the book title? ')
    author = input('Who is the author? ')
    try:
        year = int(input('In what year was it written? '))
    except:
        year = int(input('Please type a number for the year. '))
    try:
        rating = float(input('Give a rating to this book. '))
    except:
        rating = float(input('Please type a number for rating '))
    try:
        pages = int(input('How many pages are there? '))
    except:
        pages = int(input('Please type a number for pages.'))
    with open("library.txt", "a+") as f:
        f.write(f'{title}, {author}, {year}, {rating}, {pages}\n')

# Step 2 - Read data from a .txt

# Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here


def show_books():
    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            line = line.split(", ")

            book_dictionary = {
                "title": line[0],
                "author": line[1],
                "year": line[2],
                "rating": line[3],
                "pages": line[4][:-1]
            }

            title = book_dictionary["title"]
            author = book_dictionary["author"]
            year = book_dictionary["year"]
            rating = book_dictionary["rating"]
            pages = book_dictionary["pages"]

            print(
                f"{title} written by {author} in {year} with {pages} pages, {rating} rating.")


def search_book(keyword, query):
    with open("library.txt", "r") as f:
        file = f.readlines()
        search_count = 0
        for line in file:
            line = line.split(", ")

            book_dictionary = {
                "title": line[0],
                "author": line[1],
            }

            title = book_dictionary["title"]
            author = book_dictionary["author"]
            if keyword in book_dictionary[query].lower():
                print(f"{title} by {author}")
                search_count += 1
        if search_count == 0:
            print("no books found")


def find_pages():
    with open("library.txt", "r") as f:
        file = f.readlines()
        page_sum = 0
        for line in file:
            line = line.split(", ")
            page_sum += int(line[4][:-1])
        print(f"Total number of pages in all books is {page_sum}")


def find_rating():
    with open("library.txt", "r") as f:
        file = f.readlines()
        rating_sum = 0
        for line in file:
            line = line.split(", ")
            rating_sum += float(line[3])
        print(f"Average rating of all books is {rating_sum/len(file)}")


ongoing = True


def main_menu():
    option = input(
        'Type "add" for adding new book, "all" for seeing all books, "search" for searching a book,\n"pages" to see total number of pages, "rating" to see average rating, "end" to end action. ').lower()
    if option == "add":
        create_book()
    elif option == "all":
        show_books()
    elif option == "search":
        query = input(
            'Search by title or author? Type "title" or "author" to select. ').lower()
        keyword = input(
            'Please input keyword. ').lower()
        search_book(keyword, query)
    elif option == "pages":
        find_pages()
    elif option == "rating":
        find_rating()
    elif option == "end":
        global ongoing
        ongoing = False

# Step 3 - if __name__ == "__main__":

# Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.


# Code this at the bottom of the script
if __name__ == "__main__":
    while ongoing == True:
        main_menu()


# Step 4 - Expand and refactor

# Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!
