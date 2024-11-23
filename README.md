#  Youtube Videos Download Script 

A simple Python script that allows you to download YouTube videos and audio files. The script can be run from the command line and automatically saves the files to your system's default media folders (Music for audio and Videos for video).

## Features

- **Download audio** (MP3 format)
- **Download video** (Highest resolution)
- Automatically saves the media to appropriate folders (`Music` for audio and `Videos` for video) depending on the OS.

## Requirements

- Python 3.x
- **pytubefix** library: This is used to interact with the YouTube API to download videos and audio.

## Installation

### Step 1: Clone the repository or download the script

**Clone from GitHub:**
   ```bash
   git clone https://github.com/Psharkcat/yvds.git
   cd yvds
   ```
### Step 2: Install dependencies

You need to install the required Python packages, including `pytubefix`, which can be done with the following command:

```bash
pip install pytubefix
```

This will install the `pytubefix` library, which is used for downloading media from YouTube.

## Usage

### Step 1: Open your terminal (Command Prompt, PowerShell, Terminal, etc.)

### Step 2: Run the script with the appropriate command-line argument

- **To download audio:**

   If you want to download the audio (MP3 format), use the `-a` option followed by the YouTube video link:
   
   ```bash
   main.py -a <video link>
   ```

- **To download video:**

   If you want to download the video (in the highest available resolution), use the `-v` option followed by the YouTube video link:
   
   ```bash
   python main.py -v <video link>
   ```

### Output Location

- On **Windows**, the downloaded files will be saved in:
  - Audio: `C:\Users\<YourUsername>\Music`
  - Video: `C:\Users\<YourUsername>\Videos`

- On **Linux** and **Mac**:
  - Audio: `~/Music`
  - Video: `~/Videos` or `~/Movies` for Mac

### Step 3: Wait for the download to complete

The script will show a message indicating that it is downloading the audio or video, and once finished, it will display a "Done." message.

## Notes

- This script uses `pytubefix` to download media from YouTube. If YouTube changes its API or page structure, `pytubefix` may need to be updated to handle the changes.
  
- The script supports both **audio** and **video** downloads, but only the highest resolution for video and the audio stream with the lowest bitrate for audio.

## Troubleshooting

1. **`ModuleNotFoundError` for `pytubefix`**:  
   Ensure that `pytubefix` is installed using `pip install pytubefix`.

2. **Permission issues**:  
   If you encounter permission issues when trying to download the files, ensure you have write access to the download folders (`Music`, `Videos`).

3. **Network issues**:  
   Make sure your internet connection is stable as YouTube downloads may fail with an unstable connection.

## License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

---
