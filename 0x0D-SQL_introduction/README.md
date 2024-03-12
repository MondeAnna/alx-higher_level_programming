### [ALX](https://www.alxafrica.com/) System Engineering Plus

Studies carried out in the **[ALX Software Engineering Plus](https://www.alxafrica.com/software-engineering-plus/)** course

<br />

#### Technologies

* Bash:     5.1-6ubuntu1
* Docker:   24.0.5
* MySql:    8.0
* Ubuntu:   20.04 LTS

<br />

#### Primary Concept

[Databases])(DATABASES.md)

<br />

#### Learning Objectives

* At the end of this project, you are expected to be able to `explain to anyone`, **without the help of Google**:
    * What's a database
    * What's a relational database
    * What does SQL stand for
    * What's MySQL
    * How to create a database in MySQL
    * What does `DDL` and `DML` stand for
    * How to `CREATE` or `ALTER` a table
    * How to `SELECT` data from a table
    * How to `INSERT`, `UPDATE` or `DELETE` data
    * What are subqueries
    * How to use MySQL functions

<br />

#### Resources

* _[What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)_
* _[A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)_
* _[Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)_
* _[Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)_
* _[SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)_
* _[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)_
* _[What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)_
* _[MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)_
* _[MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)_
* _[installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)_

<br />

#### Requirements

* Allowed editors:
    * _[vi](https://www.geeksforgeeks.org/vi-editor-unix/)_
    * _[vim](https://www.geeksforgeeks.org/getting-started-with-vim-editor-in-linux/)_
    * _[emacs](https://www.geeksforgeeks.org/emacs-command-in-linux-with-examples/)_

* All source code:
    * Will be compiled on `Ubuntu 20.04 LTS` using `gcc`, using the options
        * `-Wall -Werror -Wextra -pedantic -std=gnu89`
    * To start by a comment describing the task
    * To end with a new line

* All your SQL queries:
    * To have a comment just before (i.e. syntax above)
    * To have uppercased keywords

* A README.md file at the root of:
    * The repo, containing a description of the repository
    * The folder of each project, containing a description of the project

<br />

### Standarisations

#### Explanatory Comments

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

<br />

#### Installation

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

#### Queries

* _[`Show All Databases`](0-list_databases.sql)_
* _[`Create Database`](1-create_database_if_missing.sql)_
* _[`Delete/Drop Database`](2-remove_database.sql)_
* _[`Show All Tables in a Database`](3-list_tables.sql)_
* _[`Create Table`](4-first_table.sql)_
* _[`Describe a Table`](5-full_table.sql)_
* _[`Select All Rows and Columns of Table`](6-list_values.sql)_
* _[`Insert Into Table`](7-insert_value.sql)_
* _[`Select Entries With Characteristic`](8-count_89.sql)_
* _[`Create Table II`](9-full_creation.sql)_
* _[`Ordered Listing`](10-top_score.sql)_
* _[`Conditional Listing`](11-best_score.sql)_
* _[`Update Table`](12-no_cheating.sql)_
* _[`Delete Entries`](13-change_class.sql)_
* _[`Calculate Averge`](14-average.sql)_
* _[`Count Occurances`](15-groups.sql)_
* _[`Select Where Column is Not Null`](16-no_link.sql)_
* _[`Alter Character Encoding`](100-move_to_utf8.sql)_
* _[`Averages`](101-avg_temperatures.sql)_
* _[``](102-top_city.sql)_

<br />
