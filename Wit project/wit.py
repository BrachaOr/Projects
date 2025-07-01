#! python
import click

from Repository import *


@click.group()
def cli():
    pass

@cli.command()
def init():
    """Initialize the repository."""
    rep = Repository()
    rep.wit_init()

@cli.command()
@click.argument('file_name')
def add(file_name):
    """Add a file to the staging area."""
    rep = Repository()
    rep.wit_add(file_name)

@cli.command()
@click.argument('message')
def commit(message):
    """Commit the staged files with a message."""
    rep = Repository()
    rep.wit_commit(message)

@cli.command()
def log():
    """Show the commit log."""
    rep = Repository()
    rep.wit_log()


@cli.command()
def status():
    """Show the status of the repository."""
    rep = Repository()
    rep.wit_status()

@cli.command()
@click.argument('commit_id')
def checkout(commit_id):
    """Checkout a specific commit."""
    rep = Repository()
    rep.wit_checkout(commit_id)

if __name__ == '__main__':
    cli()