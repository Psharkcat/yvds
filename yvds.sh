#!/bin/bash

if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found, stopping the script."
    exit 1
fi

source venv/bin/activate&> /dev/null

pip install pytubefix&> /dev/null

python main.py "$1" "$2"

deactivate&> /dev/null
