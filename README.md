# Library
These are the books I own.

# Installation

Install with this command:

  git clone git@github.com:twekberg/library.git

No virtualenv is needed.

It assumes that sqlite is installed. The author used DB Browser for
SQLite to inspect the data.

# Use

## Overview

There are two data entry programs:
  book.py
  dvd.py

They have their own table in the library.db sqlite database.

## Run
  
These programs will prompt for the fields. Those fields that have
defaults and show the default in ()s in the prompt. When entering
multiple books using book.py, when one moves from one book to another,
the previous entries for several fields are used: Author and Series,
with Book number defaulting to 1.

The dvd.py works the same way, allowing defaults for the Star and # of
disks, with Multiple Movies defaulting to '0' (False). When Multple
Movies is True, this means that the DVD contains multiple videos. In
that case, the Movie Title and Episode/Season fields are prompted
for and recorded in the movie table.

# Database

The name of the sqline database is library.db.
At some point I'll write a set of queries to display the data in various
ways using Python.
Until then, write your own using DB Browser for SQLite.
