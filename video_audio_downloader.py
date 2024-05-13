from pytube import YouTube
import moviepy.editor as mp
import sys
import os


def read_urls(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls
"C:\Users\aaliy\Documents\video_audio_downloader.py"
def download_video_as_mp3(url, output_path):

    while True:

        fileFormat = input("To download as mp3 file enter A. To download as mp4 file enter V: ")
        if fileFormat == 'A' or fileFormat == 'a':
        
            try:
                print(f"Attempting to download audio from URL: {url}")
                yt = YouTube(url)
                audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
                output_file = audio_stream.download(output_path=output_path, filename_prefix='temp_')

                # Convert downloaded file to mp3
                print(f"Converting '{output_file}' to MP3...")
                clip = mp.AudioFileClip(output_file)
                mp3_filename = output_file.replace('.mp4', '.mp3').replace('.webm', '.mp3')
                clip.write_audiofile(mp3_filename)

                # Optionally, remove the original download
                os.remove(output_file)

                print(f"Downloaded and converted video to MP3 '{mp3_filename}' successfully.")

            
            except Exception as e:
                print(f"Failed to download and convert audio from {url}: {str(e)}")
            break

        elif fileFormat == 'V' or fileFormat == 'v':
            try:
                print(f"Attempting to download video from URL: {url}")
                yt = YouTube(url)
                print(f"yt {yt}")
                stream = yt.streams
                stream.first().download(output_path)
                print(f"Downloaded '{yt.title}' successfully.")
            except Exception as e:
                print(f"Failed to download {url}: {str(e)}")
            break

        else:
            print("Invalid input. Please enter A for audio file or V for video file.")


def main():
    if len(sys.argv) < 3:
        print("Usage: python download_videos.py [URL_FILE_PATH] [OUTPUT_PATH]")
        sys.exit(1)

    url_file_path = sys.argv[1]
    output_path = sys.argv[2]

    urls = read_urls(url_file_path)
    for url in urls:
        download_video_as_mp3(url, output_path)

if __name__ == "__main__":
    main()



