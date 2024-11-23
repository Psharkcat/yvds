from pytubefix import YouTube
import os
import sys
import platform

def get_download_folder(media_type):

    user_home = os.path.expanduser("~")

    if platform.system() == "Windows":

        if media_type == 'audio':
            return os.path.join(user_home, "Music")
        elif media_type == 'video':
            return os.path.join(user_home, "Videos")

    elif platform.system() == "Linux":

        if media_type == 'audio':
            return os.path.join(user_home, "Music")
        elif media_type == 'video':
            return os.path.join(user_home, "Videos")

    elif platform.system() == "Darwin":

        if media_type == 'audio':
            return os.path.join(user_home, "Music")
        elif media_type == 'video':
            return os.path.join(user_home, "Movies")


def audio_download(link):
    try:
        yt = YouTube(link)
        stream = yt.streams.get_by_itag(140)
        print(f"Downloading audio: {stream.title}...")
        download_folder = get_download_folder('audio')
        stream.download(output_path=download_folder)
        print("Done.")
    except Exception as e:
        print(f"Error: {e}")

def video_download(link):
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        download_folder = get_download_folder('video')
        print(f"Downloading video: {stream.title}...")
        stream.download(output_path=download_folder)
        print("Done.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    try:
        if sys.argv[1] == "-a":
            audio_download(sys.argv[2])
        elif sys.argv[1] == "-v":
            video_download(sys.argv[2])
        else:
            print("Bad argument")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
