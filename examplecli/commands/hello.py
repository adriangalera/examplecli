import click

from examplecli.common.logging import debug, info
from examplecli.commands.options import verbose_option, user_option_required


@click.group()
def hello_source():
    pass


@hello_source.command()
@verbose_option
@user_option_required
def hello(**opts):
    user_name = opts["user"]
    say_hello(user_name)


def say_hello(user_name):
    debug(f"Saying hello to {user_name}")
    info(f"Hello {user_name}")
