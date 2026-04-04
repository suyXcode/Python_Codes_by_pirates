
from pytube import YouTube


def clean_url(url):
    if "youtu.be" in url:
        video_id = url.split("/")[-1].split("?")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    return url


link = input("🔗 Enter YouTube video URL: ").strip()
link = clean_url(link)

yt = YouTube(link)
yt.streams.get_highest_resolution().download()

print("✅ Downloaded successfully!")
