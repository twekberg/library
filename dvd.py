#!/usr/bin/env python
"""
Create a new DVD entry in the library.
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
                        help='Display diagnostic messages. '
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
    answer = sys.stdin.readline().strip() or default
    if answer == '-':
        answer = ''
    return answer


def get_int(prompt, default=None):
    """
    Get am int or None.
    """
    value = readline(prompt, default)
    if value:
        value = int(value)
    return value


class Dvd():
    """
    Holder for my DVDs.
    """
    def __init__(self, args):
        self.db = Database(args.database, args.noisy)
        self.star = None
        self.disk_count = 1

    def enter(self):
        """
        User interface to enter data regarding a DVD.
        """
        title = readline('DVD Title')
        if not title:
            return None
        star = readline('Star', self.star)
        if star:
            self.star = star
        else:
            star = self.star
        year = get_int('Year')
        episode = readline('Episode/Season')
        multiple_movies = bool(int(readline('Multiple Movies', '0')))
        disk_count = readline('# of disks', self.disk_count)
        if disk_count:
            self.disk_count = disk_count
        else:
            disk_count = self.disk_count
        return {'title': title,
                'star': star,
                'year': year,
                'episode': episode,
                'disk_count': disk_count,
                'multiple_movies': multiple_movies}


    def create(self, fields):
        """
        Create dvd record
        """
        self.db.insert('dvd', fields)
        if fields['multiple_movies']:
            dvd_id = self.db.get_id('dvd')
            while True:
                title = readline('Movie Title')
                if not title:
                    break
                episode = readline('Episode/Season')
                self.db.insert('movie', {'dvd_id': dvd_id,
                                         'title': title,
                                         'episode': episode})
                


def main(args):
    """
    Starting point.
    """
    dvd = Dvd(args)
    while True:
        fields = dvd.enter()
        if not fields:
            break
        dvd.create(fields)


if __name__ == '__main__':
    sys.exit(main(build_parser().parse_args()))
