# example-cli

This provides an example implementation of a cli tool

## Installation

Make sure you have `pipx` installed, to install it:
```
pip install pipx
pipx ensurepath
```
Once it's installed, generate a local build and install the wheel with pipx
```
make clean local-build
pipx install dist/example_cli-0.0.1+local*-py3-none-any.whl --force
```

## Usage

Available commands:
- bye
- hello

## Developer setup

```
python3 -m venv .venv
pip install -r requirements.txt
pip install -r requirements_test.txt 
```

Run the tests and linter:
```
make test
make lint
make coverage
```

### Running locally

Python is always picky about the modules not being in the path:

```
python3 examplecli/entrypoint.py 
Traceback (most recent call last):
  File "/Users/adrian.galera/workspace/gal/example-cli/examplecli/entrypoint.py", line 2, in <module>
    from examplecli.commands.hello import hello_source
ModuleNotFoundError: No module named 'examplecli'
```

You need to manually add it if you want to run it from local:
```
source ./scripts/set-module-in-path.sh
```

And next execution will work:

```
python3 examplecli/entrypoint.py      
Usage: entrypoint.py [OPTIONS] COMMAND [ARGS]...

  Welcome to Example CLI!

Options:
  --help  Show this message and exit.

Commands:
  bye
  hello
```