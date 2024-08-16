# YouTube Video Downloader Script

This Python script allows you to download YouTube videos by providing a URL. The video will be downloaded in the best available quality and saved to a specified directory.

## Requirements

- Python 3.6 or higher
- `yt-dlp` module

## Installation

1. Install Python 3 from the official website: [python.org](https://www.python.org/).
2. Install the `yt-dlp` package using pip:

   ```bash
   pip install yt-dlp
   ```

## Usage

1. Clone this repository or download the script.
2. Open the script in a Python IDE or text editor.
3. Update the `PATH` variable in the script to the desired download directory.
4. Run the script:

   ```bash
   python download_script.py
   ```

5. When prompted, enter the URL of the YouTube video you wish to download.

## Customization

- **Download Path**: You can change the download directory by modifying the `PATH` variable.
- **Download Format**: The script is set to download the best available quality. You can adjust the `ydl_opts` dictionary to specify a different format or quality.

## Error Handling

If an error occurs during the download process, the script will print an error message. Ensure that the URL is correct and that you have an active internet connection.

## License

This project is licensed under the MIT License.
