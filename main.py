import yt_dlp  # Import the yt_dlp module for downloading YouTube videos (pip install yt_dlp)
import os  # Import os module for handling file paths
from typing import Final  # Import Final for defining constant variables

# Define the download path as a constant
PATH: Final[str] = "C:/Users/admin/Downloads/"

def main() -> None:
    """
    Main function to download only audio from a provided URL without needing ffmpeg.
    """
    # Prompt the user to input the video URL
    url: str = input("Video-URL: ")

    try:
        # Set download options for yt_dlp to download best audio without conversion
        ydl_opts: dict = {
            'format': 'bestaudio',  # Nur die beste Audioqualität herunterladen
            'outtmpl': os.path.join(PATH, '%(title)s.%(ext)s'),  # Setzt den Ausgabeordner und Dateinamen
            'postprocessors': []  # Leerer postprocessors-Block, um Konvertierung zu vermeiden
        }

        # Initialize yt_dlp with the specified options and download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Confirm successful download
        print(f"Audio downloaded successfully to {PATH}")

    except Exception as e:
        # Handle any errors that occur during the download process
        print(f"An error occurred: {e}")

    input()

if __name__ == "__main__":
    main()
