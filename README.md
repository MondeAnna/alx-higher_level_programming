### [ALX](https://www.alxafrica.com/) System Engineering Plus

Studies carried out in the **[ALX Software Engineering Plus](https://www.alxafrica.com/software-engineering-plus/)** course

<br />

#### Technologies

* Bash:     5.1-6ubuntu1
* Docker:   24.0.5
* GCC:      9.4.0
* Python:   3.8.5
* Ubuntu:   20.04 LTS

<br />

#### Fundamentals

* _[`The Python Tutorial`](https://docs.python.org/3/tutorial/index.html)_
* _[`Python Programming - An Introduction to Computer Science`](https://nibmehub.com/opac-service/pdf/read/Python%20Programming%20_%20an%20introduction%20to%20computer%20science-%203rd%20Edition.pdf)_
* _[`Learn to Program with Python`](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)_
* _[`Python Tutorials for Beginners`](https://thepythonguru.com/)_
* _[`PyFormat`](https://pyformat.info/)_
* _[`Python Garbage Collector Implementations`](https://thp.io/2012/python-gc/python_gc_final_2012-01-22.pdf)_
* _[`A Python Interpreter Written in Python`](https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)_
* _[`Disassembler for Python bytecode`](https://docs.python.org/3.4/library/dis.html)_

<br />

#### Resources
                                                                                         * _[The Python tutorial](https://docs.python.org/3/tutorial/index.html)_
* _[Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)_
* _[Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)_
* _[An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)_
* _[How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)_
* _[Learn to Program](https://m.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)_
* _[Pycodestyle](https://pypi.org/project/pycodestyle/)_

<br />

#### Requirements: General

* Allowed editors:
    * _[vi](https://www.geeksforgeeks.org/vi-editor-unix/)_
    * _[vim](https://www.geeksforgeeks.org/getting-started-with-vim-editor-in-linux/)_
    * _[emacs](https://www.geeksforgeeks.org/emacs-command-in-linux-with-examples/)_

* All source code:
    * Will be interpreted/compiled on `Ubuntu 20.04 LTS`
    * Is to end with a new line
    * The length of your files will be tested using wc

* A README.md file at:
    * The root of the repo, containing a description of the repository
    * The folder of each project, containing a description of the project

<br />

#### Requirements: Python Scripts

* All source code:
    * Will be interpreted/compiled using `python3` version `3.8.5`
    * The first line of all your files should be exactly `#!/usr/bin/python3`
    * Your code should use the `pycodestyle` version `2.8.*`
    * All your files must be executable
    * All your test files should be inside the folder `tests`
    * You have to use the `unittest` module
    * All your test files should be python files (extension: `.py`)
    * All your test files and folders should start with `test_`
    * Your file organization in the tests folder should be the same as your project, for the example `models/base.py`, unit tests must be in: `tests/test_models/test_base.py`
    * All your tests should be executed by using this command: `python3 -m unittest discover tests`
    * You can also test file by file by using this command:
        * `python3 -m unittest tests/test_models/test_base.py`
    * Should have a documentation (`python3 -c 'print(\__import__("my_module").\__doc__)'`)
    * Should have a documentation (`python3 -c 'print(\__import__("my_module").MyClass.\__doc__)'`)
    * All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(\__import__("my_module").my_function.\__doc__)' and python3 -c 'print(\__import__("my_module").MyClass.my_function.\__doc__)'`)
    * A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
    * You are not allowed to use `execute` with sqlalchemy

<br />

#### Requirements: Shell Scripts

* All source code:
    * The first line of all your files should be exactly `#!/bin/bash`
    * All your scripts should be exactly two lines long (`wc -l file` should print `2`)
    * All your files must be executable

#### Requirements: SQL Scripts

* All source code:
    * Will be executed with `MySQLdb` version `2.0.x`
    * Will be executed with `SQLAlchemy` version `1.4.x`

* All your SQL queries:
    * To have a comment just before (i.e. syntax above)
    * To have uppercased keywords

<br />

#### Requirements: C Scripts

* All source code:
    * Will be compiled using `gcc`, with the options
        * `-Wall -Werror -Wextra -pedantic -std=gnu89`
    * Not to use `stdlib's` _[system](https://www.geeksforgeeks.org/system-call-in-c/)_
    * To have no errors and no warnings during compilation
    * To use the _[Betty](https://github.com/alx-tools/Betty)_ style.
    * To have it's best practices checked using [betty-style.pl](https://github.com/alx-tools/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/alx-tools/Betty/blob/master/betty-doc.pl)
    * Global variables are not allowed
    * No more than 5 functions per file
    * The prototypes of all your functions should be included in your header file called `lists.h`
    * Don't forget to push your header file
    * All your header files should be include guarded

#### Requirements: `.txt` Answer Files

* All text files should have these qualities:
    * Only one line
    * No Shebang
    * End with a new line

<br />

#### Notice on the checking of Python projects

* Based on the requirements of each task, **you should always write the documentation (module(s) + function(s)) and tests first**, before you actually code anything
* The intranet checks for Python projects won't be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
* We strongly encourage you to work together on test cases, so that you don't miss any edge case. **But not in the implementation of them!**
* **Don't trust the user**, always think about all possible edge cases

<br />

### SQL Standardisations

#### Explanatory Comments

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

<br />

#### Installation: SQLAlchemy ORM

```
$ sudo apt update
$ sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config
$ # inside a venv
$ pip install mysqlclient
```

<br />

#### Installation: MySQL

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

<br />

#### Connecting to MySQL server

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

<br />

#### Importing a Dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl <url> -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$
```

#### Cheat Sheet

![MySQL-Cheat-Sheet](./img/mysql-joins.png)

<br />

#### High Level Programming Concepts

* _[Python Code Interpretation](https://www.geeksforgeeks.org/what-is-python-interpreter/)_
* _[Conditional Statements](https://www.geeksforgeeks.org/python-if-else/)_, _[Loops](https://www.geeksforgeeks.org/loops-in-python/)_ and _[Functions](https://www.geeksforgeeks.org/python-functions/)_
* _[Modules](https://www.geeksforgeeks.org/python-modules/)_
* _[Lists](https://www.geeksforgeeks.org/python-lists/)_ and _[Tuples](https://www.geeksforgeeks.org/python-tuples/)_
* _[Sets](https://www.geeksforgeeks.org/python-sets/)_ and _[Dictionaries](https://www.geeksforgeeks.org/python-dictionary/)_
* _[Exceptions](https://www.geeksforgeeks.org/errors-and-exceptions-in-python/)_
* _[Test Driven Development](https://www.geeksforgeeks.org/test-driven-development-tdd/)_
* _[Object Orientated Programming](https://www.geeksforgeeks.org/python-oops-concepts/)_
* _[Inheritance](https://www.geeksforgeeks.org/inheritance-in-python/)_
* _[Input/Output](https://www.geeksforgeeks.org/input-and-output-in-python/)_
* _[MySQL](https://www.geeksforgeeks.org/what-is-mysql/)_
* _[Introduction to JavaScript](https://www.geeksforgeeks.org/introduction-to-javascript/)_
* _[Python-SQL ORM](https://www.geeksforgeeks.org/sqlalchemy-introduction/)_

<br />
