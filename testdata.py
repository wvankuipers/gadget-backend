#!/usr/bin/python3

from src.config import config
from src.db import Database

# Projects
Database().write("INSERT INTO project(name, slug) VALUES ('%s', '%s')" % ("My Project", "my-project"))
