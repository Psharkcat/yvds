from pytubefix import YouTube
import os
import sys
import platform
import subprocess

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
        print(f"Downloading audio: {yt.title}...")
        download_folder = get_download_folder('audio')
        stream.download(output_path=download_folder)
        print("Done.")
    except Exception as e:
        print(f"Error: {e}")

def video_download(link):
    try:
        yt = YouTube(link)

        # Download the video without the audio for better quality
        print(f"Downloading video: {yt.title} ... ")
        video_stream = yt.streams.filter(only_video=True).order_by("resolution").desc().first()
        download_folder = get_download_folder('video')
        video_stream.download(filename = "video")

        # Download the audio
        audio_stream = yt.streams.get_by_itag(140)
        audio_stream.download(filename = "audio")


        # Combining the video and the audio
        output_file = os.path.join(download_folder, f"{yt.title}.mp4")

        ffmpeg_command = [
            "ffmpeg",
            "-y",  # Overwrite existing files
            "-i", "video.mp4",
            "-i", "audio.m4a",
            "-c:v", "copy",
            "-c:a", "aac",
            output_file
        ]
        subprocess.run(ffmpeg_command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)        
        # Cleanup temporary files
        os.remove("audio.m4a")
        os.remove("video.mp4")
        
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