#!/bin/bash

python -m venu venu&> /dev/null

source venv/bin/activate&> /dev/null

pip install pytubefix&> /dev/null

python main.py "$1" "$2"

deactivate&> /dev/null
