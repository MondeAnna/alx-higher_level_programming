### [ALX](https://www.alxafrica.com/) System Engineering Plus

Studies carried out in the **[ALX Software Engineering Plus](https://www.alxafrica.com/software-engineering-plus/)** course.

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don't ask me how to pronounce it...) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be "What can I do with my objects" and not "How this object is stored? where? when?". You won't write any SQL queries only Python code. Last thing, your code won't be "storage type" dependent. You will be able to change your storage easily without re-writing your entire project.

<br />

#### Without ORM

```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

<br />

#### With an ORM:

```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

<br />

Do you see the difference? Cool, right? The biggest difficulty with ORM is: The syntax! Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don't read the entire documentation before starting, just jump on it if you don't get something.

<br />

#### Technologies

* Bash:     5.1-6ubuntu1
* Docker:   24.0.5
* GCC:      9.4.0
* Python:   3.8.5
* Ubuntu:   20.04 LTS

<br />

#### Learning Objectives

* At the end of this project, you are expected to be able to `explain to anyone`, **without the help of Google**:
    * Why Python programming is awesome
    * How to connect to a MySQL database from a Python script
    * How to `SELECT` rows in a MySQL table from a Python script
    * How to `INSERT` rows in a MySQL table from a Python script
    * What ORM means
    * How to map a Python Class to a MySQL table
    * How to create a Python Virtual Environment

<br />

#### Resources

* _[Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)_
* _[mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)](https://mysqlclient.readthedocs.io/)_
* _[MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)_
* _[SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)_
* _[SQLAlchemy](https://docs.sqlalchemy.org/en/13/)_
* _[mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)_
* _[Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)_
* _[Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)_
* _[10 common stumbling blocks for SQLAlchemy newbies](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)_
* _[Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)_
* _[SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)_
* _[SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)_
* _[Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)_

<br />

#### High Level Programming Concepts

* _[`Select States`](0-select_states.py)_
* _[`Filter States`](1-filter_states.py)_
* _[`User Filtered State`](2-my_filter_states.py)_
* _[`Safely Filtered User Query`](3-my_safe_filter_states.py)_
* _[`Join Tables`](4-cities_by_state.py)_
* _[`Query Cities in User Provided State`](5-filter_cities.py)_
* _[`Create State Model`](model_state.py)_
* _[`List State Objects from Database`](7-model_state_fetch_all.py)_
* _[`Print First State in Database`](8-model_state_fetch_first.py)_
* _[`Filter State Model Objects`](9-model_state_filter_a.py)_
* _[`Filter State Model Objects with User Arg`](10-model_state_my_get.py)_
* _[`Insert State`](11-model_state_insert.py)_
* _[`Update State`](12-model_state_update_id_2.py)_
* _[`Delete States`](13-model_state_delete_a.py)_
* _[`Create City Model`](model_city.py)_
* _[`Fetch City by State`](14-model_city_fetch_by_state.py)_
* _[`State Relations`](relationship_state.py)_ and _[`City Relations`](relationship_city.py)_
* _[`State-to-City Relations`](100-relationship_states_cities.py)_

<br />
