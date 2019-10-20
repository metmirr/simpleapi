# Simple REST API with falcon framework

A simple api, to demonstrate usage of falcon framework. It uses sqlite for database and sqlalchemy as orm.

## Install Requirements
You can use virtualenv, pipenv or python builtin venv module to create an environmen. I will be using pipenv:

```shell
$ pipenv --python 3.7
$ pipenv shell && pipenv install
```
After requirements installation create a database file with command below:

```shell
$ python manage.py initdb
```

If you see this message *You have database file in the current directoryto createad it run dropdb, initdb commands respectively.* run `python manage.py dropdb` and `python manage.py dropdb` commands

Now you have a database and ready to use falcon api. Let`s run the server:

```shell
$ python manage.py runserver
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 227-578-359
```


**Methods:**

```shell
$ sudo pip install httpie
```

Calling http methods:

**get**:

```shell
$ http localhost:5000/user username==foo email==foo@bar.com
HTTP/1.0 200 OK
content-length: 39
content-type: application/json; charset=UTF-8
{
    "email": "foo@bar",
    "username": "foo"
}
```

**post**:

```shell
$ http post localhost:5000/user username=foo email=foo@bar.com
```

**delete**:

```shell
$ http delete localhost:5000/user username==foo
```
