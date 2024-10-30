import sys

from lib.controls import create_database

if "database" in sys.argv:
    create_database()
