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


class Index(object):
    def on_get(self, req, resp):
        msg = {
            "message": "It's a simple api written with falcon",
            "database": "sqlite",
            "orm": "sqlalchemy",
        }
        resp.body = json.dumps(msg)


class UserResource(object):
    def __init__(self):
        """OrderedDict use to keep user fields in order"""
        self.d = OrderedDict()

    def on_get(self, req, resp):
        user = (
            session.query(User)
            .filter(
                (User.username == req.get_param("username"))
                | (User.email == req.get_param("email"))
            )
            .first()
        )
        if user:
            self.d["username"] = user.username
            self.d["email"] = user.email
            resp.body = json.dumps(self.d)
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
        if not user and username and email:
            user = User(username=username, email=email)
            session.add(user)
            session.commit()
            resp.body = "User has been created."
            resp.status = falcon.HTTP_302
        else:
            resp.body = b"username or email already in use."
            resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        user = (
            session.query(User)
            .filter(
                (User.username == req.get_param("username"))
                & (User.email == req.get_param("email"))
            )
            .first()
        )
        if user:
            session.delete(user)
            session.commit()
            resp.data = b"user deleted."
            resp.status = falcon.HTTP_200
        else:
            resp.data = b"user not found."
            resp.status = falcon.HTTP_404


api = falcon.API()
api.add_route("/", Index())
api.add_route("/user", UserResource())
