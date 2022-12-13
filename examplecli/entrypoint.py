import click
from examplecli.commands.hello import hello_source
from examplecli.commands.bye import bye_source


WELCOME_MESSAGE = """
Welcome to Example CLI!
"""


def start():
    cli = click.CommandCollection(
        sources=[hello_source, bye_source], help=WELCOME_MESSAGE)
    cli()


if __name__ == '__main__':
    start()
