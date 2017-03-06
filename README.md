
A simple api to demonstrate usage of falcon framework.
Sqlalchemy for the database operations.


Usage:

	$ pip install -r requirements.txt

	in project folder:

	$ python
	>>> import manage
	>>> manage.create_tables()

	Now you have a database and ready to use falcon api:

	$ python manage.py


Methods
-----------------------------------------------------------------------------

get

	Open address in browser, should see an empty list for first time

post

	$ pip install httpie

	$ http post localhost:5000 username=foo email=foo@bar.com

delete

	$ http delete localhost:5000 username=foo email=foo@bar.com


