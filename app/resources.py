import json
from collections import OrderedDict

import falcon

from . import session
from .models import User



class UserResource:
	def _extract_data_from_body(self, body):
		body = json.loads(body.decode('utf-8'))
		return body.get('username'), body.get('email')

	def on_get(self, req, resp):
		"""
		OrderedDict used for to keep user fields in order
		"""
		users = [] 
		for user in session.query(User).all():
			d = OrderedDict()
			d['id'] = user.id
			d['username'] = user.username
			d['email'] = user.email
			users.append(d)

		resp.body = json.dumps(users)
		resp.status = falcon.HTTP_200

	def on_post(self, req, resp):
		username, email = self._extract_data_from_body(req.stream.read())

		user = session.query(User).filter(
			(User.username==username) | (User.email==email)).first()
		if not user:
			user = User(username=username, email=email)
			session.add(user)
			session.commit()
			resp.body = 'User has been created.'
			resp.status = falcon.HTTP_302
		else:
			resp.body = b'username or email already in use.'
			resp.status = falcon.HTTP_200

	def on_delete(self, req, resp):
		username, email = self._extract_data_from_body(req.stream.read())
		user = session.query(User).filter(
			(User.username==username) & (User.email==email)).first()
		if user:
			session.delete(user)
			session.commit()
			resp.data = b'user deleted.'
			resp.status = falcon.HTTP_200
		else:
			resp.data = b'user not found.'
			resp.status = falcon.HTTP_404