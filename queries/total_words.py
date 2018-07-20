# An example analysis, for determining
# total number of words across all books.
# Calculates [#books, #words].

def mapper(book):
    words=list(book.words())
    return [1, len(words)]

reducer=double_sum
