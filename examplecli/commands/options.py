import click

user_option_required = click.option(
    "--user",
    required=True
)

verbose_option = click.option(
    "--verbose",
    default=False,
    is_flag=True
)


def is_verbose_option():
    try:
        click_ctx = click.get_current_context()
        verbose = click_ctx.params["verbose"]
        return verbose
    except RuntimeError:
        return False
