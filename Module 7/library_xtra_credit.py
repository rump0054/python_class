# Author: Erik Rumppe
# Date: 7/9/2026

from functools import total_ordering

@total_ordering
class Book:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.genre = ''
        self.isbn = ''
        self.tags = {}

    def set_fields(self, title, author, genre, isbn, tags):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.tags = tags

    def __str__(self):
        return f"{self.title} by {self.author} in {self.genre}.  {self.isbn}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def __gt__(self, other):
        return NotImplemented

# Add book to collection if not already present then return new collection.
def add_book(collection, title, author, genre, isbn, tags):
    # search through collection and make sure ISBN isn't already there
    # if not found, create a new book
    if get_book(collection, isbn) != ():
        print("ISBN already taken")
    else:
        book = Book()
        book.set_fields(title, author, genre, isbn, tags)

        # add new book to collection
        collection.append(book)

    return collection

# Get book if ISBN found
def get_book(collection, isbn):
    # loop through your books check if the ISBN matches the isbn parameter
    for my_book in collection:
        # if it does, return the book
        if my_book.isbn == isbn:
            return my_book

    return ()

# Get books with ALL tags from param present in tag field
def books_with_tags(collection, tags):
    books = []
    # loop through every book in collection
    for book in collection:
        # check if the book's tags have every tag in tags using tags.issubset()
        if tags.issubset(book.tags):
            books.append(book)
    return books

# Create empty book collection
my_collection = []

my_collection = add_book(my_collection, "The Way of Kings","Brandon Sanderson","Fantasy",
    "9780765365279", {"epic", "long", "trauma", "violence"})
my_collection = add_book(my_collection, "Luck In The Shadows", "Lynn Flewelling", "Fantasy",
    "9780553575422", {"espionage", "adventure", "friendship", "mentorship", "magic", "lgbt"})
my_collection = add_book(my_collection,"Magic's Price", "Mercedes Lackey", "Fantasy",
    "9780886774264", {"epic", "magic", "duty", "love", "sacrifice", "lgbt"})
my_collection = add_book(my_collection,"Dissolution", "Richard Lee Byers","Fantasy",
    "9780786929443", {"epic", "dark", "faith", "power", "survival"})
my_collection = add_book(my_collection,"God Emperor of Dune", "Frank Herbert", "Sci Fi",
    "9780593098257", {"power", "religion", "leadership", "humanity"})

assert len(my_collection) == 5, "Should only have five books"

# Test method books_with_tags
tag_books = books_with_tags(my_collection, {"epic", "long", "trauma", "violence"})
assert len(tag_books) == 1, "Only one book matches"

tag_books = books_with_tags(my_collection, {"epic"})
assert len(tag_books) == 3, "3 books have epic tag"

tag_books = books_with_tags(my_collection, {"epic", "religion"})
assert len(tag_books) == 0, "0 books have epic and power tags"

for book in my_collection:
    print(book)