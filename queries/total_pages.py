# An example analysis, for determining
# total number of pages across all books.
# Calculates [#books, #pages].

def mapper(book):
    return [1, book.pages]

reducer=double_sum
