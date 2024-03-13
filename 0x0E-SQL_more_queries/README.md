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
    * How to create a new MySQL user
    * How to manage privileges for a user to a database or table
    * What's a `PRIMARY KEY`
    * What's a `FOREIGN KEY`
    * How to use `NOT NULL` and `UNIQUE` constraints
    * How to retrieve datas from multiple tables in one request
    * What are subqueries
    * What are `JOIN` and `UNION`

<br />

#### Resources

* _[How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)_
* _[How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)_
* _[MySQL constraints](https://zetcode.com/mysql/constraints/)_
* _[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)_
* _[Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)_
* _[SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)_
* _[SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)_
* _[SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)_
* _[MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)_
* _[The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)_
* _[MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)_
* _[SQL Style Guide](https://www.sqlstyle.guide/)_
* _[MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)_
* _[Design](https://www.guru99.com/database-design.html)_
* _[Normalization](https://www.guru99.com/database-normalization.html)_
* _[ER Modeling](https://www.guru99.com/er-modeling.html)_

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

#### Importing a Dump: Option 1

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl <url> -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$
```

<br />

#### Importing a Dump: Option 2

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl <url> -s
$ mysql -uroot -p < <dump>
Enter password: 
$
```

<br />

#### Cheat Sheet

![MySQL-Cheat-Sheet](./img/mysql-joins.png)

<br />

#### Queries

* _[`Grants`](0-privileges.sql)_
* _[`Create Super User`](1-create_user.sql)_

<br />