#!/usr/bin/python3
""" engine init """
from os import environ as env

if env["HBNB_TYPE_STORAGE"] == "db":
    from db_storage import DBStorage
    storage = DBStorage()
else:
    from file_storage import FileStorage
    storage = FileStorage()
storage.reload()