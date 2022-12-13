import click

from examplecli.common.logging import debug, info
from examplecli.commands.options import verbose_option, user_option_required


@click.group()
def bye_source():
    pass


@bye_source.command()
@user_option_required
@verbose_option
def bye(**opts):
    user_name = opts["user"]
    say_bye(user_name)


def say_bye(user_name):
    debug(f"Saying bye to {user_name}")
    info(f"Bye {user_name}")
