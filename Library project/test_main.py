from main import *
def test_add_book():
    library = Library()
    book = Book("Harry Potter", "J.K", 1869)

    library.add_book(book)

    assert len(library.books) == 1
    assert library.books[0].title == "Harry Potter"



