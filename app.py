import json
from collections import OrderedDict

import falcon

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///data.sqlite")
session = sessionmaker(engine)()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    email = Column(String(64), unique=True)

    def to_json(self):
        return {"username": self.username, "email": self.email}


class Index(object):
    def on_get(self, req, resp):
        msg = {
            "message": "It's a simple api written with falcon",
            "database": "sqlite",
            "orm": "sqlalchemy",
        }
        resp.body = json.dumps(msg)


class UserResource(object):
    def on_get(self, req, resp):
        username = req.get_param("username")
        user = session.query(User).filter((User.username == username)).first()
        if user:
            resp.body = json.dumps(user.to_json())
            resp.status = falcon.HTTP_200
        else:
            resp.body = b"User not found!"
            resp.status = falcon.HTTP_404

    def on_post(self, req, resp):
        username = req.get_param("username")
        email = req.get_param("email")

        user = (
            session.query(User)
            .filter((User.username == username) | (User.email == email))
            .first()
        )
        if user is None:
            user = User(username=username, email=email)
            session.add(user)
            session.commit()
            resp.body = "User has been created."
            resp.status = falcon.HTTP_302
        else:
            resp.body = b"Username or email already in use."
            resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        username = req.get_param("username")
        email = req.get_param("email")
        user = (
            session.query(User)
            .filter((User.username == username) & (User.email == email))
            .first()
        )
        if user is not None:
            session.delete(user)
            session.commit()
            resp.data = b"User deleted."
            resp.status = falcon.HTTP_200
        else:
            resp.data = b"User not found."
            resp.status = falcon.HTTP_404


api = falcon.API()
api.add_route("/", Index())
api.add_route("/user", UserResource())
