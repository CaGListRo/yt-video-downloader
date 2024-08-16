import yt_dlp  # Import the yt_dlp module for downloading YouTube videos (pip install yr_dlp)
import os  # Import os module for handling file paths
from typing import Final  # Import Final for defining constant variables

# Define the download path as a constant
PATH: Final[str] = "C:/Users/admin/Downloads/"

def main() -> None:
    """
    Main function to download a video from a provided URL.
    """
    # Prompt the user to input the video URL
    url: str = input("Video-URL: ")

    try:
        # Set download options for yt_dlp
        ydl_opts: dict = {
            'format': 'best',  # Selects the best quality format available
            'outtmpl': os.path.join(PATH, '%(title)s.%(ext)s')  # Sets the output path and filename template
        }

        # Initialize yt_dlp with the specified options and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Confirm successful download
        print(f"Video downloaded successfully to {PATH}")

    except Exception as e:
        # Handle any errors that occur during the download process
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()