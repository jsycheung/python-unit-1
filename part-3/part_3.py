my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below


def book_info(book):
    info_string = f'The title of the book is {book["title"]}. It is written by {book["author"]} in {book["year"]}. It has {book["pages"]} pages and a rating of {book["rating"]}.'
    return info_string


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def title_info(book):
    title = book['title']
    title_string = f'The title of the book is {title}.'
    return title_string


def author_info(book):
    author = book['author']
    author_string = f'The author of the book is {author}.'
    return author_string


def year_info(book):
    year = book['year']
    year_string = f'The book is written in {year}.'
    return year_string


def rating_info(book):
    rating = book['rating']
    rating_string = f'The title of the book is {rating}.'
    return rating_string


def pages_info(book):
    pages = book['pages']
    pages_string = f'The book has {pages} pages.'
    return pages_string

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

# Get a list of information for each book given a list of dictionaries


def info_list(book_list):
    info_list = []
    for book in book_list:
        info_list += book_info(book)
    return info_list

# Get a list of comments about the book


def get_comments(*args):
    comments_list = []
    for comment in args:
        comments_list += comment
    return comments_list

# Create a new dictionary


def new_dict(**kwargs):
    return kwargs
