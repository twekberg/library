#!/usr/bin/env python
"""
Create a new entry in the library.
"""


import argparse
import sys

from database import Database


def build_parser():
    """
    Collect command line arguments.
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-n', '--noisy', default=False,
                        action='store_true',
                        help='set this to randomize order of the audio files. '
                        'default: %(default)s')
    parser.add_argument('-d', '--database',
                        default='library.db',
                        help='SQLite database file name. '
                        ' Default: %(default)s.')
    return parser


def readline(prompt, default=None):
    """
    Output a prompt and read a string.
    """
    if default:
        sys.stdout.write(f'{prompt} ({default}): ')
    else:
        sys.stdout.write(f'{prompt}: ')

    sys.stdout.flush()
    return sys.stdin.readline().strip() or default


class Book():
    """
    Holder for my books.
    """
    def __init__(self, args):
        self.db = Database(args.database, args.noisy)
        self.author = None


    def enter(self):
        """
        User interface to enter data regarding a book.
        """
        title = readline('Title')
        if not title:
            return None
        self.author = readline('Author', self.author)
        year = int(readline('Year'))
        isbn = readline('ISBN')
        book_number = readline('Book number (1)')
        if not book_number:
            book_number = 1
        return {'title': title,
                'author': self.author,
                'year': year,
                'isbn': isbn,
                'book_number': book_number}


    def create(self, fields):
        """
        Create book record
        """
        self.db.insert('book', fields)


def main(args):
    """
    Starting point.
    """
    book = Book(args)
    while True:
        fields = book.enter()
        if not fields:
            break
        book.create(fields)


if __name__ == '__main__':
    sys.exit(main(build_parser().parse_args()))
