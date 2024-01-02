#!/usr/bin/python3
from py_compile import compile
from os import environ

file = environ["PYFILE"]
compile(file=file, cfile=f"{file}c")
