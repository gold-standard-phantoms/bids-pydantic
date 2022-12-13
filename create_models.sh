#!/bin/bash

cd src
python -m bids_pydantic.cli make --output-all ../models/src/bids_pydantic_models/
