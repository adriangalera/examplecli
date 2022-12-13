# example-cli

This provides an example implementation of a cli tool

## Installation

Make sure you have `pipx` installed, to install it:
```
pip install pipx
pipx ensurepath
```
Once it's installed:
```
pipx install comms-cli --index-url https://$NEXUS_USERNAME:$NEXUS_PASSWORD@atm.nexus.ocado.tech/repository/pypi/simple
```

## Usage

Available commands:


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
python3 commscli/entrypoint.py
Traceback (most recent call last):
  File "/Users/adrian.galera/workspace/comms/comms-cli/commscli/entrypoint.py", line 2, in <module>
    from commscli.commands.greetings import greetings_source
ModuleNotFoundError: No module named 'commscli.commands'
```

You need to manually add it if you want to run it from local:
```
source ./scripts/set-module-in-path.sh
```

And next execution will work:

```
python3 commscli/entrypoint.py        
Usage: entrypoint.py [OPTIONS] COMMAND [ARGS]...

  Welcome to Comms CLI! For detailed documentation, please visit
  https://gitlab.ocado.tech/comms/comms-cli

Options:
  --help  Show this message and exit.

Commands:
  greet
```

### Retrieve roles and accounts from Temporary Access

The data related with accounts and roles availables is stored in some JSON files inside the package. Normally, the developer should not need to update those JSON files. 

However, when a new retailer account is created or new roles are provisioned, the developer might need to run those scripts to update the available values for accounts or roles

```bash
python3 scripts/extract-accounts-from-ta.py commscli/permissions/accounts.json
python3 scripts/extract-roles-from-ta.py commscli/permissions/roles.json
```

### Troubleshooting

There are some options useful for troubleshooting issues with the automatic permissions:

- `--show-browser`: the automatic browser will run and all the interactions will be visible
- `--verbose`: will log debug messages
- `--store-permissions-html`: will store the HTML from Temporary Access for every interaction