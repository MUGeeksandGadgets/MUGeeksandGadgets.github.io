#!/usr/bin/env python
# bake.py - generate the library
from os import listdir
from os.path import join
from collections import namedtuple
from functools import reduce
from operator import concat

def readfile(path):
    """Read and return a file's contents as a string."""
    with open(path, 'r') as f:
        return reduce(concat, f.readlines())

def listjoindir(*parts):
    """List the contents of a directory named by the joined parts."""
    return listdir(join(*parts))

def cameltotitle(s):
    """Convert a string from camel case to title case."""
    acc = ''

    for letter in s:
        if letter.isupper():
            acc += ' '
        acc += letter

    return acc.capitalize()

def isacronym(s):
    """Return whether a string is an acronym (is all caps)."""
    return s == s.upper()

# Useful data type.

Book = namedtuple('Book', 'book document title cover')

# Collect data on all books.

shelves = {}
genrecovers = {}

# Iterate through the genres...
for g in listjoindir('contents', 'library'):
    shelves[g] = []

    # Iterate through the genre's books...
    for b in listjoindir('contents', 'library', g):
        # Skip the genre's cover file but add it to our dict of those.
        if b.endswith('.jpg'):
            genrecovers[g] = b
            continue

        # Find the book's files.
        files = listjoindir('contents', 'library', g, b)

        # Extract data about the book.
        book = b
        title = cameltotitle(b)
        cover = list(filter(lambda f: f.endswith('.jpg'), files))[0]
        document = list(filter(lambda f: not f.endswith('.jpg'), files))[0]

        # Put the book on its shelf.
        shelves[g].append(Book(book, document, title, cover))

# Read in all the templates.

genretemplate = readfile('templates/genre.html')
booktemplate = readfile('templates/book.html')
radiotemplate = readfile('templates/radio.html')
librarytemplate = readfile('templates/library.html')

# Generate genreradios & genreshelves which we need
# for creating the final page.

genreradios = ''
genreshelves = ''
for g in shelves.keys():
    # Add this genre's radio to the list of radios.
    genreradios += radiotemplate.format(genre=g)

    booklinks = ''
    for b in shelves[g]:
        booklinks += booktemplate.format(genre=g,
                                         book=b.book,
                                         document=b.document,
                                         title=b.title,
                                         cover=b.cover)

    genrepretty = ''
    if isacronym(g):
        genrepretty = g
    else:
        genrepretty = g.capitalize()

    # Add this genre and its books to the list of shelves.
    genreshelves += genretemplate.format(genre=g,
                                         genrepretty=genrepretty,
                                         genrecover=genrecovers[g],
                                         radio=g + 'Radio',
                                         booklinks=booklinks)

# Load the analytics blurb.
analytics = readfile('templates/analytics.html')

# Output the final library page.
print(librarytemplate.format(genreradios=genreradios,
                             genreshelves=genreshelves,
                             analytics=analytics))
