import falcon

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///data.sqlite')
session = sessionmaker(engine)()


from .resources import UserResource


# routes
app = falcon.API()
app.add_route('/', UserResource())
