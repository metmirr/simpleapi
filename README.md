
A simple api, to demonstrate usage of falcon framework.
Sqlalchemy for the database operations.

**Usage:**

	$ pip install -r requirements.txt
	$
	$ python
	>>> import manage
	>>> manage.create_tables()

Now you have a database and ready to use falcon api:

	$ python manage.py
-----------------------------------------------------------------------------
**Methods:**

    $ pip install httpie

_get_:

    $ http localhost:5000/user username==foo email==foo@bar.com
    HTTP/1.0 200 OK
    content-length: 39
    content-type: application/json; charset=UTF-8
    {
        "email": "foo@bar", 
        "username": "foo"
    }

_post_:

	$ http post localhost:5000/user username==foo email==foo@bar.com

_delete_:

	$ http delete localhost:5000/user username==foo email==foo@bar.com


