# Import pytube library to download video
import pytube

# YouTube video URL
url = input("Enter video url: ")

# Target directory of downloaded video
path = "./download"

pytube.YouTube(url).streams.get_highest_resolution().download(path)