#!/bin/bash

# Step 1: Run the Python module `venu` with the argument `venu`
python -m venu venu&> /dev/null

# Step 2: Activate the virtual environment
source venv/bin/activate&> /dev/null

# Step 3: Install the `pytubefix` package inside the virtual environment
pip install pytubefix&> /dev/null

# Step 4: Run `main.py` with the provided arguments (inside the virtual environment)
python main.py "$1" "$2"

# Optionally, deactivate the virtual environment
deactivate&> /dev/null
