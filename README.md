# BIDS-pydantic

## Overview

BIDS-pydantic will pull a specified version (from v1.7.0 onwards, tested up to v1.7.0) of the BIDS metadata schema
which is used in the JSON BIDS sidecar, from the [official BIDS GitHub page](https://github.com/bids-standard/bids-specification/),
and create corresponding [pydantic](https://pydantic-docs.helpmanual.io/) models, which will provide BIDS data validation using
python type annotations.

## Table of Contents

- [Quickstart](#quickstart)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## How To Contribute

Got a great idea for something to implement in BIDS-pydantic, or maybe you have just found a bug?
[Create an issue](https://github.com/gold-standard-phantoms/bids-pydantic/issues) to get in touch with the development team and we’ll take it from there.

## Quickstart

If you just want to use the models in your project. Download the pydantic models file for the BIDS schema version you wish to use
from the [models](models) directory, and add it to your code-base. These files are generated using the `bids-pydantic make -a` command (see below).

If you want to use the command line tool to generate the models, keep reading this README.

## Installation

Install with:

```sh
$ pip install bids-pydantic
```

BIDS-pydantic can be installed as a module directly from the python package index.
For more information how to use a python package in this
way please see [https://docs.python.org/3/installing/index.html](https://docs.python.org/3/installing/index.html)

### Python Version

We recommend using the latest version of Python. BIDS-pydantic supports Python 3.9 and newer.

### Dependencies

These distributions will be installed automatically when installing BIDS-pydantic.

- [pydantic](https://pydantic-docs.helpmanual.io/)
- [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator)

## Usage

The primary commands can be viewed with the command `bids-pydantic`:

```
usage: bids-pydantic [-h] {list,make} ...

Run one of a set of commands. For example: `bids-pydantic list`, or `bids-pydantic make`. Run either
command with `-h` e.g. `bids-pydantic make -h` to get help for that command.

optional arguments:
  -h, --help   show this help message and exit

command:
  {list,make}  subcommand to run
```

The `list` command help can be viewed with the command `bids-pydantic list -h`:

```
usage: bids-pydantic list [-h]

Queries the GitHub API and lists the available supported BIDS schema versions. Only tested up to v1.7.0.

optional arguments:
  -h, --help  show this help message and exit
```

The `make` command help can be viewed with the command `bids-pydantic make -h`:

```
usage: bids-pydantic make [-h] [--output OUTPUT] [--output-all OUTPUT_ALL]
                          [--schema-version [SCHEMA_VERSION]]

Make a new python file(s) containing BIDS compliant pydantic models

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        The output python filename to create (will output to stdout console if not
                        specified).
  --output-all OUTPUT_ALL, -a OUTPUT_ALL
                        Find all parsable schemas and output each to the provided directory. Will create
                        filenames such as bids_schema_model_v_1_7_0.py, etc. Will overwrite any files in
                        that directory with the same name.
  --schema-version [SCHEMA_VERSION]
                        The BIDS schema version to use. e.g. 1.7.0 - supported versions can be
                        discovered using the list command. If a version is not specified v1.7.0 will be
                        used.
  --input INPUT, -i INPUT
                        Specify an input BIDS metadata (yml) file to use instead of downloading a version
                        from GitHub. Cannot be used with --schema-version or --output-all
```

## Development

Development dependencies should be installed using `pip install -r requirements/dev.txt -U`, and `pre-commit install` then run to install code-quality Git hooks.

Development should be carried out using Python 3.8. Development must comply with a few code styling/quality rules and processes:

- Before pushing any code, make sure the `CHANGELOG.md` is updated as per the instructions in the `CHANGELOG.md` file. tox should also be run to ensure that tests and code-quality checks pass.
- The README.md file should be updated with any usage or development instructions.
- Ensure that a good level of test coverage is kept. The test reports will be committed to the CI system when testing is run, and these will be made available during code review. If you wish to view test coverage locally, run `coverage report`.
- To ensure these code quality rules are kept to, [pre-commit](https://pre-commit.com/) should be installed (see the `requirements/dev.txt`), and `pre-commit install` run when first cloning this repo. This will install some pre-commit hooks that will ensure any committed code meets the minimum code-quality and is formatted correctly _before_ being committed to Git. This will ensure that tests will pass on CI system after code is pushed. The tools should also be included in any IDEs/editors used, where possible. To run manually, run `precommit run --all-files`. The following software tools will be run:

  - [mypy](https://github.com/python/mypy)
  - [pylint](https://pylint.org/)
  - [black](https://black.readthedocs.io/en/stable/)
  - [isort](https://isort.readthedocs.io/en/latest/)
  - [pyupgrade](https://github.com/asottile/pyupgrade)

## Acknowledgements

Conversion from schema to pydantic models is carried out using [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator).
Data validation is performed using [pydantic](https://pydantic-docs.helpmanual.io/).

## License

> You can check out the full license [here](LICENSE)
> This project is licensed under the terms of the **MIT** license.
