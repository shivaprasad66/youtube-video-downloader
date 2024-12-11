import yt_dlp

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': save_path + '/%(title)s.%(ext)s',  # Save path
        'format': 'best',  # Download the best quality available
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

video_url = input("Please enter the YouTube video URL: ")
save_path = "C:/Users/akar4/Downloads/"  # Change to your desired path
download_video(video_url, save_path)
