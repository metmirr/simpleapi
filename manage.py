#!/usr/bin/env python
from werkzeug.serving import run_simple

from app import app, engine
from app.models import Base

def create_tables():
	Base.metadata.create_all(engine)

if __name__ == '__main__':
	run_simple('localhost', 5000, app, use_debugger=True, use_reloader=True)
