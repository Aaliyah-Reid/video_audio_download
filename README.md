# Youtube Video and Audio Downloader

## Features

- Downloads content from YouTube URLs.
- Provides the flexibility to choose between downloading audio or video files.
- Supports batch processing of multiple URLs from a file.

## Setup

- Python 3.x
- PyTube library (`pip install pytube`)
- MoviePy library (`pip install moviepy`)

## How to Use

1. **Clone the repository:**

    ```
    git clone https://github.com/Your-Username/video_audio_download.git
    ```

2. **Navigate to the directory:**

    ```
    cd video_audio_download
    ```

3. **Run the script using:**

    ```
    python video_audio_downloader.py [URL_FILE_PATH] [OUTPUT_PATH]
    ```

    Replace `[URL_FILE_PATH]` with the path to a text file containing YouTube URLs (one URL per line).
    Replace `[OUTPUT_PATH]` with the directory where you want to save the downloaded files.

Upon execution, you'll be prompted to choose whether to download the content as audio or video files.
