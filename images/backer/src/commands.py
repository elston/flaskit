import click
from flask.cli import with_appcontext
# ..
from accounts.models import User


@click.command()
@click.option('-u', '--username', prompt=True)
@click.option('-p', '--password', prompt=True, hide_input=True, confirmation_prompt=True)
@with_appcontext
def createadmin(username, password):
    # ...
    admin = User(username=username, password=password)
    admin.is_active = True
    admin.is_admin = True
    admin.save()