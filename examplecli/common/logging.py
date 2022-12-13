import sys
from datetime import datetime
from colorama import Fore, Style
from examplecli.commands.options import is_verbose_option


INFO_COLOR = Fore.GREEN
ERROR_COLOR = Fore.RED
DEBUG_COLOR = Fore.LIGHTCYAN_EX
WARN_COLOR = Fore.YELLOW


def info(msg):
    print(Fore.WHITE + current_date_str() +
          " | " + INFO_COLOR + msg, Style.RESET_ALL)


def warn(msg):
    print(Fore.WHITE + current_date_str() + " | " + WARN_COLOR + msg, Style.RESET_ALL,
          file=sys.stderr)


def debug(msg):
    if is_verbose_option():
        print(Fore.WHITE + current_date_str() + " | " + DEBUG_COLOR + msg, Style.RESET_ALL,
              file=sys.stderr)


def error(msg):
    print(Fore.WHITE + current_date_str() + " | " + ERROR_COLOR + msg, Style.RESET_ALL,
          file=sys.stderr)


def panic(msg):
    error(msg)
    sys.exit(1)


def current_date_str():
    echo_date_fmt = "%Y-%m-%dT%H:%M:%S.%f"
    return datetime.utcnow().strftime(echo_date_fmt)[:-3] + "Z"
