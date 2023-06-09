# BIDS-pydantic-models

## Overview

BIDS-pydantic-models is a series of [pydantic](https://pydantic-docs.helpmanual.io/)
models which validate against versions of the BIDS metadata schema which is used in the
JSON BIDS sidecar, from the [official BIDS GitHub page](https://github.com/bids-standard/bids-specification/)

Each model is created using BIDS-pydantic.

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
$ pip install bids-pydantic-models
```

BIDS-pydantic-models can be installed as a module directly from the python package index.
For more information how to use a python package in this
way please see [https://docs.python.org/3/installing/index.html](https://docs.python.org/3/installing/index.html)

### Python Version

We recommend using the latest version of Python. BIDS-pydantic supports Python 3.9 and newer.

### Dependencies

These distributions will be installed automatically when installing BIDS-pydantic-models.

- [pydantic](https://pydantic-docs.helpmanual.io/) - currently only compatible with v1

## Usage

Just import the model you want to use:

```python
from bids_pydantic_models.bids_metadata_v1_7_0 import BidsMetadata
```

then use the class as you would with any other pydantic model. For example:
```python
bids_metadata = BidsMetadata(
    EchoTime=5.0, BolusCutOffFlag=True
)
bids_metadata.LabelingDuration=1.0

with open("bids_metadata.json", "w") as f:
    f.write(bids_metadata.json(indent=4, exclude_unset=True))
```

For more information, reference the
[pydantic documentation](https://pydantic-docs.helpmanual.io/)

Currently supported
schema versions are:

- v1.7.0
- v1.8.0

NOTE: the model files in the Git repository may not correspond directly with those that are installed using pip.
This is due to the fact that the models are auto-generated by GSPs CI/CD system. However, version information
is always displayed at the top of the model files.

## Acknowledgements

Conversion from schema to pydantic models is carried out using [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator).
Data validation is performed using [pydantic](https://pydantic-docs.helpmanual.io/).

## License

> You can check out the full license [here](LICENSE)
> This project is licensed under the terms of the **MIT** license.
