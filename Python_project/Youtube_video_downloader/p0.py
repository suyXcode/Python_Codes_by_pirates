from pytube import YouTube
from pytube.exceptions import PytubeError

# Download the video
def download_video(url, output_path="downloads"):
    try:
        print("🔄 Connecting to YouTube...")

        yt = YouTube(url)

        print(f"📹 Title: {yt.title}")
        print("⬇️ Downloading highest resolution...")

        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=output_path)

        print("✅ Download completed successfully!")

    except PytubeError as e:
        print("❌ Pytube Error:", e)

    except Exception as e:
        print("⚠️ Unexpected Error:", e)


if __name__ == "__main__":
    link = input("🔗 Enter YouTube video URL: ").strip()

    if not link:
        print("❌ No URL provided!")
    else:
        download_video(link)
        


# https://youtu.be/X2NVOSNBbxU?si=Bo8mk5dmDUI2OuSe



# from pytube import YouTube


# def clean_url(url):
#     if "youtu.be" in url:
#         video_id = url.split("/")[-1].split("?")[0]
#         return f"https://www.youtube.com/watch?v={video_id}"
#     return url


# link = input("🔗 Enter YouTube video URL: ").strip()
# link = clean_url(link)

# yt = YouTube(link)
# yt.streams.get_highest_resolution().download()

# print("✅ Downloaded successfully!")
