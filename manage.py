#!/usr/bin/env python

import os
import click
from werkzeug.serving import run_simple

from app import engine, api, Base


@click.group()
def cli():
    pass


@cli.command()
def runserver():
    run_simple("localhost", 5000, api, use_debugger=True, use_reloader=True)


@cli.command()
def initdb():
    if os.path.isfile("data.sqlite"):
        click.echo(
            "You have database file in the current directory"
            "to createad it run dropdb, initdb commands respectively."
        )
    else:
        click.echo("initializing database...")
        Base.metadata.create_all(engine)


@cli.command()
def dropdb():
    filename = "data.sqlite"
    if os.path.isfile(filename):
        os.remove(filename)
        click.echo("dropping database...")
    else:
        click.echo("The database doesn't exists")


if __name__ == "__main__":
    cli()
