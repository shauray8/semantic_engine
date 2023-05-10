## cloning PYTUBE no more imports form PyPI !
from pytube import YouTube

# Ask the user for the YouTube video URL
url = "https://www.youtube.com/watch?v=DOWDNBu9DkU"

# Create a YouTube object from the URL
yt = YouTube(url)

# Get the highest resolution video stream
stream = yt.streams.get_audio_only()

# Download the video
print("Downloading...")
stream.download("./Data/")
print("Download complete!")

